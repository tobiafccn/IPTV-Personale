#!/usr/bin/env python3
"""Unisce guide XMLTV pubbliche per i soli canali di IPTV-Personale.

La playlist mantiene i propri tvg-id e riceve una guida unica, utilizzabile
anche dai player che accettano una sola fonte EPG.
"""
from collections import defaultdict
from copy import deepcopy
from hashlib import sha1
from pathlib import Path
from os import environ
from urllib.request import Request, urlopen
import gzip
import re
import unicodedata
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parent
PLAYLIST = ROOT / "playlist-rock-tv.m3u"
GUIDE = ROOT / "epg-rock-tv.xml.gz"
# GITHUB_REPOSITORY segue automaticamente il nuovo nome dopo una rinomina.
REPO_SLUG = environ.get("GITHUB_REPOSITORY") or "tobiafccn/IPTV-Personale"
GUIDE_URL = f"https://raw.githubusercontent.com/{REPO_SLUG}/main/epg-rock-tv.xml.gz"
SOURCES = (
    ("Italia (EPGShare)", "https://epgshare01.online/epgshare01/epg_ripper_IT1.xml.gz", True),
    ("Pluto Italia", "https://raw.githubusercontent.com/matthuisman/i.mjh.nz/master/PlutoTV/it.xml.gz", True),
    ("Pluto USA (canali internazionali)", "https://raw.githubusercontent.com/matthuisman/i.mjh.nz/master/PlutoTV/us.xml.gz", False),
)

def normalize(value):
    value = re.sub(r"\s*\((?:Italia - )?sperimentale\)", "", value, flags=re.I)
    value = re.sub(r"\s*\((?:English|verificare)\)", "", value, flags=re.I)
    value = unicodedata.normalize("NFKD", value).casefold()
    return "".join(ch for ch in value if ch.isalnum() and not unicodedata.combining(ch))

def read_channels():
    text = PLAYLIST.read_text(encoding="utf-8-sig")
    entries = []
    for line in text.splitlines():
        if not line.startswith("#EXTINF:"):
            continue
        name = line.split(",", 1)[-1].strip()
        found = re.search(r'tvg-id="([^"]+)"', line)
        if not found:
            raise RuntimeError(f"Manca il tvg-id per {name}: rigenerare prima la M3U")
        entries.append({"name": name, "id": found.group(1), "norm": normalize(name)})
    if len(entries) < 100 or len({e["id"] for e in entries}) != len(entries):
        raise RuntimeError("Elenco canali incompleto o tvg-id duplicati")
    return text, entries

def download_xml(url):
    request = Request(url, headers={"User-Agent": "IPTV-Personale-EPG/1.0"})
    with urlopen(request, timeout=75) as response:
        data = response.read()
    if data.startswith(b"\x1f\x8b"):
        data = gzip.decompress(data)
    document = ET.fromstring(data)
    if document.tag != "tv" or not document.findall("channel"):
        raise RuntimeError(f"Non e' un file XMLTV valido: {url}")
    return document

def main():
    playlist_text, entries = read_channels()
    # Priorita': EPG italiano, poi Pluto Italia, infine Pluto USA.
    matched = {}
    programmes = defaultdict(list)
    for title, url, required in SOURCES:
        try:
            root = download_xml(url)
        except Exception as exc:
            if required:
                raise RuntimeError(f"Fonte EPG obbligatoria indisponibile ({title}): {exc}") from exc
            print(f"Fonte EPG facoltativa non disponibile: {title}: {exc}")
            continue

        by_id = {}
        by_name = defaultdict(set)
        for channel in root.findall("channel"):
            source_id = channel.get("id")
            if not source_id:
                continue
            by_id[source_id] = channel
            for label in channel.findall("display-name"):
                if label.text:
                    by_name[normalize(label.text)].add(source_id)

        source_targets = {}
        for entry in entries:
            target_id = entry["id"]
            if target_id in matched:
                continue
            source_id = target_id if target_id in by_id else None
            # Solo un nome identico e non ambiguo puo' ricevere un EPG per alias.
            if source_id is None and target_id.startswith("rocktv."):
                options = by_name.get(entry["norm"], set())
                if len(options) == 1:
                    source_id = next(iter(options))
            if not source_id:
                continue
            if source_id in source_targets:
                continue
            matched[target_id] = deepcopy(by_id[source_id])
            matched[target_id].set("id", target_id)
            source_targets[source_id] = target_id

        added = 0
        for programme in root.findall("programme"):
            target_id = source_targets.get(programme.get("channel"))
            if target_id:
                programme_copy = deepcopy(programme)
                programme_copy.set("channel", target_id)
                programmes[target_id].append(programme_copy)
                added += 1
        print(f"{title}: {len(source_targets)} canali, {added} programmi")

    with_programmes = [e for e in entries if programmes.get(e["id"])]
    programme_count = sum(len(v) for v in programmes.values())
    if len(with_programmes) < 20 or programme_count < 200:
        raise RuntimeError(
            f"Guida incompleta: {len(with_programmes)} canali, {programme_count} programmi; "
            "la guida precedente rimane invariata"
        )
    output = ET.Element("tv", {"generator-info-name": "IPTV-Personale EPG unificata"})
    for channel in entries:
        identifier = channel["id"]
        if not programmes.get(identifier):
            continue
        output.append(matched[identifier])
    for channel in entries:
        output.extend(programmes[channel["id"]])

    xml_bytes = ET.tostring(output, encoding="utf-8", xml_declaration=True)
    new_guide = gzip.compress(xml_bytes, compresslevel=9, mtime=0)
    # Scrivere la playlist solo dopo aver generato una guida valida.
    header, sep, body = playlist_text.partition("\n")
    if not header.startswith("#EXTM3U") or not sep:
        raise RuntimeError("Intestazione M3U non valida")
    new_playlist = f'#EXTM3U x-tvg-url="{GUIDE_URL}"\n{body}'
    GUIDE.write_bytes(new_guide)
    PLAYLIST.write_text(new_playlist, encoding="utf-8")
    print(f"EPG pubblicata: {len(with_programmes)} canali su {len(entries)}, "
          f"{programme_count} programmi, {len(new_guide)} byte compressi.")

if __name__ == "__main__":
    main()

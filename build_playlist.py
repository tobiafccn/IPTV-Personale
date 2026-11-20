#!/usr/bin/env python3
"""Aggiorna la playlist OpenIPTVItaly, aggiunge radio e video rock, e filtra i canali esclusi."""
from pathlib import Path
from urllib.request import Request, urlopen
import re

ROOT = Path(__file__).resolve().parent
SOURCE = "https://raw.githubusercontent.com/xN1ckuz/OpenIPTVItaly/main/OpenIPTVItaly.m3u"
LICENSE = "https://raw.githubusercontent.com/xN1ckuz/OpenIPTVItaly/main/LICENSE"
RADIOS = (
    (
        "181.FM - Rock 181",
        "https://listen.181fm.com/181-rock_128k.mp3"
    ),
    (
        "ROCK ANTENNE - Modern Rock",
        "https://stream.rockantenne.de/modern-rock/stream/mp3"
    ),
    (
        "ROCK ANTENNE - Modern Metal",
        "https://stream.rockantenne.de/modern-metal/stream/mp3"
    ),
    (
        "ROCK ANTENNE - Hard Rock",
        "https://stream.rockantenne.de/rock-antenne-hard-rock/stream/mp3"
    ),
    (
        "ROCK ANTENNE - Alternative",
        "https://stream.rockantenne.de/alternative/stream/mp3"
    ),
    (
        "TheBlast.FM - Christian Rock (verificare)",
        "https://mediacp.theblast.fm/stream/theblast"
    )
) 
VIDEOS = (
    (
        "RadioU TV (USA)",
        "https://cdnlive.radiou.com/LS-ATL-43240-1/index.m3u8"
    ),
    (
        "Rock TV (Romania)",
        "https://tv.broadcasting.ro/rocktv/85c83a80-4f71-4f2d-a8d6-43f676896bcb.m3u8"
    ),
    (
        "Muzzik Rock&Roll (Serbia - da provare)",
        "https://muzzik-live.morescreens.com/mts-1/playlist.m3u8"
    )
)

def download(url):
    request = Request(url, headers={"User-Agent": "RockTV-Personale/1.0"})
    with urlopen(request, timeout=45) as response:
        return response.read().decode("utf-8-sig").replace("\r\n", "\n")

def add_channels(base):
    lines = [base.rstrip(), ""]
    for group, start, stations in (("RADIO ROCK", 901, RADIOS), ("ROCK TV", 951, VIDEOS)):
        for number, (name, url) in enumerate(stations, start=start):
            lines.extend((
                f'#EXTINF:-1 tvg-chno="{number}" tvg-name="{name}" group-title="{group}",{name}',
                url,
            ))
    return "\n".join(lines) + "\n"

def filter_channels(playlist):
    file = ROOT / "canali_da_escludere.txt"
    exclusions = set()
    if file.exists():
        exclusions = {
            line.strip().casefold()
            for line in file.read_text(encoding="utf-8-sig").splitlines()
            if line.strip() and not line.lstrip().startswith("#")
        }
    result = []
    include = True
    excluded = []
    for line in playlist.splitlines():
        if line.startswith("#EXTINF:"):
            name = line.split(",", 1)[-1].strip()
            match = re.search(r'tvg-chno="([^"]+)"', line)
            number = match.group(1) if match else ""
            include = name.casefold() not in exclusions and number.casefold() not in exclusions
            if not include:
                excluded.append(name)
        if include:
            result.append(line)
    return "\n".join(result).rstrip() + "\n", excluded

def main():
    original = download(SOURCE).strip()
    count = original.count("#EXTINF:")
    if not original.startswith("#EXTM3U") or count < 25:
        raise RuntimeError("Fonte OpenIPTVItaly non valida. Playlist precedente conservata.")
    playlist, excluded = filter_channels(add_channels(original))
    license_text = download(LICENSE)
    (ROOT / "playlist-rock-tv.m3u").write_text(playlist, encoding="utf-8")
    (ROOT / "LICENSE_OPENIPTVITALY.txt").write_text(license_text, encoding="utf-8")
    print(f"Fonte: {count} TV; + {len(RADIOS)} radio; + {len(VIDEOS)} video; esclusi: {len(excluded)}")
    for name in excluded:
        print("Escluso:", name)

if __name__ == "__main__":
    main()

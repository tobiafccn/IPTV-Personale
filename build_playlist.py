#!/usr/bin/env python3
"""Aggiorna OpenIPTVItaly, riordina le categorie e applica le esclusioni persistenti."""
from pathlib import Path
from urllib.request import Request, urlopen
from collections import defaultdict
import re

ROOT = Path(__file__).resolve().parent
SOURCE = "https://raw.githubusercontent.com/xN1ckuz/OpenIPTVItaly/main/OpenIPTVItaly.m3u"
LICENSE = "https://raw.githubusercontent.com/xN1ckuz/OpenIPTVItaly/main/LICENSE"
CATEGORY_ORDER = ("TV ITALIANA", "FILM E SERIE", "DOCUMENTARI E SCIENZA", "ANIME", "WRESTLING E MMA", "MOTORSPORT", "ROCK TV", "RADIO ROCK",)
FILM_SERIE = set(("20Mediaset HD", "Rai 4", "Iris HD", "Rai Movie", "Rai Premium", "Cielo HD", "27Twentyseven HD", "LA7 Cinema", "La5 HD", "Cine34 HD", "Giallo", "Top Crime HD", "Italia 2 HD", "Mediaset Extra HD",))
DOC_SCIENCE = set(("Rai 5", "FOCUS HD", "Discovery", "DMAX", "Rai Storia HD", "Discovery Turbo", "BBC Top Gear Italy",))
ANIME_EXISTING = set(("MAN-GA",))
MOTOR_EXISTING = set(("ACI Sport TV HD", "Rally.TV FAST+",))
RADIOS = (("181.FM - Rock 181", "https://listen.181fm.com/181-rock_128k.mp3"), ("ROCK ANTENNE - Modern Rock", "https://stream.rockantenne.de/modern-rock/stream/mp3"), ("ROCK ANTENNE - Modern Metal", "https://stream.rockantenne.de/modern-metal/stream/mp3"), ("ROCK ANTENNE - Hard Rock", "https://stream.rockantenne.de/rock-antenne-hard-rock/stream/mp3"), ("ROCK ANTENNE - Alternative", "https://stream.rockantenne.de/alternative/stream/mp3"), ("TheBlast.FM - Christian Rock (verificare)", "https://mediacp.theblast.fm/stream/theblast"),)
ROCK_ROMANIA = ("Rock TV (Romania)", "https://tv.broadcasting.ro/rocktv/85c83a80-4f71-4f2d-a8d6-43f676896bcb.m3u8")
EXTRA_CHANNELS = (("DOCUMENTARI E SCIENZA", 970, "Documentary+", "https://ef79b15c8c7c46c7a9de9d33001dbd07.mediatailor.us-west-2.amazonaws.com/v1/master/ba62fe743df0fe93366eba3a257d792884136c7f/LINEAR-859-DOCUMENTARYPLUS-DOCUMENTARYPLUS/mt/documentaryplus/859/hls/master/playlist.m3u8"),
    ("DOCUMENTARI E SCIENZA", 971, "NHK World-Japan (English)", "https://masterpl.hls.nhkworld.jp/hls/w/live/smarttv.m3u8"),
    ("DOCUMENTARI E SCIENZA", 972, "DW English", "https://dwamdstream102.akamaized.net/hls/live/2015525/dwstream102/master.m3u8"),
    ("DOCUMENTARI E SCIENZA", 973, "France 24 English", "https://live.france24.com/hls/live/2037218/F24_EN_HI_HLS/master_2300.m3u8"),
    ("ANIME", 980, "Pluto TV Anime (sperimentale)", "https://jmp2.uk/plu-5812b7d3249444e05d09cc49.m3u8"),
    ("WRESTLING E MMA", 990, "PFL MMA (sperimentale)", "https://jmp2.uk/plu-6334a574605f140007e233c4.m3u8"),
    ("WRESTLING E MMA", 991, "TNA Wrestling (sperimentale)", "https://jmp2.uk/plu-59b722526996084038c01e1b.m3u8"),
    ("MOTORSPORT", 995, "Red Bull TV", "https://rbmn-live.akamaized.net/hls/live/590964/BoRB-AT/master_3360.m3u8"),
    ("MOTORSPORT", 996, "Motorvision+ (English)", "https://r.eu.cdn-redge.media/livehls/oeu/mt/live/motorvision_en/live.livx/playlist.m3u8"),
    ("ROCK TV", 960, "XITE Rock x Metal", "https://d198ro05q94rc4.cloudfront.net/XITE_Rock_On.m3u8"),
    ("ROCK TV", 961, "XITE Rock On - stream alternativo (sperimentale)", "https://jmp2.uk/plu-623a1b5188ecdc0007c9ef5a.m3u8"),
    ("ROCK TV", 962, "Vevo Rock (sperimentale)", "https://jmp2.uk/plu-61d4b38226b8a50007fe03a6.m3u8"),
    ("ROCK TV", 963, "Vevo 2K (sperimentale)", "https://jmp2.uk/plu-5fd7bca3e0a4ee0007a38e8c.m3u8"),
    ("ROCK TV", 964, "Metaleitor TV - alternativa Metal TV Core (sperimentale)", "https://vs20.live.opencaster.com/metaleitortv_423d3342/index.m3u8"),)

def download(url):
    request = Request(url, headers={"User-Agent": "RockTV-Personale/1.0"})
    with urlopen(request, timeout=45) as response:
        return response.read().decode("utf-8-sig").replace("\r\n", "\n")

def split_channels(text):
    lines = text.splitlines()
    if not lines or not lines[0].startswith("#EXTM3U"):
        raise ValueError("Il file M3U non contiene un'intestazione valida")
    result, current = [], None
    for line in lines[1:]:
        if line.startswith("#EXTINF:"):
            if current is not None:
                result.append(current)
            current = [line]
        elif current is not None:
            current.append(line)
    if current is not None:
        result.append(current)
    return lines[0], result

def channel_name(block):
    return block[0].split(",", 1)[-1].strip()

def category(name):
    if name in FILM_SERIE:
        return "FILM E SERIE"
    if name in DOC_SCIENCE:
        return "DOCUMENTARI E SCIENZA"
    if name in ANIME_EXISTING:
        return "ANIME"
    if name in MOTOR_EXISTING:
        return "MOTORSPORT"
    return "TV ITALIANA"

def with_group(block, group):
    first, delim, title = block[0].partition(",")
    first = re.sub(r'\s+group-title="[^"]*"', "", first)
    return [f'{first} group-title="{group}"{delim}{title}', *block[1:]]

def added_channel(group, no, name, url):
    return [
        f'#EXTINF:-1 tvg-chno="{no}" tvg-name="{name}" group-title="{group}",{name}',
        url
    ]

def exclusions():
    file = ROOT / "canali_da_escludere.txt"
    if not file.exists():
        return set()
    return {
        line.strip().casefold()
        for line in file.read_text(encoding="utf-8-sig").splitlines()
        if line.strip() and not line.lstrip().startswith("#")
    }

def main():
    raw = download(SOURCE)
    header, base = split_channels(raw)
    if len(base) < 25:
        raise RuntimeError("Fonte OpenIPTVItaly troppo corta: playlist precedente conservata")
    excluded = exclusions()
    categories = defaultdict(list)
    skipped = []
    def store(block, group):
        name = channel_name(block)
        match = re.search(r'tvg-chno="([^"]+)"', block[0])
        num = match.group(1) if match else ""
        if name.casefold() in excluded or num.casefold() in excluded:
            skipped.append(name)
            return
        categories[group].append(with_group(block, group))

    for block in base:
        name = channel_name(block)
        store(block, category(name))
    for n, (name, url) in enumerate(RADIOS, start=901):
        store(added_channel("RADIO ROCK", n, name, url), "RADIO ROCK")
    store(added_channel("ROCK TV", 952, *ROCK_ROMANIA), "ROCK TV")
    for group, no, name, url in EXTRA_CHANNELS:
        store(added_channel(group, no, name, url), group)

    lines = [header, ""]
    for group in CATEGORY_ORDER:
        for block in categories[group]:
            lines.extend(block)
            lines.append("")
    content = "\n".join(lines).rstrip() + "\n"
    if content.count("#EXTINF:") < 40:
        raise RuntimeError("Risultato sospetto: playlist precedente conservata")
    license_text = download(LICENSE)
    (ROOT / "playlist-rock-tv.m3u").write_text(content, encoding="utf-8")
    (ROOT / "LICENSE_OPENIPTVITALY.txt").write_text(license_text, encoding="utf-8")
    print("Totale:", content.count("#EXTINF:"), "Esclusi:", len(skipped))
    for group in CATEGORY_ORDER:
        print(f"{group}: {len(categories[group])}")

if __name__ == "__main__":
    main()

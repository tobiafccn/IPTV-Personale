#!/usr/bin/env python3
"""Genera RockTV-Personale: LCN italiano, gruppi extra e esclusioni persistenti."""
from pathlib import Path
from urllib.request import Request, urlopen
from collections import defaultdict
import re

ROOT = Path(__file__).resolve().parent
SOURCE = "https://raw.githubusercontent.com/xN1ckuz/OpenIPTVItaly/main/OpenIPTVItaly.m3u"
LICENSE = "https://raw.githubusercontent.com/xN1ckuz/OpenIPTVItaly/main/LICENSE"
CATEGORY_ORDER = ("DIGITALE TERRESTRE", "TV ITALIANA EXTRA", "NEWS E INFORMAZIONE", "DOCUMENTARI E SCIENZA", "ANIME", "WRESTLING E MMA", "MOTORSPORT", "ROCK TV", "RADIO ROCK",)
# Si mantengono soltanto i canali della fonte già approvati, senza importare
# automaticamente nuove emittenti o ripristinare canali eliminati.
APPROVED_SOURCE_NAMES = frozenset(("Rai 1", "Rai 2", "Rai 3", "Rete 4 HD", "Canale 5 HD", "Italia 1 HD", "LA7 HD", "TV8 HD", "NOVE HD", "TG Norba 24", "TV2000", "Real Time HD", "QVC HD", "Food Network HD", "RTL 102.5", "Boing HD", "K2", "Rai Gulp", "Rai Yoyo", "Frisbee", "Boing Plus", "Cartoonito HD", "Super!", "Rai News 24", "Sky TG24", "TGCOM 24 HD", "Italia 53", "HGTV - Home&Garden", "Italiana", "Rai Sport", "Sportitalia HD", "Canale 63", "Alma TV", "Radio 105 TV", "R101 TV", "Deejay TV HD", "RadioItaliaTV", "Rai 4K", "FIFA+", "Radio Kiss Kiss TV", "Rai Radio 2 Visual", "Radio 24 - IlSole24OreTV", "Gambero Rosso", "RadioFreccia", "Virgin Radio", "RDS Social TV", "Radio Zeta", "Euronews IT", "Hell's Kitchen Italy", "RaiPlay Sport 1", "Radio Carina TV", "Trace Urban", "Trace Latina", "Radio Capital TV", "M2O TV", "20Mediaset HD", "Rai 4", "Iris HD", "Rai Movie", "Rai Premium", "Cielo HD", "27Twentyseven HD", "LA7 Cinema", "La5 HD", "Cine34 HD", "Giallo", "Top Crime HD", "Italia 2 HD", "Mediaset Extra HD", "Rai 5", "FOCUS HD", "Discovery", "DMAX", "Rai Storia HD", "Discovery Turbo", "BBC Top Gear Italy", "MAN-GA", "ACI Sport TV HD", "Rally.TV FAST+",))
SPECIAL_GROUPS = {
    "Euronews IT": "NEWS E INFORMAZIONE",
    "DW English": "NEWS E INFORMAZIONE",
    "France 24 English": "NEWS E INFORMAZIONE",
    "Al Jazeera International": "NEWS E INFORMAZIONE",
    "CNN International": "NEWS E INFORMAZIONE",
    "Bloomberg": "NEWS E INFORMAZIONE",
    "Class CNBC": "NEWS E INFORMAZIONE",
    "BBC Top Gear Italy": "DOCUMENTARI E SCIENZA",
    "Documentary+": "DOCUMENTARI E SCIENZA",
    "NHK World-Japan (English)": "DOCUMENTARI E SCIENZA",
    "MAN-GA": "ANIME",
    "Pluto TV Anime (sperimentale)": "ANIME",
    "PFL MMA (sperimentale)": "WRESTLING E MMA",
    "TNA Wrestling (sperimentale)": "WRESTLING E MMA",
    "ACI Sport TV HD": "MOTORSPORT",
    "Rally.TV FAST+": "MOTORSPORT",
    "Red Bull TV": "MOTORSPORT",
    "Motorvision+ (English)": "MOTORSPORT",
    "Rai Scuola": "TV ITALIANA EXTRA",
    "Rock TV (Romania)": "ROCK TV",
    "XITE Rock x Metal": "ROCK TV",
    "XITE Rock On - stream alternativo (sperimentale)": "ROCK TV",
    "Vevo Rock (sperimentale)": "ROCK TV",
    "Vevo 2K (sperimentale)": "ROCK TV",
    "Metaleitor TV - alternativa Metal TV Core (sperimentale)": "ROCK TV",
    "181.FM - Rock 181": "RADIO ROCK",
    "ROCK ANTENNE - Modern Rock": "RADIO ROCK",
    "ROCK ANTENNE - Modern Metal": "RADIO ROCK",
    "ROCK ANTENNE - Hard Rock": "RADIO ROCK",
    "ROCK ANTENNE - Alternative": "RADIO ROCK",
    "TheBlast.FM - Christian Rock (verificare)": "RADIO ROCK",
}
ORDER_WITHIN_GROUP = {
    "DIGITALE TERRESTRE": (,),
    "TV ITALIANA EXTRA": (,),
    "NEWS E INFORMAZIONE": ("Euronews IT", "DW English", "France 24 English", "Al Jazeera International", "CNN International", "Bloomberg", "Class CNBC",),
    "DOCUMENTARI E SCIENZA": ("BBC Top Gear Italy", "Documentary+", "NHK World-Japan (English)",),
    "ANIME": ("MAN-GA", "Pluto TV Anime (sperimentale)",),
    "WRESTLING E MMA": ("PFL MMA (sperimentale)", "TNA Wrestling (sperimentale)",),
    "MOTORSPORT": ("ACI Sport TV HD", "Rally.TV FAST+", "Red Bull TV", "Motorvision+ (English)",),
    "ROCK TV": ("Rock TV (Romania)", "XITE Rock x Metal", "XITE Rock On - stream alternativo (sperimentale)", "Vevo Rock (sperimentale)", "Vevo 2K (sperimentale)", "Metaleitor TV - alternativa Metal TV Core (sperimentale)",),
    "RADIO ROCK": ("181.FM - Rock 181", "ROCK ANTENNE - Modern Rock", "ROCK ANTENNE - Modern Metal", "ROCK ANTENNE - Hard Rock", "ROCK ANTENNE - Alternative", "TheBlast.FM - Christian Rock (verificare)",),
}
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
    ("ROCK TV", 964, "Metaleitor TV - alternativa Metal TV Core (sperimentale)", "https://vs20.live.opencaster.com/metaleitortv_423d3342/index.m3u8"),
    ("TV ITALIANA", 1010, "Al Jazeera International", "https://live-hls-apps-aje-fa.getaj.net/AJE/index.m3u8"),
    ("TV ITALIANA", 1011, "Bloomberg", "https://bloomberg.com/media-manifest/streams/us.m3u8"),
    ("TV ITALIANA", 1012, "Class CNBC", "https://amg14891-amg14891c5-amgplt0020.playout.now3.amagi.tv/playlist.m3u8"),
    ("TV ITALIANA", 1013, "CNN International", "https://d3bp6dwmpbdajl.cloudfront.net/v1/master/3722c60a815c199d9c0ef36c5b73da68a62b09d1/cc-ury0meh5m4nzm/index.m3u8"),
    ("DOCUMENTARI E SCIENZA", 1014, "Rai Scuola", "https://mediapolis.rai.it/relinker/relinkerServlet.htm?cont=747011"),
)

def download(url):
    request = Request(url, headers={"User-Agent": "RockTV-Personale/1.0"})
    with urlopen(request, timeout=45) as response:
        return response.read().decode("utf-8-sig").replace("\r\n", "\n")

def split_channels(text):
    lines = text.splitlines()
    if not lines or not lines[0].startswith("#EXTM3U"):
        raise ValueError("Manca la intestazione M3U")
    blocks, current = [], None
    for line in lines[1:]:
        if line.startswith("#EXTINF:"):
            if current is not None:
                blocks.append(current)
            current = [line]
        elif current is not None:
            current.append(line)
    if current is not None:
        blocks.append(current)
    return lines[0], blocks

def channel_name(block):
    return block[0].split(",", 1)[-1].strip()

def number_from(block):
    match = re.search(r'tvg-chno="([^"]+)"', block[0])
    return int(match.group(1)) if match and match.group(1).isdigit() else None

def with_group_number(block, group, number):
    first, separator, name = block[0].partition(",")
    first = re.sub(r'\s+group-title="[^"]*"', "", first)
    if re.search(r'tvg-chno="[^"]*"', first):
        first = re.sub(r'tvg-chno="[^"]*"', f'tvg-chno="{number}"', first)
    else:
        first += f' tvg-chno="{number}"'
    return [f'{first} group-title="{group}"{separator}{name}', *block[1:]]

def added_channel(group, old_number, name, url):
    return [
        f'#EXTINF:-1 tvg-chno="{old_number}" tvg-name="{name}" group-title="{group}",{name}',
        url,
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

def choose_group(name, original_number):
    if original_number is not None and 1 <= original_number <= 70:
        return "DIGITALE TERRESTRE"
    return SPECIAL_GROUPS.get(name, "TV ITALIANA EXTRA")

def sort_key(group, block):
    name = channel_name(block)
    if group in ("DIGITALE TERRESTRE", "TV ITALIANA EXTRA"):
        num = number_from(block)
        return (num if num is not None else 9999, name.casefold())
    priority = ORDER_WITHIN_GROUP.get(group, ())
    return (priority.index(name) if name in priority else 9999, name.casefold())

def main():
    header, base = split_channels(download(SOURCE))
    if len(base) < 25:
        raise RuntimeError("Fonte OpenIPTVItaly incompleta: playlist precedente conservata")

    excluded = exclusions()
    categories = defaultdict(list)
    found_source = set()
    excluded_names = []

    def store(block, group):
        name = channel_name(block)
        orig_number = number_from(block)
        if name.casefold() in excluded or (orig_number is not None and str(orig_number) in excluded):
            excluded_names.append(name)
            return
        categories[group].append(block)

    for block in base:
        name = channel_name(block)
        if name not in APPROVED_SOURCE_NAMES:
            continue
        found_source.add(name)
        store(block, choose_group(name, number_from(block)))

    # Non pubblicare aggiornamenti parziali se la fonte perde canali approvati.
    required_names = {name for name in APPROVED_SOURCE_NAMES if name.casefold() not in excluded}
    missing = required_names - found_source
    if missing:
        raise RuntimeError(f"Mancano {len(missing)} canali approvati nella fonte: {sorted(missing)}")

    for n, (name, url) in enumerate(RADIOS, start=901):
        store(added_channel("RADIO ROCK", n, name, url), "RADIO ROCK")
    store(added_channel("ROCK TV", 952, *ROCK_ROMANIA), "ROCK TV")
    for group, number, name, url in EXTRA_CHANNELS:
        store(added_channel(group, number, name, url), choose_group(name, number))

    lines = [header, ""]
    next_extra_number = 101
    all_names = set()
    for group in CATEGORY_ORDER:
        for block in sorted(categories[group], key=lambda b: sort_key(group, b)):
            name = channel_name(block)
            if name in all_names:
                raise RuntimeError(f"Canale duplicato: {name}")
            all_names.add(name)
            original_number = number_from(block)
            if group == "DIGITALE TERRESTRE":
                if original_number is None:
                    raise RuntimeError(f"Manca il numero DTT: {name}")
                number = original_number
            else:
                number = next_extra_number
                next_extra_number += 1
            lines.extend(with_group_number(block, group, number))
            lines.append("")

    playlist = "\n".join(lines).rstrip() + "\n"
    if len(all_names) < 70 or not playlist.startswith("#EXTM3U"):
        raise RuntimeError("Risultato sospetto: playlist precedente conservata")
    license_text = download(LICENSE)
    (ROOT / "playlist-rock-tv.m3u").write_text(playlist, encoding="utf-8")
    (ROOT / "LICENSE_OPENIPTVITALY.txt").write_text(license_text, encoding="utf-8")
    print(f"Totale: {len(all_names)}; esclusi: {len(excluded_names)}")
    for group in CATEGORY_ORDER:
        print(f"{group}: {len(categories[group])}")

if __name__ == "__main__":
    main()

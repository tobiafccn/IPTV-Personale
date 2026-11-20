#!/usr/bin/env python3
"""Unisce la playlist pubblica OpenIPTVItaly con un gruppo di radio rock."""
from pathlib import Path
from urllib.request import Request, urlopen

SOURCE = "https://raw.githubusercontent.com/xN1ckuz/OpenIPTVItaly/main/OpenIPTVItaly.m3u"
LICENSE = "https://raw.githubusercontent.com/xN1ckuz/OpenIPTVItaly/main/LICENSE"
ROOT = Path(__file__).resolve().parent

# I collegamenti delle emittenti possono cambiare nel tempo.
RADIOS = [
    ("181.FM - Rock 181", "https://listen.181fm.com/181-rock_128k.mp3"),
    ("ROCK ANTENNE - Modern Rock", "https://stream.rockantenne.de/modern-rock/stream/mp3"),
    ("ROCK ANTENNE - Modern Metal", "https://stream.rockantenne.de/modern-metal/stream/mp3"),
    ("ROCK ANTENNE - Hard Rock", "https://stream.rockantenne.de/rock-antenne-hard-rock/stream/mp3"),
    ("ROCK ANTENNE - Alternative", "https://stream.rockantenne.de/alternative/stream/mp3"),
    # Il collegamento diretto di TheBlast.FM non e' stato verificato su TiViMate.
    ("TheBlast.FM - Christian Rock (verificare)", "https://mediacp.theblast.fm/stream/theblast"),
]

def read_url(url):
    request = Request(url, headers={"User-Agent": "RockTV-Personale/1.0"})
    with urlopen(request, timeout=45) as response:
        return response.read().decode("utf-8-sig").replace("\r\n", "\n")

def main():
    original = read_url(SOURCE).strip()
    count = original.count("#EXTINF:")
    if not original.startswith("#EXTM3U") or count < 25:
        raise RuntimeError("La fonte OpenIPTVItaly non e' una playlist valida. File precedente conservato.")
    lines = [original, ""]
    for i, (name, url) in enumerate(RADIOS, start=901):
        lines.extend([
            f'#EXTINF:-1 tvg-chno="{i}" tvg-name="{name}" group-title="RADIO ROCK",{name}',
            url,
        ])
    # Scarica la licenza prima di scrivere, evitando file parziali in caso di errore.
    license_text = read_url(LICENSE)
    (ROOT / "playlist-rock-tv.m3u").write_text("\n".join(lines) + "\n", encoding="utf-8")
    (ROOT / "LICENSE_OPENIPTVITALY.txt").write_text(license_text, encoding="utf-8")
    print(f"Creati {count} canali TV + {len(RADIOS)} radio rock.")

if __name__ == "__main__":
    main()

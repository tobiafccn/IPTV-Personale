# RockTV-Personale — TV italiana, radio rock e ROCK TV

Playlist M3U unica per TiViMate con i canali pubblici [OpenIPTVItaly](https://github.com/xN1ckuz/OpenIPTVItaly), sei radio audio e tre canali video musicali.

## URL da inserire in TiViMate

```text
https://raw.githubusercontent.com/tobiafccn/RockTV-Personale/main/playlist-rock-tv.m3u
```

**Non devi cambiare indirizzo in TiViMate quando aggiorniamo la playlist.** Basta aggiornare la playlist in TiViMate, o attendere il normale aggiornamento configurato.

### Gruppo RADIO ROCK — solo audio

- 181.FM - Rock 181
- ROCK ANTENNE - Modern Rock
- ROCK ANTENNE - Modern Metal
- ROCK ANTENNE - Hard Rock
- ROCK ANTENNE - Alternative
- TheBlast.FM - Christian Rock (collegamento ancora da verificare)

### Gruppo ROCK TV — canali con video

- RadioU TV (USA) — alternative rock / Christian rock e altri generi
- Rock TV (Romania) — rock
- Muzzik Rock&Roll (Serbia - da provare) — rock classico e moderno

Sono flussi video HLS (`.m3u8`) riportati in elenchi di emittenti pubblicamente accessibili. **La riproduzione su TiViMate non è ancora verificata.** Muzzik ha avuto segnalazioni di interruzioni del flusso; se non funziona, verrà sostituito o rimosso. L'offerta dei singoli canali può essere diversa dai tuoi gruppi preferiti.

## Nascondere canali che non interessano

Modifica [canali_da_escludere.txt](canali_da_escludere.txt), inserendo su ogni riga **il nome esatto del canale** oppure il numero `tvg-chno`, senza `#` davanti. Gli esempi già nel file iniziano con `#` e non tolgono nulla finché non li attivi.

Il generatore esclude i canali indicati **anche durante gli aggiornamenti successivi**, senza cancellarli dalla fonte originale OpenIPTVItaly. Le esclusioni valgono per tutti i gruppi, anche radio e video. I numeri dei canali rimasti non vengono rinumerati.

Dopo la modifica, avvia **Actions → Aggiorna canali TV e radio rock → Run workflow**. Poi aggiorna la playlist in TiViMate.

## Aggiornamenti

Il file `build_playlist.py` scarica OpenIPTVItaly, conserva la sua EPG, aggiunge le radio e i canali video, applica le esclusioni e aggiorna `playlist-rock-tv.m3u`.

Il workflow `.github/workflows/aggiorna.yml` si avvia ogni giorno alle 04:17 UTC e manualmente da GitHub Actions, se le autorizzazioni delle Actions lo permettono.

## Crediti

La fonte TV è [xN1ckuz/OpenIPTVItaly](https://github.com/xN1ckuz/OpenIPTVItaly); la relativa licenza MIT è disponibile in [LICENSE_OPENIPTVITALY.txt](LICENSE_OPENIPTVITALY.txt). I flussi audio/video restano sotto il controllo delle rispettive emittenti. Nessun contenuto viene ospitato in questo repository.

# RockTV-Personale — playlist TV personalizzata

**URL M3U invariato per TiViMate**

```text
https://raw.githubusercontent.com/tobiafccn/RockTV-Personale/main/playlist-rock-tv.m3u
```

## Ordine ispirato al digitale terrestre

La playlist rispetta l'ordine dei canali approvato il 20/11/2026. I canali della sezione iniziale sono numerati secondo l'LCN della fonte OpenIPTVItaly (da 1 a 70, con i numeri mancanti lasciati vuoti); gli altri canali sono numerati senza interruzioni da 101 a 180.

| Gruppo | Canali | Numerazione |
|---|---:|---|
| DIGITALE TERRESTRE | 57 | LCN 1–70 |
| TV ITALIANA EXTRA | 17 | 101–117 |
| FILM E SERIE | 8 | 118–125 |
| NEWS E INFORMAZIONE | 7 | 126–132 |
| DOCUMENTARI E SCIENZA | 25 | 133–157 |
| ANIME | 3 | 158–160 |
| WRESTLING E MMA | 2 | 161–162 |
| MOTORSPORT | 4 | 163–166 |
| ROCK TV | 8 | 167–174 |
| RADIO ROCK | 6 | 175–180 |

**Totale: 137 canali.** I numeri 71–100 sono lasciati liberi per distinguere i canali dell'antenna da quelli extra.

Le posizioni di Rai 1, Rai 2, Rai 3, Rete 4, Canale 5, Italia 1, LA7, TV8, NOVE e degli altri canali italiani principali non sono state modificate. Le reti già eliminate rimangono escluse.

## Aggiornamenti automatici

Il programma `build_playlist.py` ricrea la playlist ogni giorno usando i collegamenti aggiornati dalla fonte OpenIPTVItaly, **importando solo i canali già approvati**. Gli altri canali non vengono aggiunti automaticamente. Continua ad applicare tutte le righe del file `canali_da_escludere.txt`, senza ripristinare canali rimossi.

Il workflow `.github/workflows/aggiorna.yml` può essere avviato anche manualmente dalla scheda **Actions**. Se la sorgente non contiene uno dei canali approvati, la generazione fallisce senza sostituire la playlist precedentemente funzionante.

**Nota TiViMate Free:** se `Aggiorna playlist` è bloccato, rimuovi e reinserisci la stessa playlist M3U. Eliminare una playlist può cancellare i preferiti locali.

## Flussi sperimentali

Alcuni stream XITE, Vevo, Pluto TV e altri possono dipendere dalla regione o non essere compatibili con TiViMate. Il contenuto non viene ospitato dal repository. Le prove sulla Fire TV Stick rimangono necessarie.

## Fonte e licenza

La fonte TV italiana è [xN1ckuz/OpenIPTVItaly](https://github.com/xN1ckuz/OpenIPTVItaly), con licenza MIT conservata nel file `LICENSE_OPENIPTVITALY.txt`. Il file `canali_richiesti_stato.md` documenta le richieste precedenti e i limiti dei relativi flussi.

## Nuovi canali sperimentali — 20 novembre 2026

Sono stati aggiunti **6 nuovi flussi video M3U8**, mantenendo tutti i 105 canali precedenti e le esclusioni esistenti. Le nuove stazioni sono indicate come *sperimentali* perché il loro funzionamento effettivo su Fire TV Stick/TiViMate in Italia non è stato provato:

- **FilmRise Sci-Fi (sperimentale)** — FILM E SERIE
- **Alien Nation by DUST (sperimentale)** — FILM E SERIE
- **NASA TV Media (sperimentale)** — DOCUMENTARI E SCIENZA
- **WildEarth (sperimentale)** — DOCUMENTARI E SCIENZA
- **RetroCrush (sperimentale)** — ANIME
- **Metal.Rocks (sperimentale)** — ROCK TV

**BSB TV+** non è stato aggiunto: l'emittente pubblica un lettore Web Viloud ma non un URL diretto M3U8 riconosciuto e riutilizzabile in TiViMate. Per guardarlo usa [il sito ufficiale](https://bloodsweatandbeers.tv/tv/).

Il nuovo gruppo **FILM E SERIE** è stato inserito fra TV ITALIANA EXTRA e NEWS E INFORMAZIONE. La sezione DIGITALE TERRESTRE resta nell'ordine LCN; le sezioni extra vengono numerate consecutivamente da 101 a 167. I numeri possono variare se vengono aggiunti altri canali.

## Aggiunte del 20 novembre 2026 — Pluto TV Italia e Rakuten TV Italia

Sono state aggiunte altre **13 emittenti sperimentali**, preservando i 111 canali precedenti e tutte le 48 esclusioni. I collegamenti sono stati recuperati dagli elenchi pubblici `iptv-org/iptv` per i cataloghi italiani `streams/it_pluto.m3u` e `streams/it_rakuten.m3u`. I flussi non sono ancora stati collaudati su Amazon Fire TV Stick, possono cambiare o dipendere dal Paese.

- **Pluto TV Sci-Fi (Italia - sperimentale)** — gruppo FILM E SERIE
- **Pluto TV Serie Sci-Fi (Italia - sperimentale)** — gruppo FILM E SERIE
- **Pluto TV Film Azione (Italia - sperimentale)** — gruppo FILM E SERIE
- **Pluto TV Film Thriller (Italia - sperimentale)** — gruppo FILM E SERIE
- **Pluto TV Horror (Italia - sperimentale)** — gruppo FILM E SERIE
- **Rakuten TV Sci-Fi (Italia - sperimentale)** — gruppo FILM E SERIE
- **Rakuten TV Action Movies (Italia - sperimentale)** — gruppo FILM E SERIE
- **Pluto TV Documentari (Italia - sperimentale)** — gruppo DOCUMENTARI E SCIENZA
- **Pluto TV Natura (Italia - sperimentale)** — gruppo DOCUMENTARI E SCIENZA
- **Pluto TV Storia (Italia - sperimentale)** — gruppo DOCUMENTARI E SCIENZA
- **Space Live (sperimentale)** — gruppo DOCUMENTARI E SCIENZA
- **Pluto TV Anime Italia (sperimentale)** — gruppo ANIME
- **That's Rock (Italia - sperimentale)** — gruppo ROCK TV

**Pluto TV Anime Italia** è un'alternativa di prova e non sostituisce ancora la variante americana presente in playlist. La lingua italiana è prevista per i canali italiani di film e documentari, ma andrà verificata su TiViMate.

## Ultime quattro aggiunte approvate — 20 novembre 2026

Aggiunte finali della selezione, senza nuovi canali anime:

- **Pluto TV Serie Crime (Italia - sperimentale)** — gruppo `FILM E SERIE`
- **Pluto TV Film Commedia (Italia - sperimentale)** — gruppo `FILM E SERIE`
- **Pluto TV Paranormal (Italia - sperimentale)** — gruppo `DOCUMENTARI E SCIENZA`
- **Pluto TV True Crime (Italia - sperimentale)** — gruppo `DOCUMENTARI E SCIENZA`

I quattro nuovi flussi provengono dalla raccolta pubblica `iptv-org/iptv` (`streams/it_pluto.m3u`) e saranno collaudati insieme agli altri flussi sperimentali su TiViMate Free dopo la conclusione della selezione. Le esclusioni precedenti rimangono attive. Per il momento non sono previste ulteriori aggiunte.

## Rimozioni dopo il test su Fire TV — 20 novembre 2026

Questi sei canali non venivano riprodotti in TiViMate e sono stati eliminati senza cercare collegamenti alternativi:

- Rai Scuola (posizione precedente 75)
- Alien Nation by DUST (sperimentale) (posizione precedente 77)
- Rakuten TV Sci-Fi (Italia - sperimentale) (posizione precedente 83)
- Rakuten TV Action Movies (Italia - sperimentale) (posizione precedente 84)
- NASA TV Media (sperimentale) (posizione precedente 97)
- RetroCrush (sperimentale) (posizione precedente 107)

I sei nomi sono stati aggiunti alle esclusioni permanenti. **Boing Plus** (precedente posizione 36) non è stato rimosso in questa operazione. Le integrazioni dei loghi saranno affrontate separatamente.

## Loghi dei canali — 20 novembre 2026

Aggiunti **43 campi `tvg-logo`** ai canali che ne erano privi; tutte le **122 voci** della playlist ora contengono un riferimento a un'immagine. Il generatore automatico è stato aggiornato per mantenere gli stessi loghi. **I collegamenti di streaming, l'ordine e la numerazione non sono cambiati.**

Fonti: immagini dei canali Pluto TV, directory pubbliche di loghi e siti dei broadcaster. Per alcuni marchi si usano i loro favicon. La presenza dell'URL non garantisce che TiViMate Free riesca a caricare ogni immagine: occorre un riscontro sulla Fire TV Stick dopo il nuovo caricamento della playlist.

## Guida programmi EPG unificata

Per risolvere la dicitura **«Nessuna informazione»** sui canali FAST, è stato preparato \`build_epg.py\` per creare una guida XMLTV compressa \`epg-rock-tv.xml.gz\` dai dati EPGShare Italia e Pluto TV Italia, con Pluto TV USA come fonte aggiuntiva facoltativa. La guida conserva gli ID esistenti delle reti nazionali, usa gli ID originali dei canali Pluto e cerca abbinamenti esatti per alcune reti aggiuntive. Quando la generazione termina correttamente, l'intestazione della M3U punta automaticamente a un'unica guida: \`https://raw.githubusercontent.com/tobiafccn/RockTV-Personale/main/epg-rock-tv.xml.gz\`.

**Limiti:** per emittenti che non forniscono una programmazione pubblica compatibile potrà ancora comparire «Nessuna informazione». Il processo non crea titoli di trasmissioni immaginari. Se una fonte obbligatoria manca o il risultato è anomalo, la pubblicazione viene bloccata per non sovrascrivere la guida precedente. Non sono stati modificati gli stream, i loghi o la numerazione. La prima generazione GitHub Actions deve essere completata e verificata prima di considerare la guida operativa.

## Nuove dirette Terra e safari — 22 novembre 2026

Aggiunte 3 sorgenti HLS sperimentali per l'osservazione della Terra dalla ISS e 4 webcam Africam della fauna africana:

- **Africam - Elephant Park (sperimentale)**: https://outbound-production.explore.org/stream-production-110/.m3u8
- **Africam - Tau Waterhole (sperimentale)**: https://outbound-production.explore.org/stream-production-317/.m3u8
- **Africam - Rosies Pan (sperimentale)**: https://outbound-production.explore.org/stream-production-108/.m3u8
- **Africam - Safari Cam 4 (sperimentale)**: https://outbound-production.explore.org/stream-production-49/.m3u8
- **Sen SpaceTV-1 - viste ISS (sperimentale)**: https://linear-1224.frequency.stream/dist/lg-uk/1224/hls/master/playlist.m3u8
- **NASA ISS - Terra in diretta (relay sperimentale)**: https://hls.youtb.workers.dev/video/0P41gTF-Nl4.m3u8
- **Space Live by Sen - stream alternativo (sperimentale)**: https://d111bsx9oooqoh.cloudfront.net/playlist.m3u8

Le due sorgenti **Sen / Space Live** possono trasmettere gli stessi contenuti; la vista verso il basso (*nadir*) non è garantita in ogni momento. Il canale NASA usa un **relay HLS di terzi per un video YouTube NASA** e può smettere di funzionare. I quattro flussi Africam/Explore.org provengono da playlist pubbliche e devono essere verificati su TiViMate; una webcam live può non mostrare sempre animali. Tutti e sette i flussi sono **sperimentali e non collaudati sulla Fire TV**. La playlist continua a conservare tutti i 122 stream precedenti, 54 esclusioni, i loghi e i numeri LCN originali; il generatore automatico manterrà le aggiunte.

## Webcam marine e animali di Explore.org — 22 novembre 2026

Aggiunti **8 nuovi flussi HLS sperimentali**: sei osservazioni marine (barriera corallina, squali, kelp forest, pinguini, orche e lamantini) e due birdcam (aquile e colibrì).

- **Explore - Barriera corallina (sperimentale)** — https://outbound-production.explore.org/stream-production-10/.m3u8
- **Explore - Squali in acquario (sperimentale)** — https://outbound-production.explore.org/stream-production-12/.m3u8
- **Explore - Foresta di alghe (sperimentale)** — https://outbound-production.explore.org/stream-production-70/.m3u8
- **Explore - Pinguini sulla spiaggia (sperimentale)** — https://outbound-production.explore.org/stream-production-14/.m3u8
- **Explore - Orche OrcaLab (sperimentale)** — https://outbound-production.explore.org/stream-production-95/.m3u8
- **Explore - Lamantini sott'acqua (sperimentale)** — https://outbound-production.explore.org/stream-production-162/.m3u8
- **Explore - Aquile di Decorah (sperimentale)** — https://outbound-production.explore.org/stream-production-216/.m3u8
- **Explore - Colibri al mangiatoia (sperimentale)** — https://outbound-production.explore.org/stream-production-189/.m3u8

Ogni nuovo canale usa il logo del marchio Explore.org e possiede un identificativo tecnico. **Non è stata verificata la riproduzione sulla Fire TV**: i link provengono da playlist webcam pubbliche e possono essere offline o cambiati. Essendo webcam 24 ore su 24, non possiedono una normale scaletta oraria EPG; «Nessuna informazione» può essere normale. Restano invariati tutti i precedenti 129 indirizzi di streaming, i 54 canali esclusi e i loghi esistenti. Gli ID EPG tecnici sono stati rinumerati per evitare collisioni dopo gli inserimenti.

# RockTV-Personale — playlist TV personalizzata

**URL M3U invariato per TiViMate**

```text
https://raw.githubusercontent.com/tobiafccn/RockTV-Personale/main/playlist-rock-tv.m3u
```

## Ordine ispirato al digitale terrestre

La playlist rispetta l'ordine dei canali approvato il 20/11/2026. I canali della sezione iniziale sono numerati secondo l'LCN della fonte OpenIPTVItaly (da 1 a 70, con i numeri mancanti lasciati vuoti); gli altri canali sono numerati senza interruzioni da 101 a 178.

| Gruppo | Canali | Numerazione |
|---|---:|---|
| DIGITALE TERRESTRE | 57 | LCN 1–70 |
| TV ITALIANA EXTRA | 17 | 101–117 |
| FILM E SERIE | 8 | 118–125 |
| NEWS E INFORMAZIONE | 7 | 126–132 |
| DOCUMENTARI E SCIENZA | 17 | 133–149 |
| WEBCAM ANIMALI | 6 | 150–155 |
| ANIME | 3 | 156–158 |
| WRESTLING E MMA | 2 | 159–160 |
| MOTORSPORT | 4 | 161–164 |
| ROCK TV | 8 | 165–172 |
| RADIO ROCK | 6 | 173–178 |

**Totale: 135 canali.** I numeri 71–100 sono lasciati liberi per distinguere i canali dell'antenna da quelli extra.

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

## Rimozione webcam non funzionanti — 22 novembre 2026

In base alla prova pratica su TiViMate, sono stati eliminati **11 canali** senza tentare collegamenti alternativi. Le quattro Africam alle precedenti posizioni **94–97** non si riproducevano e non mostravano il logo. Le sette Explore alle posizioni **99–105** mostravano il logo ma rimanevano in caricamento senza mostrare immagini né segnalare errori.

- 94: Africam - Elephant Park (sperimentale)
- 95: Africam - Tau Waterhole (sperimentale)
- 96: Africam - Rosies Pan (sperimentale)
- 97: Africam - Safari Cam 4 (sperimentale)
- 99: Explore - Squali in acquario (sperimentale)
- 100: Explore - Foresta di alghe (sperimentale)
- 101: Explore - Pinguini sulla spiaggia (sperimentale)
- 102: Explore - Orche OrcaLab (sperimentale)
- 103: Explore - Lamantini sott'acqua (sperimentale)
- 104: Explore - Aquile di Decorah (sperimentale)
- 105: Explore - Colibri al mangiatoia (sperimentale)

**Explore - Barriera corallina**, precedente posizione **98**, non è stato eliminato perché non era incluso nella segnalazione. Le posizioni TiViMate si aggiornano dopo le rimozioni: non usare più i vecchi numeri. Le 11 voci sono state inserite in `canali_da_escludere.txt` e rimosse dal generatore. Rimangono i 126 canali approvati e tutti i loghi preesistenti; in assenza di EPG delle webcam può comparire «Nessuna informazione».

## Ulteriori due rimozioni — 22 novembre 2026

Rimosse **Explore - Barriera corallina (sperimentale)** (vecchia posizione 98 nella lista di 137 canali) e **NASA ISS - Terra in diretta (relay sperimentale)** (vecchia posizione 111 nella lista di 137 canali). Entrambi davano errore di riproduzione sulla Fire TV. Sono stati esclusi permanentemente senza tentativi di riparazione.

**Attenzione:** nella playlist a 126 voci la posizione 111 corrispondeva a Red Bull TV, che **non è stata rimossa**. Non sono stati alterati gli altri stream. Esclusioni attive: 67.

## Documentari naturalistici aggiunti — 22 novembre 2026

Aggiunti tre canali naturalistici FAST con i loghi Samsung TV Plus, identificativi EPG dei cataloghi ufficiali e flussi HLS raccolti pubblicamente:

- **NatureTime Italia (sperimentale)** — `IT2100001EZ` — https://amg01515-amg01515c47-samsung-it-9436.playouts.now.amagi.tv/ts-eu-w1-n2/playlist/amg01515-blueskyeentertainment-naturetimeemeaita-samsungit/playlist.m3u8
- **Earth Touch TV (English - sperimentale)** — `GBBD3200001E2` — https://amg01823-earthtouch-amg01823c1-samsung-gb-862.playouts.now.amagi.tv/playlist/amg01823-earthtouch-earthtouch-samsunggb/playlist.m3u8
- **Wild Planet (English - sperimentale)** — `GBBB5000002PL` — https://d1h8whhtg5u7om.cloudfront.net/WildPlanet_GB.m3u8

**NatureTime**: sorgente Samsung TV Plus Italia. **Earth Touch TV** e **Wild Planet**: sorgenti per Samsung TV Plus Regno Unito, in inglese, che potrebbero essere soggette a blocchi territoriali. Tutti e tre i flussi devono ancora essere verificati su TiViMate Fire TV. L'avere un tvg-id e un logo non garantisce che il player carichi la guida TV. Tutti i precedenti 124 stream e le 67 esclusioni restano invariati; il generatore applica gli ID dei broadcaster anche negli aggiornamenti futuri.

## Esito prova canali documentari — 22 novembre 2026

Prova Fire TV: **NatureTime Italia** (vecchia posizione 94) e **Wild Planet** (vecchia posizione 96) funzionano. **Earth Touch TV** (vecchia posizione 95) non funziona ed è stato rimosso da M3U, generatore e aggiunto alle esclusioni permanenti. Numero aggiornato dei canali: **126**; esclusioni permanenti: **68**. I due canali funzionanti sono stati conservati con lo stesso streaming, logo e identificativo EPG originale. Gli altri stream non sono cambiati. Dopo la rimozione, Wild Planet passa alla posizione 95 in TiViMate.

## Documentari globali e webcam animali — 22 novembre 2026

Sono stati aggiunti **7 canali**, di cui tre FAST di Samsung TV Plus Italia e quattro webcam live esterne. Le webcam sono in un gruppo dedicato **WEBCAM ANIMALI** per facilitarne la prova su TiViMate Free. Tutte le aggiunte sono sperimentali perché la riproduzione HLS non è stata verificata sulla Fire TV.

- **BBC Earth Italia (sperimentale)** (DOCUMENTARI E SCIENZA): https://amg00793-amg00793c23-samsung-it-4780.playouts.now.amagi.tv/playlist/amg00793-bbcstudios-bbcearthitaly-samsungit/playlist.m3u8
- **Love the Planet Italia (sperimentale)** (DOCUMENTARI E SCIENZA): https://cdn-ue1-prod.tsv2.amagi.tv/linear/amg01821-lovetvchannels-lovetheplanetitsamsung-samsungit/playlist.m3u8
- **Ocean Vibes Italia (sperimentale)** (DOCUMENTARI E SCIENZA): https://jmp2.uk/stvp-IT18000076Y
- **Webcam - Orsi polari San Diego Zoo (sperimentale)** (WEBCAM ANIMALI): https://polarplunge.hls.camzonecdn.com/CamzoneStreams/polarplunge/Playlist.m3u8
- **Webcam - Pinguini San Diego Zoo (sperimentale)** (WEBCAM ANIMALI): https://zssd-penguin.hls.camzonecdn.com/CamzoneStreams/zssd-penguin/Playlist.m3u8
- **Webcam - Panda gigante San Diego Zoo (sperimentale)** (WEBCAM ANIMALI): https://zssd-panda2024.hls.camzonecdn.com/CamzoneStreams/zssd-panda2024/Playlist.m3u8
- **Webcam - Elefanti marini California (sperimentale)** (WEBCAM ANIMALI): https://video.parks.ca.gov/Hearst/Piedras.stream/playlist.m3u8

BBC Earth e Love the Planet offrono documentari sulla natura e sugli ambienti terrestri/marini. Ocean Vibes è un canale ambient/relax con immagini del mare, **non** un programma naturalistico. Le webcam del San Diego Zoo mostrano animali **in cattività**, non riprese dei Poli o della fauna nel suo habitat naturale; la Polar Cam e la Penguin Cam trasmettono durante il giorno locale. La webcam degli elefanti marini riguarda una colonia **selvatica** a Piedras Blancas. Tutte queste webcam provengono da operatori differenti da Explore.org, ma le URL HLS pubbliche possono cessare di funzionare e non sono state collaudate su TiViMate. Le webcam 24/7 non hanno un palinsesto orario reale: la guida può restare «Nessuna informazione». I 126 stream precedenti e le 68 esclusioni rimangono intatti. I tre ID EPG Samsung sono registrati nel generatore, ma l'abbinamento EPG effettivo dipende dalla guida importata dal player.

## Nuove webcam di fauna libera — 22 novembre 2026

Aggiunti **due flussi HLS sperimentali** alla categoria **WEBCAM ANIMALI**. Questa aggiunta dà priorità a fauna *libera* rispetto a esemplari ospitati in zoo:

- **Webcam - Leoni marini selvatici Oregon (sperimentale)** — https://s74.ipcamlive.com/streams/4ahhtgcizabw1oewq/stream.m3u8
- **Webcam - Uccelli selvatici WildlifeKate UK (sperimentale)** — https://stream.wildlifestreaming.io:8443/WildlifeKate/13.stream_aac/playlist.m3u8

La webcam **Newport Sea Lion Docks** osserva leoni marini selvatici nella baia di Yaquina, Oregon, che usano pontili galleggianti; perciò non è un habitat completamente privo di strutture umane. La webcam **WildlifeKate UK** riprende uccelli selvatici attirati da mangiatoie all'aperto nel Regno Unito. I due stream sono stati reperiti in playlist pubbliche ma **non collaudati su Fire TV o TiViMate**; l'accesso potrebbe dipendere da disponibilità e restrizioni dell'operatore. Nessun programma EPG con orari è garantito per queste webcam 24/7. Le quattro webcam dello zoo già approvate, WildEarth, NatureTime, Wild Planet e tutte le altre 133 voci preesistenti restano immutate. Le 68 esclusioni non cambiano. Per safari africani e animali polari liberi risultano dirette disponibili sui siti degli operatori, ma non sono stati trovati ulteriori HLS permanenti sufficientemente affidabili per inserirli ora.

## Esito test webcam Oregon e WildlifeKate — 22 novembre 2026

La webcam **leoni marini selvatici Oregon** (precedente posizione 111) non riproduceva immagini, restando in caricamento, quindi è stata eliminata dal generatore e aggiunta alle esclusioni permanenti (69 in totale). La webcam **uccelli selvatici WildlifeKate UK** (precedente posizione 112) è invece confermata funzionante, ma il logo favicon non veniva visualizzato. Lo streaming non è stato modificato; il logo è stato sostituito con un file PNG ufficiale del sito WildlifeKate (`WLKTransparentWHITE.png`, static.wixstatic.com). La nuova posizione dell'unica webcam WildlifeKate è **111**. La visualizzazione del nuovo logo sul dispositivo è da verificare. La playlist comprende **134 canali**.

## Webcam delfini — 22 novembre 2026

Aggiunta in **WEBCAM ANIMALI** una webcam sperimentale denominata **Webcam - Delfini Clearwater Marine Aquarium (sperimentale)**, basata su un collegamento HLS di Ozolio pubblicato in una playlist di terzi: https://use01-smr04-relay.ozolio.com/hls-live/_definst_/relay01.zemocxr.fd0.sm1.av2.mt0.at0.as0.dv0.sh2.rt20687.rc0.edge.basic.stream/playlist.m3u8

La struttura gestisce delfini recuperati e assistiti nelle Florida Keys/Florida; questa webcam è attribuita alla struttura da un elenco pubblico, ma **l'esatta corrispondenza tra il feed e la telecamera è da confermare con la prova in TiViMate**. Non va confusa con una webcam di delfini liberi in mare. Il collegamento non è stato collaudato sulla Fire TV e potrebbe essere offline o mostrare un contenuto diverso. Le webcam di orche selvatiche disponibili su Orca Conservancy e OrcaLab utilizzano prevalentemente YouTube o Explore.org; non è stato trovato un flusso M3U8 diretto verificato da aggiungere. La webcam delle **foche elefante selvatiche** a Piedras Blancas è già nella playlist come *Elefanti marini California*, e le webcam degli orsi polari e pinguini di San Diego erano già funzionanti. I 134 vecchi stream sono rimasti invariati, insieme alle 69 esclusioni.

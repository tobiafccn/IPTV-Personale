# RockTV-Personale — playlist TV personalizzata

**URL M3U invariato per TiViMate**

```text
https://raw.githubusercontent.com/tobiafccn/RockTV-Personale/main/playlist-rock-tv.m3u
```

## Ordine ispirato al digitale terrestre

La playlist rispetta l'ordine dei canali approvato il 20/11/2026. I canali della sezione iniziale sono numerati secondo l'LCN della fonte OpenIPTVItaly (da 1 a 70, con i numeri mancanti lasciati vuoti); gli altri canali sono numerati senza interruzioni da 101 a 154.

| Gruppo | Canali | Numerazione |
|---|---:|---|
| DIGITALE TERRESTRE | 57 | LCN 1–70 |
| TV ITALIANA EXTRA | 18 | 101–118 |
| FILM E SERIE | 2 | 119–120 |
| NEWS E INFORMAZIONE | 7 | 121–127 |
| DOCUMENTARI E SCIENZA | 5 | 128–132 |
| ANIME | 3 | 133–135 |
| WRESTLING E MMA | 2 | 136–137 |
| MOTORSPORT | 4 | 138–141 |
| ROCK TV | 7 | 142–148 |
| RADIO ROCK | 6 | 149–154 |

**Totale: 111 canali.** I numeri 71–100 sono lasciati liberi per distinguere i canali dell'antenna da quelli extra.

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

Il nuovo gruppo **FILM E SERIE** è stato inserito fra TV ITALIANA EXTRA e NEWS E INFORMAZIONE. La sezione DIGITALE TERRESTRE resta nell'ordine LCN; le sezioni extra vengono numerate consecutivamente da 101 a 154. I numeri possono variare se vengono aggiunti altri canali.

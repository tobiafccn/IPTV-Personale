# RockTV-Personale — playlist TV personalizzata

**URL M3U invariato per TiViMate**

```text
https://raw.githubusercontent.com/tobiafccn/RockTV-Personale/main/playlist-rock-tv.m3u
```

## Ordine ispirato al digitale terrestre

La playlist rispetta l'ordine dei canali approvato il 20/11/2026. I canali della sezione iniziale sono numerati secondo l'LCN della fonte OpenIPTVItaly (da 1 a 70, con i numeri mancanti lasciati vuoti); gli altri canali sono numerati senza interruzioni da 101 a 148.

| Gruppo | Canali | Numerazione |
|---|---:|---|
| DIGITALE TERRESTRE | 57 | LCN 1–70 |
| TV ITALIANA EXTRA | 18 | 101–118 |
| NEWS E INFORMAZIONE | 7 | 119–125 |
| DOCUMENTARI E SCIENZA | 3 | 126–128 |
| ANIME | 2 | 129–130 |
| WRESTLING E MMA | 2 | 131–132 |
| MOTORSPORT | 4 | 133–136 |
| ROCK TV | 6 | 137–142 |
| RADIO ROCK | 6 | 143–148 |

**Totale: 105 canali.** I numeri 71–100 sono lasciati liberi per distinguere i canali dell'antenna da quelli extra.

Le posizioni di Rai 1, Rai 2, Rai 3, Rete 4, Canale 5, Italia 1, LA7, TV8, NOVE e degli altri canali italiani principali non sono state modificate. Le reti già eliminate rimangono escluse.

## Aggiornamenti automatici

Il programma `build_playlist.py` ricrea la playlist ogni giorno usando i collegamenti aggiornati dalla fonte OpenIPTVItaly, **importando solo i canali già approvati**. Gli altri canali non vengono aggiunti automaticamente. Continua ad applicare tutte le righe del file `canali_da_escludere.txt`, senza ripristinare canali rimossi.

Il workflow `.github/workflows/aggiorna.yml` può essere avviato anche manualmente dalla scheda **Actions**. Se la sorgente non contiene uno dei canali approvati, la generazione fallisce senza sostituire la playlist precedentemente funzionante.

**Nota TiViMate Free:** se `Aggiorna playlist` è bloccato, rimuovi e reinserisci la stessa playlist M3U. Eliminare una playlist può cancellare i preferiti locali.

## Flussi sperimentali

Alcuni stream XITE, Vevo, Pluto TV e altri possono dipendere dalla regione o non essere compatibili con TiViMate. Il contenuto non viene ospitato dal repository. Le prove sulla Fire TV Stick rimangono necessarie.

## Fonte e licenza

La fonte TV italiana è [xN1ckuz/OpenIPTVItaly](https://github.com/xN1ckuz/OpenIPTVItaly), con licenza MIT conservata nel file `LICENSE_OPENIPTVITALY.txt`. Il file `canali_richiesti_stato.md` documenta le richieste precedenti e i limiti dei relativi flussi.

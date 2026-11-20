# RockTV-Personale: TV italiana + radio rock

Una sola playlist M3U per TiViMate: i canali della lista [OpenIPTVItaly](https://github.com/xN1ckuz/OpenIPTVItaly) e sei emittenti dedicate al rock.

## Playlist pronta da copiare

```text
https://raw.githubusercontent.com/tobiafccn/RockTV-Personale/main/playlist-rock-tv.m3u
```

La categoria **RADIO ROCK** comprende:

- 181.FM - Rock 181
- ROCK ANTENNE - Modern Rock
- ROCK ANTENNE - Modern Metal
- ROCK ANTENNE - Hard Rock
- ROCK ANTENNE - Alternative
- TheBlast.FM - Christian Rock (collegamento diretto da verificare su TiViMate)

## Come usarla in TiViMate gratuito

1. In **Impostazioni → Playlist**, cerca la playlist esistente OpenIPTVItaly.
2. Se TiViMate consente di modificarne l'indirizzo, sostituiscilo con l'URL indicato sopra.
3. Se l'indirizzo non è modificabile, elimina la vecchia playlist e aggiungi questo URL come *unica playlist M3U*.
4. Aggiorna la playlist nell'app, quindi cerca il gruppo **RADIO ROCK**.

**Attenzione:** la rimozione della vecchia playlist potrebbe cancellare preferiti o impostazioni a essa associati. Conserva l'URL precedente finché non hai verificato che questa nuova lista funziona correttamente.

## Aggiornamenti automatici

GitHub Actions usa `.github/workflows/aggiorna.yml` per ricreare la playlist ogni giorno alle 04:17 UTC e quando si avvia manualmente **Actions → Aggiorna canali TV e radio rock → Run workflow**. Il generatore `build_playlist.py` scarica ogni volta la fonte OpenIPTVItaly, mantiene le righe originali (inclusa la guida EPG) e aggiunge le stazioni rock.

L'aggiornamento automatico richiede che GitHub Actions sia abilitato nel repository e che i workflow possano scrivere i contenuti. L'esecuzione iniziale **non** è necessaria: `playlist-rock-tv.m3u` è già pubblicata. Se l'aggiornamento automatico fallisce, rimane disponibile l'ultima playlist caricata.

I collegamenti radio dipendono dai rispettivi editori e possono cambiare; nessuno stream è stato collaudato su una TV reale. **TheBlast.FM** può richiedere un collegamento diverso se il flusso attuale non viene riprodotto.

## Crediti e licenza

L'elenco TV viene da [xN1ckuz/OpenIPTVItaly](https://github.com/xN1ckuz/OpenIPTVItaly). La sua licenza MIT è conservata nel file [LICENSE_OPENIPTVITALY.txt](LICENSE_OPENIPTVITALY.txt). Le stazioni radio appartengono ai rispettivi editori. Il progetto non è affiliato alle emittenti.

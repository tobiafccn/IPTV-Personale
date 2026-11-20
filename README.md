# RockTV-Personale — la playlist IPTV personalizzata

**Un unico URL M3U per TiViMate gratuito:**

```text
https://raw.githubusercontent.com/tobiafccn/RockTV-Personale/main/playlist-rock-tv.m3u
```

## Ordine dei gruppi

1. TV ITALIANA
2. FILM E SERIE
3. DOCUMENTARI E SCIENZA
4. ANIME
5. WRESTLING E MMA
6. MOTORSPORT
7. ROCK TV
8. RADIO ROCK

L'ordine relativo dei canali italiani all'interno di ogni gruppo viene conservato quanto più possibile; rimangono i numeri TV originali dove disponibili. Per ottenere i gruppi nell'ordine richiesto, alcuni canali già esistenti vengono ricollocati dal gruppo generale a quello tematico.

## Canali

- La fonte TV è la playlist pubblica OpenIPTVItaly; il file `canali_da_escludere.txt` contiene le esclusioni stabilite dal proprietario.
- Gruppo RADIO ROCK: sei stazioni audio.
- ROCK TV: Rock TV Romania, XITE Rock x Metal, XITE Rock On (link di prova alternativo), Vevo Rock, Vevo 2K e Metaleitor TV sperimentale.
- Documentari, notizie in inglese, anime, wrestling/MMA e motorsport: inseriti canali gratuiti pubblicamente elencati.

**Importante:** i flussi di Pluto TV (`jmp2.uk`) e altri canali FAST possono essere geobloccati, instabili o incompatibili con TiViMate. Il loro funzionamento effettivo su Fire TV Stick in Italia deve essere collaudato. XITE Rock On e Rock x Metal possono mostrare lo stesso programma: sono due indirizzi alternativi per la prova. Metaleitor TV è un'alternativa sperimentale a Metal TV Core: non è la stessa emittente; per Metal TV Core non è stato identificato un URL M3U8 riutilizzabile.

## Aggiornamento e personalizzazione

Il generatore `build_playlist.py` scarica i canali originali, applica i filtri, riordina i gruppi e aggiunge i flussi supplementari. L'automazione `.github/workflows/aggiorna.yml` esegue il programma giornalmente, se GitHub Actions è attivo; puoi anche avviarla manualmente. Le esclusioni sono permanenti e non verranno ripristinate da un aggiornamento ordinario.

In TiViMate gratuito, se `Aggiorna playlist` è bloccato, elimina e reinserisci l'unica playlist M3U usando l'URL sopra. Attenzione a eventuali preferiti e impostazioni collegati alla playlist precedente.

## Fonte, licenza e responsabilità

I canali italiani provengono da [xN1ckuz/OpenIPTVItaly](https://github.com/xN1ckuz/OpenIPTVItaly). La relativa licenza MIT è riportata in `LICENSE_OPENIPTVITALY.txt`. Alcuni flussi aggiuntivi sono indicizzati da [iptv-org/iptv](https://github.com/iptv-org/iptv), altri sono stream pubblici delle emittenti. Il repository non ospita né ritrasmette video e non garantisce la disponibilità futura dei collegamenti.

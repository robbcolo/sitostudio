---
name: Studio Dentistico Colombo
description: "La targa sul muro. L'ingresso dello studio di Patti: una lastra in plexiglass sul muro bianco e il citofono accanto."
colors:
  blu: "#0A67B0"
  blu-scuro: "#08568F"
  navy: "#192642"
  ink-soft: "#4A5670"
  calce: "#F2F4F5"
  calce-2: "#E9EDEF"
  calce-carta: "#FFFFFF"
  calce-riga: "rgba(25,38,66,.12)"
  plexi: "rgba(255,255,255,.38)"
  plexi-bordo: "rgba(25,38,66,.11)"
  acciaio: "#CDD2D8"
  acciaio-bordo: "#A3ACB5"
  filetto-targa: "#8FB4D9"
  selezione: "#CFE0F1"
  azure-pale: "#E3ECF5"
  border-strong: "rgba(25,38,66,.22)"
  text-on-dark: "#EEF2F6"
  stato-aperto: "#1B8A55"
  stato-tra-poco: "#D98E14"
  stato-chiuso: "#7A8597"
  smalto-urgenza: "#B42318"
typography:
  display:
    fontFamily: "Tenor Sans, Tenor Sans Fallback, Optima, Gill Sans, sans-serif"
    fontSize: "clamp(2.1rem, 1.3rem + 4vw, 3.6rem)"
    fontWeight: 400
    lineHeight: 1
    letterSpacing: "0.12em"
  headline:
    fontFamily: "Tenor Sans, Tenor Sans Fallback, Optima, Gill Sans, sans-serif"
    fontSize: "clamp(1.6rem, 1.2rem + 1.9vw, 2.75rem)"
    fontWeight: 400
    lineHeight: 1.12
    letterSpacing: "0.06em"
  titolo-pagina:
    fontFamily: "Tenor Sans, Tenor Sans Fallback, Optima, Gill Sans, sans-serif"
    fontSize: "clamp(2rem, 1.4rem + 2.6vw, 3.4rem)"
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: "0.005em"
  title:
    fontFamily: "Tenor Sans, Tenor Sans Fallback, Optima, Gill Sans, sans-serif"
    fontSize: "clamp(1.2rem, 1.1rem + 0.4vw, 1.4rem)"
    fontWeight: 400
    lineHeight: 1.25
  targa-riga:
    fontFamily: "Tenor Sans, Tenor Sans Fallback, Optima, Gill Sans, sans-serif"
    fontSize: "0.8125rem"
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: "0.34em"
  panel-heading:
    fontFamily: "Figtree, Figtree Fallback, system-ui, sans-serif"
    fontSize: "1.3125rem"
    fontWeight: 700
    lineHeight: 1.3
  lede:
    fontFamily: "Figtree, Figtree Fallback, system-ui, sans-serif"
    fontSize: "clamp(1.0625rem, 1rem + 0.3vw, 1.2rem)"
    fontWeight: 400
    lineHeight: 1.55
  body:
    fontFamily: "Figtree, Figtree Fallback, system-ui, sans-serif"
    fontSize: "1.0625rem"
    fontWeight: 400
    lineHeight: 1.65
  label:
    fontFamily: "Figtree, Figtree Fallback, system-ui, sans-serif"
    fontSize: "1rem"
    fontWeight: 700
    lineHeight: 1.2
  small:
    fontFamily: "Figtree, Figtree Fallback, system-ui, sans-serif"
    fontSize: "0.875rem"
    fontWeight: 400
    lineHeight: 1.3
rounded:
  tasto: "6px"
  lastra: "8px"
  barra: "10px"
  tondo: "999px"
spacing:
  stretto: "8px"
  base: "16px"
  blocco: "30px"
  colonna: "56px"
  pad-inline: "clamp(1.25rem, 3vw, 3.5rem)"
  sezione: "clamp(64px, 10vw, 128px)"
  muro: "1180px"
components:
  tasto-blu:
    backgroundColor: "{colors.blu}"
    textColor: "{colors.calce-carta}"
    typography: "{typography.label}"
    rounded: "{rounded.tasto}"
    padding: "0 18px"
    height: "50px"
  tasto-blu-hover:
    backgroundColor: "{colors.blu-scuro}"
  tasto-chiaro:
    backgroundColor: "{colors.calce-carta}"
    textColor: "{colors.navy}"
    typography: "{typography.label}"
    rounded: "{rounded.tasto}"
    padding: "0 18px"
    height: "50px"
  tasto-chiaro-hover:
    textColor: "{colors.blu}"
  cit-tasto:
    backgroundColor: "{colors.calce-carta}"
    textColor: "{colors.navy}"
    rounded: "{rounded.lastra}"
    padding: "8px 10px 8px 16px"
    height: "64px"
  cit-pulsante:
    backgroundColor: "{colors.blu}"
    textColor: "{colors.calce-carta}"
    rounded: "{rounded.tondo}"
    size: "44px"
  cit-pulsante-hover:
    backgroundColor: "{colors.blu-scuro}"
  targhetta-carta:
    backgroundColor: "{colors.calce-carta}"
    textColor: "{colors.navy}"
    rounded: "{rounded.lastra}"
    padding: "22px"
  targa:
    backgroundColor: "{colors.plexi}"
    textColor: "{colors.navy}"
    rounded: "{rounded.lastra}"
    padding: "48px 40px 36px"
  sit-voce:
    textColor: "{colors.navy}"
    typography: "{typography.title}"
    padding: "12px 2px"
    height: "62px"
  sit-voce-aperta:
    textColor: "{colors.blu}"
  sit-voce-urgente:
    textColor: "{colors.smalto-urgenza}"
  orari-oggi:
    textColor: "{colors.blu}"
  lastra-azione:
    backgroundColor: "{colors.plexi}"
    textColor: "{colors.navy}"
    rounded: "{rounded.lastra}"
  campo:
    backgroundColor: "{colors.calce-carta}"
    textColor: "{colors.navy}"
    rounded: "{rounded.tasto}"
    padding: "0.9rem 1rem"
    height: "50px"
  filtro-attivo:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.calce-carta}"
    rounded: "{rounded.tasto}"
---

# Design System: Studio Dentistico Colombo

> **Ambito.** Questo sistema vive su tutto il sito: la home e le 23 pagine interne (indice e 12 pagine dei trattamenti, indice delle schede, chi siamo, prima visita, dentista a Patti, contatti, prenota, domande frequenti, privacy, cookie, 404). Ogni pagina costruita da `page()` in `sorgenti/sitelib.py` (`MONDO_PAGINE = 'ingresso'`) ha la classe `w-ingresso` sul `body`, carica `css/ingresso.css` dopo `css/styles.css` e riceve la barra del citofono. Restano fuori, per scelta, solo le 12 schede singole (`sito/schede/*.html`, tema proprio `schede-theme.css`, costruite da `sorgenti/build_schede.py`). Il vecchio aspetto di `css/styles.css` (Newsreader, carta crema, archi, beige) resta solo come base sotto il mondo e **non** è un riferimento. Le nuove superfici seguono questo documento.

## Overview

**Creative North Star: "La targa sul muro"**

Il sito è l'ingresso dello studio come si presenta oggi: un muro bianco freddo, una lastra di plexiglass trasparente fissata con quattro distanziali d'acciaio che dice chi sono i dentisti, da quando sono a Patti, gli orari e se lo studio è aperto adesso; accanto, il citofono, che è l'azione. Tutto il resto del sito continua la stessa grammatica: titoli incisi in maiuscolo spaziato con un filetto sotto, etichette porta-nome bianche accanto ai volti, una seconda lastra per indirizzo e orari, elenchi a righe sottili al posto delle griglie di carte. Nelle pagine interne il titolo della pagina sta direttamente sul muro col filetto blu del logo, e il citofono è sempre a portata: barra agganciata in fondo e, nelle pagine dei trattamenti, citofono intero nel riquadro laterale.

Il tono visivo è moderno, chiaro e quieto. Il blu del logo dà il nome «COLOMBO» e i pulsanti; il blu notte scrive tutto il resto; il muro e la carta bianca fanno da fondo. Un solo segnale acceso per schermo: il punto dello stato aperto/chiuso. La densità è bassa nel primo schermo e media nelle sezioni, con righe sottili al posto delle schede pesanti.

Rifiuti confermati: niente richiami antichi o di lusso (oro, ottone, portoni dipinti, sabbia e beige del vecchio aspetto); niente hero con slogan e foto generica, niente righe di numeri o stelle.

**Key Characteristics:**
- Muro bianco freddo, lastra di plexiglass con bordo luminoso e distanziali d'acciaio.
- Tenor Sans in maiuscolo spaziato per targa e titoli, Figtree per leggere.
- Blu del logo solo per il nome, i pulsanti, i link e gli stati attivi; blu notte per il testo.
- Un solo segnale colorato acceso: il punto dello stato. L'unica eccezione cromatica è il rosso della voce d'urgenza.
- Righe sottili e carte bianche con bordo di 1px; ombre solo sulle lastre.
- Il citofono si aggancia come barra fissa quando esce dallo schermo; nelle pagine senza citofono la barra è agganciata da subito.

## Colors

Un muro freddo quasi bianco, due blu dal logo e un sistema di stato a semaforo; nessun colore caldo.

### Primary
- **Blu del logo** (`blu`): il colore riconoscibile dello studio. «COLOMBO» sulla targa, pulsanti tondi del citofono, `tasto-blu` e pulsanti primari comuni, link, voce aperta del selettore, anno sulle targhette dei dentisti, filetto sotto il titolo di pagina, riga di oggi negli orari (lettere in grassetto), icone delle righe e di WhatsApp, voce corrente dell'indice laterale, domanda aperta, sottolineatura della navigazione (piena, non più a tre colori), anello del focus.
- **Blu del logo scuro** (`blu-scuro`): solo hover e pressione di ciò che è già blu.

### Neutral
- **Blu notte** (`navy`): tutto il testo principale, i titoli, il filetto sotto i titoli, il cerchio numerato dei passi, il bordo del segno «+» delle domande, il filtro attivo delle schede e delle domande, il fondo del footer.
- **Inchiostro tenue** (`ink-soft`): testi di supporto, lede, descrizioni sotto i link, note del citofono.
- **Calce** (`calce`): il muro, fondo di pagina e della testata.
- **Calce ombra** (`calce-2`): fondo secondario; i vecchi token comuni `--beige` e `--beige-soft` puntano qui, `--bg-warm` anche.
- **Carta** (`calce-carta`): carte, tasti del citofono, etichette porta-nome, `tasto-chiaro`, barra agganciata.
- **Riga del muro** (`calce-riga`): ogni bordo da 1px e ogni divisorio di elenco; è anche `--border`.
- **Plexiglass** (`plexi`, `plexi-bordo`): faccia trasparente della lastra e suo bordo; sopra la faccia passa un riflesso a gradiente (vedi Elevation).
- **Acciaio** (`acciaio`, `acciaio-bordo`): solo i distanziali disegnati agli angoli delle lastre.
- **Filetto della targa** (`filetto-targa`): la riga azzurra tra nome e dottori sulla targa; sulla lastra degli orari la riga sotto l'indirizzo è il blu del logo al 55% (`rgba(10,103,176,.55)`).
- **Selezione** (`selezione`): fondo del testo selezionato.
- **Azzurro pallido** (`azure-pale`): fondo della scelta selezionata nei moduli (pillole).
- **Riga del campo** (`border-strong`): bordo dei campi dei moduli, più marcato della riga del muro perché il campo si trovi.
- **Bianco freddo su notte** (`text-on-dark`): testo del footer blu notte, a opacità tra 66% e 85% per note, colonne e link; sostituisce il vecchio crema.

### Stato e urgenza
- **Aperto** (`stato-aperto`), **Chiude tra poco** (`stato-tra-poco`), **Chiuso / festa / ferie** (`stato-chiuso`): solo il punto di stato (targa, lastra degli orari, riquadro del citofono, barra agganciata, footer e righe di contatto delle pagine interne), con alone di 3px al 20% quando aperto o in chiusura. I vecchi punti comuni sono ricolorati su questi tre token: niente rosso per «chiuso».
- **Smalto d'urgenza** (`smalto-urgenza`): solo l'etichetta e il titolo della voce «Ho dolore o un'urgenza».

### Named Rules
**The One Lit Signal Rule.** Su ogni schermo c'è un solo segnale colorato acceso: il punto dello stato. Il telefono della testata non ha un secondo punto, i pulsanti non hanno colori di stato, WhatsApp resta nel blu del logo (icona blu su tasto chiaro) e non diventa mai verde.

**The Urgent Red Rule.** Il rosso esiste solo sull'etichetta e sul titolo della voce d'urgenza, perché chi ha dolore la trovi a colpo d'occhio. I suoi pulsanti restano nel blu del logo.

**The Cold Wall Rule.** Nessun tono caldo: niente sabbia, beige, crema, oro o ottone. I vecchi token comuni (`--beige`, `--beige-soft`, `--bg-alt` → muro; `--beige-deep` → blu del logo; `--text-on-dark` → bianco freddo) sono rimappati e non vanno riportati in vita.

## Typography

**Display Font:** Tenor Sans 400 (con fallback metrico «Tenor Sans Fallback» su Optima / Gill Sans / Arial, `size-adjust:98%`), servito da `fonts/tenor-sans-400.woff2`.
**Body Font:** Figtree variabile (con fallback system-ui), servito da `fonts/figtree-var.woff2`.

**Character:** Tenor Sans ha il taglio inciso e geometrico di una targa professionale moderna; in maiuscolo spaziato si legge come lettere applicate sul plexiglass. Figtree è il testo da leggere: chiaro, amichevole, robusto sul telefono.

### Hierarchy
- **Display** (`display`, maiuscolo, `padding-left` uguale alla spaziatura per centrare otticamente): solo «COLOMBO» sulla targa, in blu del logo.
- **Riga di targa** (`targa-riga`, maiuscolo): «Studio Dentistico» sopra il nome, dentro lo stesso `h1`. Varianti più strette sulla targa: «Odontoiatri · a Patti dal 1992» (.2em), anno sulle targhette (.14em), «Orari» sulla lastra (.24em).
- **Titolo di pagina** (`titolo-pagina`, maiuscolo/minuscolo, `max-width:24ch`, `text-wrap:balance`): `h1` delle pagine interne, direttamente sul muro, seguito dal filetto blu del logo (56×2px, 20px sotto). Non è in maiuscolo: è il titolo da leggere, non una scritta incisa.
- **Headline** (`headline`, maiuscolo, `max-width:22ch`, `text-wrap:balance`): titolo di ogni sezione, sempre seguito dal filetto blu notte (56×2px, 18px sotto). Nelle pagine interne la stessa voce scala un poco più piccola (`clamp(1.55rem,1.2rem + 1.8vw,2.5rem)`, 1.14) e i titoli dei gruppi dell'indice trattamenti scendono a `clamp(1.25rem,1.05rem + .9vw,1.7rem)`. I titoli della fascia finale e dei riquadri laterali usano Tenor Sans maiuscolo a .05em (1.3rem nei riquadri).
- **Title** (`title`): voci del selettore «Cosa ti serve oggi?»; nomi dei dottori sulla targa e sulle targhette (Tenor Sans, .03em, in maiuscolo/minuscolo). Le risposte «Fa male?» e «Quanto costa?» usano Tenor Sans maiuscolo a 1.35rem.
- **Panel heading** (`panel-heading`): titoli dentro i pannelli aperti e i passi della prima visita (1.25rem). Nelle righe degli elenchi interni il titolo è Figtree 700 a 1.0625rem.
- **Lede** (`lede`): frase sotto ogni titolo, `ink-soft`, massimo 58ch. Su desktop la frase dell'ingresso passa a Tenor Sans.
- **Body** (`body`): testo corrente, 60–62ch.
- **Label** (`label`): testo dei tasti e nomi sul citofono (1.0625rem); note e sottotitoli in `small`.
- Tutti i titoli `h1`–`h3` del mondo sono in peso 400: Tenor Sans ha un solo peso, niente grassetto finto.
- Numeri degli orari sempre in cifre tabellari.

### Named Rules
**The Engraved Caps Rule.** Il maiuscolo spaziato appartiene solo a Tenor Sans e solo a ciò che starebbe inciso su una targa: nome, titoli di sezione, righe della targa, intestazione degli orari, indirizzo, titoli delle lastre. Figtree non va mai in maiuscolo spaziato; il titolo di pagina resta in maiuscolo/minuscolo.

**The No Kicker Rule.** Nessuna etichetta piccola sopra i titoli di sezione o di pagina. «Studio Dentistico» è parte del nome nell'`h1`, non un'eyebrow; le vecchie eyebrow delle pagine interne sono nascoste dal mondo e non tornano.

## Layout

Un muro unico, larghezza utile massima di 1180px (`muro`), margini laterali `pad-inline`. Le sezioni sotto l'ingresso si aprono con `sezione` di spazio sopra; dalla seconda in poi sono separate da una riga del muro sopra il contenuto (spazio ridotto a `clamp(40px,6vw,64px)` + `clamp(48px,7vw,88px)`).

**Ingresso.** Telefono: colonna centrata con targa (fino a 460px), citofono (fino a 460px), poi frase e tre volti. Da 960px: tre colonne sullo stesso muro, frase e volti a sinistra (fino a 360px, allineati a destra), targa al centro (460–540px), citofono a destra (fino a 330px); altezza `min(100svh - testata, 820px)`, contenuti centrati verticalmente.

**Sezioni.** Titolo e lede in alto a sinistra, contenuto 30–34px sotto. Da 960px il selettore diventa due colonne 5/7 (voci a sinistra, pannello aperto a destra, gap 56px); la prima visita 7/5 (passi e risposte); dove siamo 5/6. La famiglia passa a tre colonne uguali da 760px, i trattamenti a due colonne da 800px.

**Pagine interne.** Briciole, titolo di pagina col filetto blu e frase d'apertura in alto a sinistra (testata della pagina `clamp(20px,4vw,44px)` sopra, `clamp(28px,4vw,56px)` sotto), poi le sezioni comuni che alternano muro e muro ombra (`calce-2`) senza archi. Pagina di un trattamento: indice laterale a sinistra (barra orizzontale scorrevole su telefono), contenuto al centro, riquadro del citofono a destra. Gli elenchi «come lavoriamo», «cosa portare», valori e trattamenti collegati sono righe sotto un filo: una colonna su telefono, due da 800px (gap 48px), tre per i trattamenti collegati (gap 40px). Contatti: lastra degli orari a sinistra; righe di contatto, mappa su richiesta e modulo a destra. Chiude ogni pagina la fascia finale come lastra d'azione.

**Ritmo.** 8px tra elementi impilati di un gruppo (tasti del citofono, link del pannello), 16px tra blocchi vicini, 30–36px tra titolo e contenuto, 18px di aria sopra e sotto ogni riga d'elenco, 56px tra colonne su desktop. Breakpoint usati: 520, 640, 720, 760, 800, 960px.

## Elevation & Depth

Sistema piatto con un'unica eccezione materica: le lastre di plexiglass. Ce ne sono di due tipi. Le **lastre-targa** (la targa, la lastra degli orari in home e in Contatti) hanno i quattro distanziali d'acciaio. Le **lastre d'azione** (fascia finale di ogni pagina interna, riquadro del citofono nelle pagine dei trattamenti, riquadro «Pronto a venire?» della prima visita) hanno la stessa faccia, lo stesso spessore e la stessa ombra, ma senza distanziali. Tutto il resto (carte, tasti, citofono, voci, domande, campi) sta sul muro con un bordo da 1px e nessuna ombra; la testata scrollata mostra solo una riga, senza ombra; le carte al passaggio del puntatore cambiano solo il bordo, non si sollevano.

### Shadow Vocabulary
- **Ombra della lastra** (`box-shadow: 0 2px 3px rgba(20,35,60,.10), 0 24px 38px -26px rgba(20,35,60,.5)`): contatto e distacco della lastra dal muro, solo sulle lastre-targa e sulle lastre d'azione.
- **Spessore del plexiglass** (`box-shadow: inset 1.5px 1.5px 0 rgba(255,255,255,.95), inset -1px -1.5px 0 rgba(25,38,66,.09)`): luce sul bordo in alto a sinistra, ombra in basso a destra; sempre insieme all'ombra della lastra.
- **Riflesso** (`background: linear-gradient(160deg, rgba(255,255,255,.62), rgba(255,255,255,.12) 48%, rgba(255,255,255,.34))` sopra `plexi`): la faccia lascia vedere il muro.
- **Barra agganciata** (`box-shadow: 0 -10px 24px -18px rgba(20,35,60,.45)`): unica ombra fuori dalle lastre, per staccare la barra fissa dal contenuto che scorre sotto.
- **Fuoco dei campi** (`box-shadow: 0 0 0 4px rgba(10,103,176,.14)` con bordo blu): solo sui campi dei moduli in fuoco.
- **Alone di stato** (`box-shadow: 0 0 0 3px` del colore di stato al 20–22%): solo il punto aperto/in chiusura.

### Named Rules
**The Only Plates Float Rule.** Solo le lastre di plexiglass hanno ombra e spessore. Una carta bianca non diventa mai una lastra: per distinguerla basta il bordo. I distanziali d'acciaio spettano solo alle lastre-targa (chi siamo, indirizzo, orari, stato).

## Shapes

Angoli appena smussati, coerenti: 8px (`lastra`) per lastre, carte, tasti del citofono, ritratti, targhette, domande e riquadri; 6px (`tasto`) per i tasti, i pulsanti comuni, i campi, le pillole, i filtri e le etichette dei trattamenti; 10px per la barra agganciata su desktop. I vecchi raggi comuni sono rimappati sotto il mondo (`--radius-s` 6px, `--radius-m` e `--radius-l` 8px): niente pillole. Il tondo pieno è riservato ai pulsanti del citofono, ai punti di stato e ai cerchi numerati dei passi (40px, bordo 1.5px blu notte). I distanziali d'acciaio sono cerchi da 12px disegnati a 12px dagli angoli della lastra (10px sulla lastra degli orari). Nei volti dell'ingresso foto e etichetta formano un solo pezzo: foto con angoli superiori arrotondati, etichetta bianca senza bordo superiore con angoli inferiori arrotondati.

## Components

### Buttons
Tasti pieni e sobri, senza ombra né animazioni di riempimento. I pulsanti comuni delle pagine interne seguono la stessa coppia.
- **Shape:** angoli leggermente smussati (6px), altezza minima 50px (48px nella sezione Dove siamo), icona SVG 20px a sinistra.
- **Primary (`tasto-blu`):** blu del logo, testo bianco Figtree 700; hover `blu-scuro`. In Prenota l'invio del modulo su WhatsApp è il tasto blu, perché è l'azione della pagina.
- **Secondary (`tasto-chiaro`):** carta bianca, bordo riga del muro, testo blu notte; hover bordo e testo blu. WhatsApp è sempre un tasto chiaro con l'icona blu.
- **Link (`link`):** Figtree 700 blu, sottolineato 1px con offset 4px, freccia SVG; hover `blu-scuro`.
- **Focus:** anello di 3px blu del logo con offset 3px su tutto il mondo; sulla targa l'anello è blu notte.

### Citofono (signature)
La pulsantiera accanto alla targa: tre righe bianche (Chiama lo studio, Scrivi su WhatsApp, Prenota una visita), ognuna con nome in grassetto, una riga di nota sotto e un pulsante tondo blu da 44px a destra.
- **Riga:** carta bianca, bordo 1px riga del muro, 8px, altezza 64px; hover bordo blu, pulsante `blu-scuro`; pressione `scale(.94)` in 80ms.
- **Studio chiuso, festa o ferie** (`html[data-studio-kind]`): WhatsApp passa per primo; «Chiama» resta ma il suo pulsante diventa vuoto con anello blu notte da 1.5px. Le note sotto Chiama e WhatsApp sono scritte da `renderPorta`.
- **Riquadro del citofono** (pagine dei trattamenti): lastra d'azione con titolo in Tenor Sans maiuscolo, una frase, il punto di stato e il citofono intero.
- **Barra agganciata:** presente su ogni pagina del mondo. Dove c'è un citofono, quando questo esce dallo schermo la stessa pulsantiera compatta (Chiama, WhatsApp, Prenota, pulsanti da 30px) entra dal basso in 260ms con `ease-out`, preceduta dal punto di stato. Telefono: a tutta larghezza su fondo bianco al 96% con area sicura; desktop: in basso a destra, bordo e angoli da 10px. Rispetta l'ordine «chiuso» del citofono. Nelle pagine senza citofono (o senza `IntersectionObserver`) è agganciata dal caricamento; si disattiva quando il menu mobile è aperto.

### Targa (signature)
La lastra in plexiglass: logo, «Studio Dentistico», «COLOMBO» in blu, filetto azzurro, i tre dottori (link ai loro profili nella sezione famiglia), «Odontoiatri · a Patti dal 1992», orari, stato. Testo centrato. Lo stato è un punto da 10px seguito dall'etichetta in grassetto e dal dettaglio (vocabolario `open`, `closing`, `closed`, `holiday`, `ferie` di `computeStatus`); resta nascosto senza JavaScript. La **lastra degli orari** in Dove siamo è la stessa lastra, più piccola, con indirizzo in Tenor Sans maiuscolo blu sopra una riga blu al 55%, la tabella orari in Tenor Sans con righe del muro e oggi scritto in blu del logo grassetto (nessuna fascia di fondo). In Contatti la stessa lastra porta anche il punto di stato sotto l'indirizzo.

### Cards / Containers
- **Corner Style:** 8px.
- **Background:** carta bianca su muro.
- **Shadow Strategy:** nessuna (vedi The Only Plates Float Rule).
- **Border:** 1px riga del muro; hover sui link-carta, sulle carte delle schede e sulle voci dell'indice: bordo blu, nessun sollevamento.
- **Internal Padding:** 12–14px per i link nei pannelli, 22px per le risposte, 9×12px per le targhette porta-nome, 10×14px per le etichette delle assistenti.
- **Icone:** nelle carte e nelle righe le icone SVG stanno nude, in blu, senza tondo o fondo colorato.

### Selettore «Cosa ti serve oggi?»
Accordion a righe: ogni voce è un bottone a tutta larghezza in Tenor Sans, alto almeno 62px, separato da righe del muro, con chevron 22px che ruota di 180° in 250ms. Aperta o in hover diventa blu. Il pannello contiene titolo Figtree 700, testo, link-carta ai trattamenti e due tasti (Prenota in blu, WhatsApp chiaro). La prima voce è sempre l'urgenza: etichetta e titolo in `smalto-urgenza`, frase iniziale che cambia con lo stato, e a studio chiuso WhatsApp diventa il tasto blu e passa davanti a Chiama; sotto, un blocco di sicurezza separato da una riga (pronto soccorso, 112).

### Elenchi a righe
Passi della prima visita (cerchio numerato in Tenor Sans a sinistra), trattamenti (nome Figtree 700 e frase semplice; hover nome blu): sempre righe del muro sopra e sotto, niente carte. Nelle pagine interne, ogni serie di icona + titolo + testo («come lavoriamo», «cosa portare», valori, trattamenti collegati) è la stessa riga: icona blu 28px a sinistra, titolo Figtree 700, testo `ink-soft`, filo sopra il gruppo e sotto ogni riga; i trattamenti collegati diventano blu al passaggio.

### Percorso della prima visita
Linea verticale da 2px (riga del muro, avanzamento in blu del logo); cerchi numerati in Tenor Sans con bordo 1.5px blu notte su fondo muro, pieni di blu con numero bianco quando il passo è raggiunto. Nessun alone, nessuna sfumatura.

### Domande frequenti
Righe-carta bianche da 8px con bordo del muro; il segno «+» è un cerchio con anello blu notte da 1.5px che a domanda aperta si riempie di blu, e la carta aperta prende il bordo blu.

### Inputs / Fields
- **Style:** carta bianca, bordo `border-strong`, 6px, altezza minima 50px.
- **Focus:** bordo blu e alone di 4px blu al 14%.
- **Scelte (pillole):** 6px; selezionata con bordo blu e fondo `azure-pale`. **Filtri** delle schede e delle domande: 6px, attivo pieno blu notte.

### Famiglia
Ritratto quadrato piccolo (104px, 120px da 760px) accanto a un'etichetta porta-nome bianca (nome in Tenor Sans, anno in Tenor Sans maiuscolo blu), testo sotto. I tre dentisti hanno sempre la stessa misura e lo stesso peso, sempre nell'ordine Alfredo, Roberto, Aurora; Chi siamo usa la stessa coppia ritratto + etichetta della home. Le assistenti sono etichette bianche col solo nome e il ruolo.

### Navigation e componenti comuni riusati
Tutte le pagine del mondo riusano i componenti comuni di `css/styles.css`, rivestiti sotto `.w-ingresso`: testata (fondo muro al 97%, nome in Tenor Sans 1.18rem, voce corrente blu, sottolineatura piena blu), mega menu, menu mobile, palette di ricerca, visualizzatore delle schede, briciole (pagina corrente blu notte), indice laterale dei trattamenti, tabella orari, scheda della mappa (ridotta a carta bianca con nota e pulsante; la mappa si carica solo su richiesta). I pulsanti comuni `.btn` prendono angoli da 6px, perdono l'ombra e il riempimento al passaggio del puntatore. Il footer resta blu notte con testo in bianco freddo. Nella 404 lo «0» è il logo dello studio. Sono nascosti nel mondo: barra di avanzamento, WhatsApp laterale, torna su, punto di stato della testata, eyebrow, sorrisi, archi e anelli decorativi, avatar disegnati; in home anche stato e orari nel footer.

## Do's and Don'ts

### Do:
- **Do** mettere ogni nuova superficie sul muro `calce` con testo `navy`, e usare il `blu` solo per nome, azioni, link e stato attivo.
- **Do** aprire ogni sezione con il titolo in Tenor Sans maiuscolo spaziato e il suo filetto blu notte da 56×2px; ogni pagina interna con il titolo di pagina sul muro e il filetto blu del logo.
- **Do** usare la lastra con i quattro distanziali solo per le informazioni che starebbero su una targa vera: chi siamo, indirizzo, orari, stato. Per la fascia finale e i riquadri d'azione usare la lastra senza distanziali.
- **Do** trasformare le serie di icona + titolo + testo in righe sotto un filo, non in griglie di carte uguali.
- **Do** tenere il contatto a un tocco: citofono o barra agganciata con Chiama, WhatsApp, Prenota, e l'ordine che cambia a studio chiuso.
- **Do** separare contenuti con righe da 1px `calce-riga` prima di ricorrere a una carta.
- **Do** mostrare i tre dentisti sempre alla stessa misura.

### Don't:
- **Don't** usare oro, ottone, sabbia, beige, crema o portoni dipinti: il sito deve sembrare moderno.
- **Don't** aggiungere un secondo segnale acceso accanto al punto di stato, né colorare di verde WhatsApp.
- **Don't** usare il rosso fuori dall'etichetta e dal titolo della voce d'urgenza.
- **Don't** dare ombra a carte, tasti o citofono, né farli sollevare al passaggio del puntatore: solo le lastre si staccano dal muro.
- **Don't** mettere etichette piccole sopra i titoli, righe di numeri o stelle.
- **Don't** prendere come riferimento il vecchio aspetto di `css/styles.css` che resta sotto il mondo (Newsreader, archi, anelli, sorrisi, eyebrow, sottolineature a tre colori, pulsanti a pillola con riempimento radiale, WhatsApp verde, fasce blu notte di chiusura).

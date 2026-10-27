# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users

**Primari: nuovi pazienti di Patti e dintorni** (provincia di Messina) che cercano un dentista, quasi sempre dallo smartphone, di solito arrivando da una ricerca Google («dentista Patti») o dalla scheda Google dello studio. Devono capire in fretta se lo studio fa quello che serve loro e se possono fidarsi, poi chiamare o scrivere su WhatsApp con un tocco. Il sito oggi li accoglie in sette situazioni concrete: un controllo, dolore o urgenza, un dente mancante, un sorriso più bello, gengive che sanguinano, un dente da curare, un figlio da portare.

**Secondari:**
- pazienti già in cura che cercano orari, contatti o una scheda da rileggere a casa;
- i dentisti stessi, che aprono le schede a tutto schermo alla poltrona per spiegare un trattamento.

## Product Purpose

È il sito dello Studio Dentistico Colombo di Patti. Serve a far scegliere lo studio a chi non lo conosce e a portarlo al primo contatto: telefonata, messaggio WhatsApp o richiesta di visita. Spiega anche ogni trattamento in modo chiaro e onesto, prima che il paziente arrivi in studio.

Funziona quando un nuovo paziente della zona, dal telefono, trova ciò che cerca, si sente rassicurato e contatta lo studio.

## Positioning

Tre punti, nell'ordine:

1. **Famiglia e continuità.** Alfredo Colombo esercita a Patti dal 1992. I figli Roberto e Aurora, anche loro odontoiatri, lavorano con lui ogni giorno nello stesso ambulatorio. Chi ti cura oggi conosce la tua storia clinica e ti seguirà negli anni, e sui casi delicati i tre dentisti si confrontano.
2. **Spiegare prima di curare.** Dodici schede illustrate scritte dallo studio, un piano di cura con i costi spiegato prima di iniziare, decisioni prese con calma. Il tono è onesto e non mette pressione.
3. **Strumenti attuali.** Scanner intraorale per l'impronta digitale (niente pasta), corone, onlay e intarsi in zirconia senza metallo, strumenti per le cure canalari aperti nuovi per ogni paziente.

La pedodonzia (con Aurora come riferimento per i bambini) e l'attenzione ai pazienti ansiosi sono servizi offerti, non elementi di posizionamento.

## Operating Context

- **Come arrivano:** ricerca Google locale, Google Business Profile, passaparola. Nome, indirizzo e telefono devono essere identici ovunque (sito, Google, social, elenchi).
- **Come contattano:** telefono negli orari di apertura (per le urgenze è il canale più rapido), WhatsApp anche fuori orario. Non c'è prenotazione online con calendario: il modulo di Prenota prepara un messaggio WhatsApp e quello di Contatti prepara un'email, e nessuno dei due salva dati sul sito.
- **Orari:** lunedì–giovedì 8:30–12:30 e 16:00–20:00, venerdì 8:30–12:30, sabato e domenica chiuso. Lo stato «aperto/chiuso» si calcola dal vivo con ora italiana, festività nazionali e ferie impostate in `sito/js/config.js`.
- **In studio:** le schede si aprono a tutto schermo alla poltrona e si scorrono una dopo l'altra. Si condividono con link o codice QR e si stampano. Daniela e Tonina, le assistenti alla poltrona, accolgono il paziente.
- **Manutenzione:** le pagine si generano dai programmi Python in `sorgenti/` (`python3 sorgenti/build.py`) dentro `sito/`. Contatti, orari, ferie, social e recensioni si cambiano in `sito/js/config.js`. Dominio, civico e social si cambiano in tutte le pagine con `strumenti/imposta-sito.py`.
- **Pubblicazione:** il contenuto di `sito/` si carica via FTP su Aruba. Ogni push su `main` che tocca `sito/` aggiorna da solo l'anteprima pubblica su GitHub Pages.

## Capabilities and Constraints

- **Contenuti:** 12 pagine di trattamento (igiene e prevenzione, conservativa, endodonzia, parodontologia, chirurgia orale, implantologia, protesi, ortodonzia con Invisalign, gnatologia, estetica, pedodonzia, scanner intraorale), 12 schede informative, più prima visita, chi siamo, FAQ, dentista a Patti, prenota, contatti, privacy, cookie e 404.
- **Clinica:** solo anestesia locale, nessuna sedazione. Per l'urgenza fuori orario il sito rimanda al pronto soccorso o al 112.
- **Tono solo informativo** (Legge 145/2018 e codice deontologico): niente toni promozionali, sconti, foto prima/dopo o promesse di risultato.
- **Nessun tracciamento:** niente cookie di tracciamento, analytics, font o script da servizi esterni. La mappa Google si carica solo se il visitatore tocca «Mostra la mappa». Per questo non c'è banner cookie, e privacy e cookie policy vanno aggiornate se si aggiunge qualcosa.
- **Sito statico su Aruba:** HTML, CSS e JavaScript puri, niente WordPress né database. Unica eccezione facoltativa: `sito/api/recensioni.php` (PHP su Aruba) per le recensioni Google automatiche. Il sito deve restare leggibile e usabile anche con JavaScript disattivato.
- **Nessun contenuto inventato:** niente recensioni, numeri, prezzi, titoli o affermazioni non confermati. Ogni testo medico nuovo o modificato va approvato dai dentisti prima di andare online.
- **Dati segnaposto ancora aperti:**
  - dominio definitivo (oggi provvisorio `https://www.studiodentisticocolombo.it`);
  - numero civico di Via Fontanella;
  - link Facebook e Instagram (finché mancano, i pulsanti restano nascosti);
  - link diretto per scrivere una recensione Google;
  - foto di Daniela e Tonina;
  - verifica della frase «dall'autostrada A20 si esce a Patti»;
  - approvazione finale dei testi medici di schede e trattamenti.

## Brand Commitments

- Nome esatto: **Studio Dentistico Colombo**, Via Fontanella, 98066 Patti (ME). Telefono 0941 22749, WhatsApp +39 379 152 3085, email colombostudiodentistico@gmail.com, P. IVA 01777580836.
- Logo: `sito/assets/logo.png`, da usare così com'è (il dente nella C, blu e blu notte).
- Il blu del logo (`#0A67B0`) resta il colore riconoscibile dello studio, anche con un aspetto nuovo.
- Il sito deve sembrare moderno: niente richiami antichi o di lusso (oro, ottone, portoni dipinti).
- Voce: italiano semplice, frasi brevi, si dà del «tu» al paziente. Si spiega cosa si sente e cosa succede, con calma e senza allarmismi. I titoli sono «Dott.» e «Dott.ssa»; nel testo corrente i dentisti si chiamano per nome (Alfredo, Roberto, Aurora).
- Il sito è solo in italiano.

## Evidence on Hand

- **Team:**
  - Dott. Alfredo Colombo: fondatore, laureato a Messina nel 1989, a Patti dal 1992;
  - Dott. Roberto Colombo: laureato a Messina, esercita dal 2024, sta completando un master in implantoprotesi a Torino, si interessa in particolare di implantologia e parodontologia;
  - Dott.ssa Aurora Colombo: laureata a Torino nel 2025, frequenta la specializzazione in Chirurgia Orale a Messina, riferimento per i bambini;
  - assistenti Daniela e Tonina.
- **Foto vere:** ritratti di Alfredo, Roberto e Aurora in `sito/assets/team/`.
- **Schede:** 12 schede con illustrazioni in `sito/assets/schede/`. I sorgenti originali sono in `sorgenti/schede-sorgenti/`.
- **Immagine per i social:** `sito/assets/og-cover.jpg`.
- **Assenti, da non inventare:** foto dell'ambulatorio e della sala d'attesa, recensioni (oggi il sito invita solo a lasciarne una su Google), prezzi, numero di pazienti curati, certificazioni o premi.

## Product Principles

1. **Il contatto è a un tocco.** Ogni pagina deve portare in fretta a chiamare, scrivere su WhatsApp o chiedere una visita dal telefono.
2. **Informare, non vendere.** Fatti, tempi, rischi e alternative al posto di promesse. Il paziente decide con calma.
3. **Persone e fatti veri.** La fiducia viene dai nomi, dai volti e dalla storia reale della famiglia Colombo. Se un dato manca, si omette invece di inventarlo.
4. **Chiaro anche per chi ha paura.** Prima della tecnica viene la risposta alle domande che il paziente si fa davvero: fa male, quanto dura, cosa succede dopo.
5. **Leggero e privato.** Il sito funziona senza tracciamento né servizi esterni, e i dati che cambiano (orari, ferie, contatti) si aggiornano senza programmatori.

## Accessibility & Inclusion

Non ci sono esigenze specifiche dichiarate oltre all'uso quasi esclusivo da smartphone. Restano gli impegni già presi dal sito: rispetto delle animazioni ridotte, navigazione completa da tastiera, compatibilità con i lettori di schermo, uso possibile senza JavaScript.

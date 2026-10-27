# -*- coding: utf-8 -*-
"""Pagine: home, hub trattamenti, pagina trattamento, schede."""
from sitelib import *

BLURB = {
    'igiene-prevenzione': 'Pulizia professionale dei denti e controlli periodici, per prevenire carie e infiammazioni.',
    'conservativa': 'Cura della carie e otturazioni dello stesso colore del dente, fino ai restauri su misura.',
    'endodonzia': 'La cura canalare per salvare un dente quando carie o trauma raggiungono il nervo.',
    'parodontologia': 'Cura delle gengive che sanguinano e dei tessuti che sostengono i denti.',
    'chirurgia-orale': 'Estrazioni, denti del giudizio e piccoli interventi chirurgici in anestesia locale.',
    'implantologia-dentale': 'Impianti per sostituire uno o più denti mancanti, senza limare i denti vicini.',
    'protesi-dentarie': 'Corone, ponti e protesi mobili su misura per tornare a masticare e sorridere.',
    'ortodonzia': 'Apparecchi fissi, mobili e allineatori trasparenti Invisalign, per bambini e adulti.',
    'gnatologia': "Bruxismo, dolore alla mandibola e disturbi dell'articolazione, spesso con un bite su misura.",
    'estetica-dentale': 'Sbiancamento, faccette e ricostruzioni in composito per un sorriso più armonioso.',
    'pedodonzia': 'La prima visita e la cura dei più piccoli, con Aurora Colombo come punto di riferimento.',
    'scanner-intraorale': "L'impronta digitale in pochi minuti, senza pasta e senza fastidio.",
}

DOCTOR_NOTE = {
    'implantologia-dentale': 'In studio Roberto Colombo segue in particolare questa area, con un master post-laurea in implantoprotesi.',
    'parodontologia': 'Roberto Colombo ha un interesse particolare per la parodontologia.',
    'pedodonzia': 'Il punto di riferimento per i pazienti bambini è Aurora Colombo.',
    'chirurgia-orale': 'Aurora Colombo sta frequentando la scuola di specializzazione in Chirurgia Orale a Messina.',
}

def provider():
    return {"@type": "Dentist", "name": SITE_NAME, "url": SITE_URL + "/", "telephone": PHONE_SCHEMA,
            "image": SITE_URL + "/assets/logo.png",
            "address": {"@type": "PostalAddress", "streetAddress": "Via Fontanella", "addressLocality": "Patti", "addressRegion": "ME", "postalCode": "98066", "addressCountry": "IT"}}

def website_ld():
    return {"@context": "https://schema.org", "@type": "WebSite", "@id": SITE_URL + "/#sito", "url": SITE_URL + "/", "name": SITE_NAME,
            "inLanguage": "it-IT", "publisher": provider()}

# =============================================================== HOME =========
FINDER = [
    dict(id='controllo', ico='calendar', label='Voglio fare un controllo',
         title='Un controllo e una pulizia',
         text='Una visita di controllo e una seduta di igiene professionale sono il modo più semplice per tenere sotto controllo denti e gengive, prima che ci sia un dolore.',
         links=[('igiene-prevenzione', None), ('prima-visita', ('La prima visita', 'Come si svolge, cosa portare, cosa aspettarti.'))], schede=['ablazione-e-scaling']),
    dict(id='dolore', ico='bolt', label="Ho dolore o un'urgenza", urgent=True,
         title='Dolore, gonfiore o trauma',
         text='Se un dente fa molto male, la gengiva è gonfia o hai preso una botta, non aspettare: chiamaci.',
         links=[('endodonzia', None), ('chirurgia-orale', None)], schede=['cura-canalare'],
         note="Con un dente caduto del tutto, conservalo in un contenitore con latte o saliva e portalo con te. Fuori orario, rivolgiti al pronto soccorso. Se il gonfiore si estende a viso o collo, o fai fatica a respirare o a deglutire, chiama subito il 112."),
    dict(id='mancanti', ico='tooth', label='Mi manca un dente',
         title='Sostituire uno o più denti',
         text='Impianto, ponte e protesi mobile sono tre strade diverse. Dopo la visita ti spieghiamo vantaggi e limiti di ciascuna nel tuo caso.',
         links=[('implantologia-dentale', None), ('protesi-dentarie', None)], schede=['impianto-dentale', 'ponte-dentale', 'protesi-mobile']),
    dict(id='sorriso', ico='smile', label='Voglio un sorriso più bello',
         title='Estetica e allineamento',
         text="Sbiancamento, faccette o apparecchio: prima di scegliere guardiamo la salute di denti e gengive, poi ti mostriamo cosa è possibile fare.",
         links=[('estetica-dentale', None), ('ortodonzia', None)], schede=['sbiancamento-dentale', 'faccette-dentali']),
    dict(id='gengive', ico='shield', label='Le gengive sanguinano',
         title='Gengive che sanguinano',
         text='Il sanguinamento è spesso il primo segnale di un’infiammazione. Controllarla presto è molto più semplice che curarla tardi.',
         links=[('parodontologia', None), ('igiene-prevenzione', None)], schede=['ablazione-e-scaling']),
    dict(id='cura', ico='check', label='Devo curare un dente',
         title='Carie e denti rovinati',
         text='Dalla piccola otturazione alla cura canalare, fino alle corone su misura: si sceglie la soluzione che conserva più dente sano possibile.',
         links=[('conservativa', None), ('endodonzia', None)], schede=['cura-canalare', 'corona-onlay-intarsio']),
    dict(id='bambini', ico='baby', label='Devo portare mio figlio',
         title='La visita dei più piccoli',
         text="La prima visita non deve aspettare il primo mal di denti. In studio il punto di riferimento per i bambini è Aurora Colombo.",
         links=[('pedodonzia', None), ('ortodonzia', None)], schede=[]),
]

# La home è l'ingresso dello studio: la targa in plexiglass (chi, da quando, orari, stato)
# e il citofono (chiamare, scrivere, prenotare). L'urgenza è la prima voce di «Cosa ti serve oggi?».
SITUAZIONI = [f for f in FINDER if not f.get('urgent')]
URGENZA = next(f for f in FINDER if f.get('urgent'))

DOTTORI = [  # testi ricavati dai profili lunghi di TEAM
    dict(slug='alfredo', targa='Dott. Alfredo Colombo', anno='A Patti dal 1992',
         testo='Ha fondato lo studio. Laureato a Messina nel 1989, lavora a Patti dal 1992 e si occupa di ogni tipo di trattamento, dalla prevenzione alla chirurgia.'),
    dict(slug='roberto', targa='Dott. Roberto Colombo', anno='Esercita dal 2024',
         testo='Laureato a Messina, sta completando un master in implantoprotesi a Torino. Segue in particolare implantologia e parodontologia.'),
    dict(slug='aurora', targa='Dott.ssa Aurora Colombo', anno='Laureata nel 2025',
         testo='Laureata a Torino, frequenta la specializzazione in Chirurgia Orale a Messina. È il punto di riferimento quando a curarsi è un bambino.'),
]

MSG_URGENZA = 'Buongiorno, ho un dolore o un’urgenza dentale. Potete aiutarmi?'

def ingresso(P):
    """Il primo schermo: la targa in plexiglass sul muro bianco dello studio, il citofono accanto,
    e sul muro la frase e i volti dei tre dentisti."""
    nomi = ''.join(f'<li><a href="#dott-{d["slug"]}">{esc(d["targa"])}</a></li>' for d in DOTTORI)
    volti = ''.join(f'<li><a href="#dott-{d["slug"]}"><img src="{P}assets/team/{d["slug"]}.jpg" alt="" width="500" height="500" decoding="async"><span>{esc(d["targa"].split()[1])}</span></a></li>' for d in DOTTORI)
    return f'''<section class="ingresso" aria-labelledby="targa-nome">
<div class="targa">
<img class="targa-logo" src="{P}assets/logo.png" alt="" width="425" height="425">
<h1 class="targa-nome" id="targa-nome"><span class="targa-k">Studio Dentistico</span> <span class="targa-n">Colombo</span></h1>
<ul class="targa-dottori" aria-label="I dentisti dello studio">{nomi}</ul>
<p class="targa-dal"><span class="unito">Odontoiatri</span><span class="sep"> · </span><span class="unito">a Patti dal 1992</span></p>
<p class="targa-orari"><span>Lun–Gio 8:30–12:30 · 16:00–20:00</span> <span>Ven 8:30–12:30</span></p>
<p class="targa-stato" data-plate-status hidden><i class="stato-punto" aria-hidden="true"></i><b data-plate-label></b> <span data-plate-detail></span></p>
</div>
{citofono(P)}
<div class="ingresso-muro">
<p class="ingresso-frase">Padre e figli, dentisti nello stesso studio di Via Fontanella. Prima di ogni cura ti spieghiamo cosa faremo, quanto dura e quanto costa.</p>
<ul class="volti" aria-label="Conosci i dentisti">{volti}</ul>
</div>
</section>'''

def urgenza_voce(P):
    """La prima voce del selettore: dolore o urgenza. Sa se lo studio è aperto (main.js, renderPorta)."""
    pannello = (f'<h4>Dolore, gonfiore o un dente rotto</h4>'
                f'<p class="urg-lead" data-urg-aperto>Chiamaci subito: negli orari di apertura cerchiamo sempre di trovare spazio per le urgenze.</p>'
                f'<p class="urg-lead" data-urg-chiuso hidden>Adesso lo studio è chiuso<span data-urg-riapre></span>. Scrivici su WhatsApp: ti ricontattiamo appena riapriamo.</p>'
                f'<div class="sit-azioni urg-tasti"><a class="tasto tasto-blu" href="tel:{PHONE_HREF}" data-tel data-urg-call>{ICON["phone"]}<span>Chiama <span data-tel-text>{PHONE}</span></span></a>'
                f'<a class="tasto tasto-chiaro" href="{wa_link(MSG_URGENZA)}" data-whatsapp data-wa-msg="{esc(MSG_URGENZA)}" target="_blank" rel="noopener" data-urg-wa>{ICON["whatsapp"]}<span>Scrivi su WhatsApp</span></a></div>'
                f'<div class="urg-sicurezza"><p><strong>Fuori orario</strong>, per un trauma importante, rivolgiti al pronto soccorso più vicino. Se un dente è caduto del tutto, conservalo in un contenitore con latte o saliva e portalo con te: nei traumi dentali il tempo conta.</p>'
                f'<p><strong>Chiama subito il 112</strong> se il gonfiore si estende a viso o collo, o se fai fatica a respirare o a deglutire.</p></div>')
    return (f'<div class="sit sit-urgente"><h3 class="sit-h"><button class="sit-btn" type="button" aria-expanded="false" aria-controls="sit-urgenza" id="sitb-urgenza">'
            f'<span>{esc(URGENZA["label"])}</span>{ICON["chev"]}</button></h3>'
            f'<div class="sit-pannello" id="sit-urgenza" role="region" aria-labelledby="sitb-urgenza" data-urgenza>{pannello}</div></div>')

def situazioni(P):
    items = urgenza_voce(P)
    for f in SITUAZIONI:
        links = ''
        for slug, custom in f['links']:
            if custom:
                links += f'<li><a href="{P}prima-visita.html"><b>{esc(custom[0])}</b><span>{esc(custom[1])}</span></a></li>'
            else:
                links += f'<li><a href="{P}servizi/{slug}.html"><b>{esc(S[slug]["name"])}</b><span>{esc(BLURB[slug])}</span></a></li>'
        msg = 'Buongiorno, vorrei informazioni: ' + f['label'].lower() + '.'
        cta = (f'<div class="sit-azioni"><a class="tasto tasto-blu" href="{P}prenota.html">{ICON["calendar"]}<span>Prenota una visita</span></a>'
               f'<a class="tasto tasto-chiaro" href="{wa_link(msg)}" data-whatsapp data-wa-msg="{esc(msg)}" target="_blank" rel="noopener">{ICON["whatsapp"]}<span>Chiedi su WhatsApp</span></a></div>')
        items += (f'<div class="sit"><h3 class="sit-h"><button class="sit-btn" type="button" aria-expanded="false" aria-controls="sit-{f["id"]}" id="sitb-{f["id"]}">'
                  f'<span>{esc(f["label"])}</span>{ICON["chev"]}</button></h3>'
                  f'<div class="sit-pannello" id="sit-{f["id"]}" role="region" aria-labelledby="sitb-{f["id"]}"><h4>{esc(f["title"])}</h4><p>{esc(f["text"])}</p>'
                  f'<ul class="sit-cure">{links}</ul>{cta}</div></div>')
    return (f'<section class="muro situazioni-sec" id="orientamento" aria-labelledby="sit-t"><div class="muro-in">'
            f'<h2 class="titolo" id="sit-t">Cosa ti serve oggi?</h2>'
            f'<p class="lede">Scegli la situazione più vicina alla tua: ti diciamo da quale cura partire. Nelle pagine dei trattamenti trovi anche le schede da leggere con calma.</p>'
            f'<div class="situazioni" data-situazioni>{items}</div></div></section>')

def famiglia(P):
    figs = ''.join(f'<figure class="dott" id="dott-{d["slug"]}"><img src="{P}assets/team/{d["slug"]}.jpg" alt="Ritratto di {esc(d["targa"])}" width="500" height="500" loading="lazy" decoding="async">'
                   f'<figcaption><span class="dott-targhetta"><span class="dott-nome">{esc(d["targa"])}</span><span class="dott-anno">{esc(d["anno"])}</span></span><span class="dott-testo">{esc(d["testo"])}</span></figcaption></figure>'
                   for d in DOTTORI)
    return (f'<section class="muro famiglia-sec" id="team" aria-labelledby="famiglia-t"><div class="muro-in">'
            f'<h2 class="titolo" id="famiglia-t">Tre dentisti, una famiglia</h2>'
            f'<p class="lede">Alfredo esercita a Patti dal 1992. Roberto e Aurora sono i figli: oggi lavorano insieme nello stesso studio, e chi ti cura conosce la tua storia.</p>'
            f'<div class="dottori">{figs}</div>'
            f'<p class="assistenti">In studio ti accolgono <strong>Daniela</strong> e <strong>Tonina</strong>, le assistenti alla poltrona: ti seguono dall’arrivo alla fine della seduta.</p>'
            f'<p class="sec-link"><a class="link" href="{P}chi-siamo.html">La storia dello studio {ARR}</a></p></div></section>')

def prima_visita_home(P):
    steps = [
        ('Ci contatti', 'Telefono, WhatsApp o il modulo del sito: scegli tu. Ti rispondiamo con le date più vicine alle tue esigenze.'),
        ('Ti accogliamo', 'Daniela o Tonina ti accolgono in studio. Ti chiediamo qualche informazione sulla tua salute e sui farmaci che prendi.'),
        ('Visita e, se serve, scansione', 'Guardiamo denti e gengive e, quando è utile, usiamo lo scanner intraorale o una radiografia. Niente impronte in pasta.'),
        ('Il piano di cura, spiegato', 'Ti raccontiamo cosa abbiamo trovato, quali strade ci sono e i costi, prima di iniziare. Decidi con calma.'),
    ]
    passi = ''.join(f'<li><h3>{esc(t)}</h3><p>{esc(p)}</p></li>' for t, p in steps)
    return (f'<section class="muro visita-sec" id="prima-visita" aria-labelledby="visita-t"><div class="muro-in">'
            f'<h2 class="titolo" id="visita-t">La prima visita</h2>'
            f'<p class="lede">Sapere cosa ti aspetta aiuta ad arrivare più tranquillo. Ecco come va, e le due domande che ci fanno più spesso.</p>'
            f'<div class="visita-grid"><ol class="passi">{passi}</ol>'
            f'<div class="risposte">'
            f'<div class="risposta"><h3>Fa male?</h3><p>Con l’anestesia locale la maggior parte delle cure, comprese devitalizzazioni ed estrazioni, si fa senza dolore; nei giorni dopo alcune cure è normale un po’ di sensibilità. Se hai paura, diccelo: adattiamo tempi e modi della visita.</p>'
            f'<a class="link" href="{P}faq.html#d-le-cure-dal-dentista-sono-dolorose">Leggi la risposta completa {ARR}</a></div>'
            f'<div class="risposta"><h3>Quanto costa?</h3><p>Dipende da cosa serve nel tuo caso. Dopo la visita ti presentiamo un piano di cura chiaro, con i tempi e i costi, prima di iniziare qualsiasi trattamento.</p>'
            f'<a class="link" href="{P}prima-visita.html">Come funziona la prima visita {ARR}</a></div>'
            f'</div></div></div></section>')

def trattamenti_home(P):
    cure = ''.join(f'<li><a href="{P}servizi/{s}.html"><b>{esc(S[s]["name"])}</b><span>{esc(BLURB[s])}</span></a></li>' for s in SERVICE_ORDER)
    return (f'<section class="muro cure-sec" id="trattamenti" aria-labelledby="cure-t"><div class="muro-in">'
            f'<h2 class="titolo" id="cure-t">I trattamenti</h2>'
            f'<p class="lede">Dalla prevenzione alla chirurgia, per adulti e bambini, tutto nello stesso studio.</p>'
            f'<ul class="cure">{cure}</ul>'
            f'<p class="sec-link"><a class="link" href="{P}servizi.html">Tutti i trattamenti, spiegati {ARR}</a></p></div></section>')

def dove_siamo(P):
    # la targhetta con indirizzo e orari è il centro della sezione; la mappa si chiede a parte
    return (f'<section class="muro dove-sec" id="dove-siamo" aria-labelledby="dove-t"><div class="muro-in">'
            f'<h2 class="titolo" id="dove-t">Ci trovi in Via Fontanella, a Patti</h2>'
            f'<div class="dove-grid">'
            f'<div class="targhetta"><p class="targhetta-via" data-address-text>{ADDRESS_LINE}</p><h3 class="dove-h">Orari</h3>{hours_table()}</div>'
            f'<div class="dove-info">'
            f'<p class="dove-note">Dall’autostrada A20 si esce a Patti.</p>'
            f'<div class="dove-tasti"><a class="tasto tasto-chiaro" data-gmaps href="https://www.google.com/maps/search/?api=1&query=Studio+Dentistico+Colombo+Patti+ME" target="_blank" rel="noopener">{ICON["pin"]}<span>Google Maps</span></a>'
            f'<a class="tasto tasto-chiaro" data-amaps href="https://maps.apple.com/?q=Studio+Dentistico+Colombo&ll={LAT},{LNG}" target="_blank" rel="noopener">{ICON["pin"]}<span>Apple Maps</span></a>'
            f'<button class="tasto tasto-chiaro" type="button" data-copy="address" data-copy-msg="Indirizzo copiato">{ICON["file"]}<span>Copia indirizzo</span></button>'
            f'<button class="tasto tasto-chiaro" type="button" data-vcard>{ICON["plus"]}<span>Salva in rubrica</span></button></div>'
            f'{map_card(P)}'
            f'<p class="dove-recensioni" data-reviews-fallback>Le recensioni dei pazienti sono su Google. <a class="link" data-reviews-url href="https://www.google.com/maps/search/?api=1&query=Studio+Dentistico+Colombo+Patti+ME" target="_blank" rel="noopener">Leggile o lascia la tua {ICON["external"]}</a></p>'
            f'<div data-reviews hidden></div>'
            f'</div></div></div></section>')

TEAM = [
    dict(slug='roberto', name='Dott. Roberto Colombo', short="Laureato all'Università di Messina, si dedica in particolare a implantologia e protesi, con una formazione post-laurea in continuo aggiornamento.",
         long="Laureato in Odontoiatria e Protesi Dentaria presso l'Università degli Studi di Messina, esercita la professione dal 2024. Sta completando un master post-laurea in implantoprotesi presso l'Università di Torino, con un interesse particolare per l'implantologia e la parodontologia.",
         uni='Università degli Studi di Messina'),
    dict(slug='alfredo', name='Dott. Alfredo Colombo', short='Fondatore dello studio, laureato a Messina nel 1989. Lavora a Patti dal 1992 e si occupa di ogni tipo di trattamento.',
         long='Fondatore dello studio, laureato in Odontoiatria presso l\'Università degli Studi di Messina nel 1989. Lavora a Patti dal 1992 e si occupa naturalmente di ogni tipo di trattamento, dalla prevenzione alla chirurgia.',
         uni='Università degli Studi di Messina'),
    dict(slug='aurora', name='Dott.ssa Aurora Colombo', short='Laureata a Torino nel 2025, sta specializzandosi in Chirurgia Orale a Messina. Il punto di riferimento in studio quando si tratta di pazienti bambini.',
         long="Laureata in Odontoiatria presso l'Università degli Studi di Torino nel 2025, sta frequentando la scuola di specializzazione in Chirurgia Orale dell'Università degli Studi di Messina. In studio si occupa di ogni tipo di trattamento, ma è lei il punto di riferimento quando ad avere bisogno di cure è un bambino.",
         uni='Università degli Studi di Torino'),
]

def portrait(P, t):
    return (f'<div class="portrait"><img src="{P}assets/team/{t["slug"]}.jpg" alt="{esc(t["name"])}" width="500" height="500" loading="lazy" decoding="async">'
            f'<svg viewBox="0 0 100 100" aria-hidden="true"><circle class="a1" cx="50" cy="50" r="53"/><circle class="a2" cx="50" cy="50" r="49"/><circle class="a3" cx="50" cy="50" r="45"/></svg></div>')

def team_grid(P, long=False):
    if mondo() == 'ingresso':
        # come nella home: Alfredo, Roberto, Aurora, ritratto con l'etichetta nome + anno e il profilo
        per_slug = {t['slug']: t for t in TEAM}
        figs = ''.join(f'<figure class="dott" id="dott-{d["slug"]}"><img src="{P}assets/team/{d["slug"]}.jpg" alt="Ritratto di {esc(d["targa"])}" width="500" height="500" loading="lazy" decoding="async">'
                       f'<figcaption><span class="dott-targhetta"><span class="dott-nome">{esc(d["targa"])}</span><span class="dott-anno">{esc(d["anno"])}</span></span>'
                       f'<span class="dott-testo">{esc(per_slug[d["slug"]]["long" if long else "short"])}</span></figcaption></figure>' for d in DOTTORI)
        return f'<div class="dottori">{figs}</div>'
    cards = ''.join(f'<article class="team-card">{portrait(P, t)}<h3>{esc(t["name"])}</h3><p class="role">Odontoiatra</p><p>{esc(t["long" if long else "short"])}</p></article>' for t in TEAM)
    return f'<div class="team-grid">{cards}</div>'

def assist_row(center=True):
    return ('<div class="assist-row' + (' center' if center else '') + '">'
            '<div class="assist-item"><div class="avatar" aria-hidden="true">D</div><div><strong>Daniela</strong><span>Assistente alla poltrona</span></div></div>'
            '<div class="assist-item"><div class="avatar" aria-hidden="true">T</div><div><strong>Tonina</strong><span>Assistente alla poltrona</span></div></div></div>')

def home():
    P = ''
    main = (ingresso(P) + situazioni(P) + famiglia(P) + prima_visita_home(P) +
            trattamenti_home(P) + dove_siamo(P))
    desc = 'Dentista a Patti (ME): Studio Dentistico Colombo, tre dentisti di famiglia. Igiene, impianti, endodonzia, ortodonzia e cure per bambini. Prenota la tua visita.'
    d = dentist_full(); d['hasMap'] = 'https://www.google.com/maps/search/?api=1&query=Studio+Dentistico+Colombo+Patti+ME'
    ld = [d, website_ld(),
          {"@context": "https://schema.org", "@type": "WebPage", "@id": SITE_URL + "/#home", "url": SITE_URL + "/", "name": 'Dentista a Patti (ME) | Studio Dentistico Colombo', "description": desc,
           "inLanguage": "it-IT", "isPartOf": {"@id": SITE_URL + "/#sito"}, "about": {"@id": SITE_URL + "/#studio"}, "primaryImageOfPage": SITE_URL + "/assets/og-cover.jpg"}]
    return dict(path='', title='Dentista a Patti (ME) | Studio Dentistico Colombo', desc=desc, nav='home', main=main, ld=ld, world='ingresso')

# =========================================================== HUB TRATTAMENTI ===
def hub_servizi():
    P = ''
    groups = ''
    for g in GROUPS:
        cards = ''
        for s in g['services']:
            sc_links = ''.join(f'<a href="{P}schede/{x}.html" data-scheda-open="{x}" data-scheda-title="{esc(SCHEDE_BY_SLUG[x]["title"])}">{esc(SCHEDE_BY_SLUG[x]["short"])}</a>' for x in S[s]['schede'][:3])
            sc = f'<div class="hc-schede" aria-label="Schede collegate">{sc_links}</div>' if sc_links else ''
            cards += (f'<article class="hub-card" data-anim="iris"><span class="icon">{S[s]["icon"]}</span><h3><a href="{P}servizi/{s}.html">{esc(S[s]["name"])}</a></h3><p>{esc(BLURB[s])}</p>{sc}</article>')
        groups += (f'<section class="hub-group" aria-label="{esc(g["name"])}"><div class="hub-group-head"><h2 data-split>{esc(g["name"])}</h2><p>{esc(g["blurb"])}</p></div>'
                   f'<div class="link-cards" data-scheda-set>{cards}</div></section>')
    hero_ = page_hero(P, [('Home', 'index.html'), ('Trattamenti', None)], 'I trattamenti dello studio',
                      'Dodici aree di cura, dalla prevenzione alla chirurgia, per adulti e bambini. Scegli quella che ti interessa: trovi come lavoriamo, quando serve e le schede da leggere.',
                      extra=f'<div class="btn-row" style="margin-top:var(--sp-5)"><button class="btn btn-secondary" type="button" data-open-search>{ICON["search"]}Cerca un trattamento</button><a class="btn btn-primary" href="{P}prenota.html">Prenota una visita</a></div>')
    main = (hero_ + section(groups, prev=None, tight=True) + section(cta_band(P, title='Non sai quale trattamento ti serve?', text='Capita spesso: con una visita lo capiamo insieme, senza impegno.'), prev='', tight=True))
    ld = [breadcrumb([('Home', ''), ('Trattamenti', 'servizi.html')]),
          {"@context": "https://schema.org", "@type": "CollectionPage", "@id": SITE_URL + "/servizi.html#pagina", "url": SITE_URL + "/servizi.html", "name": 'Trattamenti dentistici a Patti', "inLanguage": "it-IT",
           "isPartOf": {"@id": SITE_URL + "/#sito"}, "about": provider(),
           "mainEntity": {"@type": "ItemList", "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": S[s]['name'], "url": f"{SITE_URL}/servizi/{s}.html"} for i, s in enumerate(SERVICE_ORDER)]}}]
    return dict(path='servizi.html', title='Trattamenti dentistici a Patti (ME) | Studio Colombo',
                desc="Tutti i trattamenti dello Studio Dentistico Colombo a Patti: igiene, conservativa, endodonzia, parodontologia, implantologia, protesi, ortodonzia, estetica e pedodonzia.",
                nav='servizi', main=main, ld=ld)

# ============================================================ PAGINA TRATTAMENTO ===
HOW_ICONS = ['clock', 'shield', 'smile', 'info', 'check']

def service_page(slug):
    P = '../'
    s = S[slug]
    url = f'{SITE_URL}/servizi/{slug}.html'
    grp = next(g for g in GROUPS if slug in g['services'])
    schede = [SCHEDE_BY_SLUG[x] for x in s['schede']]
    chips = [grp['name'], 'Studio di famiglia a Patti'] + (['Con schede informative'] if schede else [])
    chips_html = ''.join(f'<span class="chip">{esc(c)}</span>' for c in chips)
    msg = f'Buongiorno, vorrei informazioni su: {s["name"]}.'
    rings = ('<svg class="rings" viewBox="-20 -20 340 340" aria-hidden="true">'
             '<g transform="rotate(150 150 150)"><circle class="r1" cx="150" cy="150" r="150"/></g>'
             '<g transform="rotate(-35 150 150)"><circle class="r2" cx="150" cy="150" r="124"/></g>'
             '<g transform="rotate(60 150 150)"><circle class="r3" cx="150" cy="150" r="98"/></g></svg>')
    hero_ = (f'<section class="page-hero"><div class="container">{crumbs([("Home", "index.html"), ("Trattamenti", "servizi.html"), (s["name"], None)], P)}'
             f'<div class="svc-hero-grid"><div><div class="testa"><h1>{esc(s["h1"])}</h1><p class="lead">{esc(s["lead"])}</p></div><div class="svc-chips">{chips_html}</div>'
             f'<div class="btn-row"><a class="btn btn-primary" href="{P}prenota.html">{ICON["calendar"]}Prenota una visita</a>{wa_icon_btn(P, "Scrivici su WhatsApp", msg)}</div></div>'
             f'<div class="svc-visual" aria-hidden="true">{rings}<div class="badge">{s["icon"]}</div></div></div></div></section>')

    toc_items = [('cose', 'In cosa consiste'), ('quando', 'Quando serve'), ('come', 'Come lavoriamo')] + ([('schede', 'Schede')] if schede else []) + [('domande', 'Domande')]
    toc = '<div class="toc-title">In questa pagina</div>' + ''.join(f'<a href="#{i}">{t}</a>' for i, t in toc_items)
    toc_bar = '<nav class="toc-bar" aria-label="In questa pagina">' + ''.join(f'<a href="#{i}">{t}</a>' for i, t in toc_items) + '</nav>'

    about = ''.join(f'<p class="{"lead-p" if i == 0 else ""}">{esc(t)}</p>' for i, t in enumerate(s['about']))
    ticks = ''.join(f'<li>{ICON["check"]}<span>{rich(b)}</span></li>' for b in s['bullets'])
    signs = ''.join(f'<li>{ICON["check"]}<span>{esc(b)}</span></li>' for b in s['signs'])
    how = ''.join(f'<div class="how-card"><span class="hc-ico">{ICON[HOW_ICONS[i % len(HOW_ICONS)]]}</span><h3>{esc(t)}</h3><p>{esc(d)}</p></div>' for i, (t, d) in enumerate(s['how']))
    sec_cose = f'<section class="svc-sec" id="cose"><h2 data-split data-smile>In cosa consiste</h2><div class="prose">{about}</div><p class="mini-h">Di cosa ci occupiamo</p><ul class="tick-list">{ticks}</ul></section>'
    sec_quando = f'<section class="svc-sec" id="quando"><h2 data-split data-smile>Quando conviene farsi visitare</h2><div class="prose"><p>Potresti aver bisogno di questo trattamento se ti riconosci in una di queste situazioni.</p></div><ul class="tick-list signs">{signs}</ul></section>'
    sec_come = f'<section class="svc-sec" id="come"><h2 data-split data-smile>Come lavoriamo</h2><div class="how-grid">{how}</div></section>'
    sec_sch = ''
    if schede:
        cards = ''.join(scheda_card(x, P, area=False) for x in schede)
        sec_sch = (f'<section class="svc-sec" id="schede"><div class="schede-box" data-scheda-set><h2 data-split data-smile>Le schede informative</h2>'
                   f'<p class="sb-lead">Spiegazioni illustrate, passo per passo. Le puoi leggere con calma oppure le apriamo insieme, a tutto schermo, durante la visita: un tocco e si aprono.</p>'
                   f'<div class="scheda-grid">{cards}</div><p style="margin-top:var(--sp-5)"><a class="link-arrow" href="{P}schede.html">Tutte le schede informative {ICON["arrow"]}</a></p></div></section>')
    faqs = ''.join(faq_item(q, f'<p>{esc(a)}</p>') for q, a in s['faq'])
    sec_faq = f'<section class="svc-sec" id="domande"><h2 data-split data-smile>Domande frequenti</h2><div class="faq-list">{faqs}</div>' \
              f'<div class="note-box">{ICON["info"]}<p>Le informazioni di questa pagina sono generali e non sostituiscono una visita: il piano di cura dipende sempre dal tuo caso.</p></div></section>'

    doc = DOCTOR_NOTE.get(slug)
    contatto = (f'<div class="aside-citofono"><h3>Vuoi parlarne con noi?</h3><p>Una visita ti dà una risposta per il tuo caso. Chiamaci, scrivici o prenota.</p>'
                f'<p class="targa-stato" data-plate-status hidden><i class="stato-punto" aria-hidden="true"></i><b data-plate-label></b> <span data-plate-detail></span></p>'
                f'{citofono(P)}</div>')
    aside = ((f'<aside class="svc-aside">{contatto}' if mondo() == 'ingresso' else f'<aside class="svc-aside"><div class="book-card"><h3>Vuoi parlarne con noi?</h3><p>Una visita ti dà una risposta per il tuo caso. Prenota o scrivici.</p>'
             f'<a class="btn btn-primary btn-block" href="{P}prenota.html">Prenota una visita</a>'
             f'<a class="btn btn-secondary btn-block" href="tel:{PHONE_HREF}" data-tel>{ICON["phone"]}Chiama {PHONE}</a>'
             f'{wa_icon_btn(P, "WhatsApp", msg).replace("btn btn-whatsapp", "btn btn-whatsapp btn-block")}'
             f'<div class="bc-status"><span data-open-status>{HOURS_SHORT}</span></div></div>')
             + (f'<div class="aside-note">{esc(doc)}</div>' if doc else '')
             + f'<div class="aside-note">Vuoi vedere come si svolge una visita? <a href="{P}prima-visita.html">Leggi la prima visita</a>.</div></aside>')
    layout = f'{toc_bar}<div class="svc-layout"><nav class="toc" aria-label="In questa pagina">{toc}</nav><div class="svc-main">{sec_cose}{sec_quando}{sec_come}{sec_sch}{sec_faq}</div>{aside}</div>'

    rel = ''.join(f'<a class="service-link-card" href="{P}servizi/{r}.html" data-anim="iris"><span class="icon">{S[r]["icon"]}</span><h3>{esc(S[r]["name"])}</h3><p>{esc(BLURB[r])}</p><span class="more">Scopri di più {ICON["arrow"]}</span></a>' for r in s['related'])
    related = head_block('Per approfondire', 'Trattamenti collegati') + f'<div class="link-cards">{rel}</div>'

    main = (hero_ + section(layout, prev=None, tight=True) + section(related, bg='bg-alt', prev='') +
            section(cta_band(P, title=f'Parliamone in una visita.', text='Ti spieghiamo cosa è possibile fare nel tuo caso, con calma e senza impegno.', msg=msg), prev='bg-alt', bg='', tight=True))
    ld = [breadcrumb([('Home', ''), ('Trattamenti', 'servizi.html'), (s['name'], f'servizi/{slug}.html')]),
          {"@context": "https://schema.org", "@type": "Service", "@id": url + "#servizio", "url": url, "name": s['name'], "serviceType": s['name'], "description": s['seo_desc'],
           "provider": provider(), "areaServed": [{"@type": "City", "name": "Patti"}, {"@type": "AdministrativeArea", "name": "Provincia di Messina"}],
           "audience": {"@type": "PeopleAudience", "audienceType": "Pazienti adulti e bambini"}},
          faq_ld([(q, a) for q, a in s['faq']])]
    return dict(path=f'servizi/{slug}.html', P=P, title=s['seo_title'], desc=s['seo_desc'], nav='servizi', main=main, ld=ld, footer_prev='var(--paper)')

# ================================================================ HUB SCHEDE ===
def hub_schede():
    P = ''
    pills = '<button class="fpill" type="button" data-f-cat="all" aria-pressed="true">Tutte</button>' + ''.join(
        f'<button class="fpill" type="button" data-f-cat="{k}" aria-pressed="false">{esc(v)}</button>' for k, v in AREAS)
    cards = ''.join(scheda_card(sc, P) for sc in SCHEDE)
    howto = ''.join(f'<div class="ht"><span class="hc-ico">{ICON[i]}</span><div><h2 class="as-h3">{esc(t)}</h2><p>{esc(p)}</p></div></div>' for i, t, p in [
        ('file', 'Leggila con calma', 'Ogni scheda spiega il trattamento passo per passo: a cosa serve, come si svolge, quanto dura, quali sono i rischi e cosa fare dopo.'),
        ('screen', 'Guardala insieme a noi', 'In studio possiamo aprire la scheda a tutto schermo e vederla insieme, per rispondere ai tuoi dubbi mentre la leggi.'),
        ('qr', 'Portala con te', 'Ogni scheda ha un link e un codice QR: puoi mandarla a un familiare o ritrovarla più tardi dal telefono.')])
    body = (f'<div class="how-to">{howto}</div><div style="height:var(--sp-7)"></div>'
            f'<div data-filter><div class="filter-bar"><div class="filter-pills" role="group" aria-label="Filtra per argomento">{pills}</div>'
            f'<label class="search-field">{ICON["search"]}<span class="visually-hidden">Cerca nelle schede</span><input type="search" data-f-search placeholder="Cerca una scheda…" autocomplete="off" enterkeyhint="search"></label></div>'
            f'<p class="text-soft" data-f-count aria-live="polite" style="margin:-.6rem 0 var(--sp-4);font-size:var(--small)">{len(SCHEDE)} risultati</p>'
            f'<div class="scheda-grid" data-scheda-set>{cards}</div>'
            f'<div class="empty-state" data-f-empty hidden><b>Nessuna scheda trovata</b>Prova con un’altra parola, per esempio «impianto», «sbiancamento» o «canalare».</div></div>'
            f'<div class="note-box">{ICON["info"]}<p>Le schede servono a capire un trattamento in generale e non sostituiscono la visita: il piano di cura dipende sempre dal tuo caso.</p></div>')
    hero_ = page_hero(P, [('Home', 'index.html'), ('Schede informative', None)], 'Schede informative per i pazienti',
                      'Dodici schede illustrate che spiegano i trattamenti in modo semplice. Da leggere a casa, da guardare insieme in studio, da condividere con chi vuoi.')
    main = hero_ + section(body, prev=None, tight=True) + section(cta_band(P, title='Hai letto una scheda e hai dei dubbi?', text='Scrivici o chiamaci: ne parliamo con calma.', msg='Buongiorno, ho letto una scheda sul vostro sito e vorrei qualche informazione.'), prev='', tight=True)
    ld = [breadcrumb([('Home', ''), ('Schede informative', 'schede.html')]),
          {"@context": "https://schema.org", "@type": "CollectionPage", "@id": SITE_URL + "/schede.html#pagina", "url": SITE_URL + "/schede.html", "name": 'Schede informative per i pazienti', "inLanguage": "it-IT",
           "isPartOf": {"@id": SITE_URL + "/#sito"}, "publisher": provider(),
           "mainEntity": {"@type": "ItemList", "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": sc['title'], "url": f"{SITE_URL}/schede/{sc['slug']}.html"} for i, sc in enumerate(SCHEDE)]}}]
    return dict(path='schede.html', title='Schede informative sui trattamenti dentali | Studio Colombo Patti',
                desc="Schede illustrate per capire impianti, protesi, cura canalare, faccette, sbiancamento e igiene. Da leggere, mostrare in studio o condividere. Studio Dentistico Colombo, Patti.",
                nav='schede', main=main, ld=ld)

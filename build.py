#!/usr/bin/env python3
"""
Builds the "Journey Home" site per the full spec: Home / The Golu Story /
Journey Home / Divine Name Collection / Audio Guides / About & Acknowledgements.
Divine Name pages use pretty folder URLs: /divine-names/<slug>/
"""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
NAMES_DIR = os.path.join(ROOT, "divine-names")
JOURNEY_DIR = os.path.join(ROOT, "journey-home")
os.makedirs(NAMES_DIR, exist_ok=True)
os.makedirs(JOURNEY_DIR, exist_ok=True)

GOPURAM_SVG = """
<svg class="gopuram" viewBox="0 0 700 130" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Temple gopuram silhouette">
  <defs>
    <linearGradient id="goldGrad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#e6c765"/>
      <stop offset="100%" stop-color="#c9a227"/>
    </linearGradient>
  </defs>
  <g fill="url(#goldGrad)" opacity="0.9">
    <rect x="0" y="118" width="700" height="2"/>
    <polygon points="350,10 300,60 400,60"/>
    <rect x="320" y="55" width="60" height="14"/>
    <polygon points="350,26 330,52 370,52"/>
    <rect x="230" y="70" width="40" height="48"/>
    <polygon points="250,50 232,72 268,72"/>
    <rect x="430" y="70" width="40" height="48"/>
    <polygon points="450,50 432,72 468,72"/>
    <rect x="120" y="86" width="30" height="32"/>
    <polygon points="135,70 122,88 148,88"/>
    <rect x="550" y="86" width="30" height="32"/>
    <polygon points="565,70 552,88 578,88"/>
    <circle cx="350" cy="20" r="4"/>
  </g>
</svg>
"""

NAV_ITEMS = [
    ("home", "Home", "/index.html"),
    ("golu-story", "The Golu Story", "/golu-story.html"),
    ("tour", "Virtual Tour", "/virtual-tour.html"),
    ("journey", "Journey Home", "/journey-home/index.html"),
    ("malai", "Malai Nadu Divya Desam", "/malai-nadu/index.html"),
    ("names", "Divine Name Collection", "/divine-names/index.html"),
    ("audio", "Audio Guides", "/audio-guides.html"),
    ("about", "About & Acknowledgements", "/about.html"),
]

def depth_prefix(depth):
    return "../" * depth

def masthead(active, depth):
    p = depth_prefix(depth)
    links = "\n  ".join(
        f'<a href="{p}{path.lstrip("/")}"{" aria-current=\"page\"" if key==active else ""}>{label}</a>'
        for key, label, path in NAV_ITEMS
    )
    return f"""
<header class="masthead">
  {GOPURAM_SVG}
  <p class="eyebrow">Navaratri Golu 2026 &middot; Journey Home</p>
  <h1>The Journey Home</h1>
  <p class="tagline">The soul&rsquo;s journey to the lotus feet of Sriman Narayana</p>
</header>
<nav class="primary">
  {links}
</nav>
<hr class="divider"/>
"""

def footer(depth):
    return """
<footer class="site">
  <p>A humble family kainkaryam presenting the timeless teachings of our &Acirc;ch&amacr;ryas through art, technology, and storytelling.</p>
  <p>Inspired by the teachings of Dr. Venkatesh Swamin &middot; &copy; 2026 Golu Journey Home Project</p>
</footer>
"""

def page(title, active, body, depth=0, description=None):
    p = depth_prefix(depth)
    desc = description or "The Journey Home — a Navaratri Golu 2026 exhibition sharing the divine names of Sriman Narayana through story, based on the teachings of Dr. Venkatesh Swamin."
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="stylesheet" href="{p}assets/style.css">
</head>
<body>
<div class="wrap">
{masthead(active, depth)}
{body}
{footer(depth)}
</div>
</body>
</html>"""

# ------------------------------------------------------------------
# DATA
# ------------------------------------------------------------------

CHAPTERS = [
    dict(num=1, title="The Supreme Lord", desc="Who is Sriman Narayana?", range=(1, 9)),
    dict(num=2, title="The Compassionate Lord", desc="His compassion and divine initiative.", range=(10, 18)),
    dict(num=3, title="The Protector", desc="Avat\u0101ras, protection, and bhakta-rak\u1e63a\u1e47a.", range=(19, 27)),
    dict(num=4, title="The Guide", desc="Prapatti, \u015aara\u1e47\u0101gati, and the spirit of Gadya Trayam.", range=(28, 36)),
    dict(num=5, title="The Bestower of Grace", desc="Vishnu Dhootas, guidance, and the Archir\u0101di M\u0101rgam.", range=(37, 45)),
    dict(num=6, title="The Journey Home", desc="Paramapadam, bliss, and eternal kainkaryam.", range=(46, 54)),
]

def chapter_for(num):
    for c in CHAPTERS:
        if c["range"][0] <= num <= c["range"][1]:
            return c
    return None

def pathram_code(num):
    c = chapter_for(num)
    seq = num - c["range"][0] + 1
    return f"JH-{c['num']}.{seq:02d}"

DIVINE_NAMES = [
    dict(
        num=1, slug="visvam",
        deva="विश्वम्", tamil="விஶ்வம்", iast="Vi\u015bvam",
        meaning="The One who is completely whole \u2014 perfect in nature, form, and every quality.",
        story="""<p>Dr. Venkatesh tells of Na\u1e5bcelvan, a cowherd of \u0100yarp\u0101\u1e0di so devoted to K\u1e5b\u1e63\u1e47a's service
that he forgot even to milk his own cows. Moved by her calf's hunger, the mother buffalo let her
milk flow on its own \u2014 so abundantly that it ran like a stream through the house, day after day.</p>
<p>When villagers asked the sage Garga \u0100c\u0101rya how wealth could possibly remain in a house where milk
was flowing away like this, he explained: K\u1e5b\u1e63\u1e47a carries the name <em>Vi\u015bvam</em> because He Himself
is completely whole and lacking nothing \u2014 in His nature, form, and every quality. And because He is
whole, He makes His devotees whole too, filling them completely \u2014 from ordinary worldly wealth to
the highest wealth of bhakti and j\u00f1\u0101na.</p>""",
        teaching="<em>Vi\u015bvam</em> means being completely whole (<em>parip\u016br\u1e47a</em>) in <em>svabh\u0101va</em> (nature), <em>sv\u0101r\u016bpa</em> (form), and every gu\u1e47a (quality) \u2014 nothing lacking in any respect. Because Perum\u0101\u1e37 is Himself entirely whole, He extends that same fullness to any devotee who draws near Him, granting complete wealth in every sense \u2014 from ordinary worldly wealth to the highest wealth of bhakti and j\u00f1\u0101na. Nothing He gives is ever partial, because nothing in Him is ever partial.",
        living="When we serve without calculating what we'll get in return, the Lord ensures nothing we truly need is lacking.",
        reflection="Do one act of service today without keeping track of what comes back.",
        mantra="Om Vi\u015bv\u0101ya Nama\u1e25a",
        connection="As the exhibition opens with the soul's journey home, Vi\u015bvam reminds us the One we're journeying toward is already complete \u2014 the fullness we seek was never missing on His side.",
    ),
    dict(
        num=2, slug="vishnu",
        deva="विष्णुः", tamil="விஷ்ணு:", iast="Vi\u1e63\u1e47u\u1e25",
        meaning="The One who enters and fills everything \u2014 the universe is His body, and He dwells within it as the Self.",
        story="""<p>Dr. Venkatesh tells of the cardamom milk (<em>\u0113lakk\u0101i p\u0101l</em>) \u2014 a delicacy K\u1e5b\u1e63\u1e47a had
never stolen before, so curiosity got the better of Him. He sneaks into the gopi Pu\u1e63\u1e6dimati's house
to taste it, is caught, and struck on the back with a cane.</p>
<p>But it is not K\u1e5b\u1e63\u1e47a who cries out in pain \u2014 it is the very woman who struck Him, along with every
being in creation, from an ant to the celestials to Brahm\u0101 himself in Satyaloka. As Pi\u1e37\u1e37ai Perum\u0101\u1e37
Aiya\u1e45g\u0101r's verse puts it, when she struck Him, all fourteen worlds shook with the blow. The reason:
the entire universe and every being in it is His body, and He is the soul residing within. The name
Vi\u1e63\u1e47u comes from the root <em>vi\u1e63</em> \u2014 to enter \u2014 the One who enters and completely fills every
single thing, everywhere.</p>""",
        teaching="The word <em>Vi\u1e63\u1e47u</em> comes from the root <em>vi\u1e63</em>, to enter and pervade completely. Because the entire universe and every being within it is His body, and He dwells inside as the indwelling Self (antar\u0101tm\u0101), nothing and no one stands truly outside Him. Dr. Venkatesh draws out the implication directly: separation from another being is, at the deepest level, an illusion \u2014 even someone we consider an enemy shares the same indwelling Lord we do.",
        living="Remembering this dissolves hatred and conflict \u2014 we're never truly separate from the one we're upset with.",
        reflection="Notice one moment of irritation today, and remember He dwells in them too.",
        mantra="Om Vi\u1e63\u1e47ave Nama\u1e25a",
        connection="The Archir\u0101dhi M\u0101rga is only possible because the Lord already pervades every step of the path \u2014 the soul never truly travels away from Him.",
    ),
    dict(
        num=3, slug="vasatkarah",
        deva="वषट्कारः", tamil="வஷட்காரஹ​", iast="Va\u1e63a\u1e6dk\u0101ra\u1e25a",
        meaning="The Internal Controller \u2014 the One who directs every being from within.",
        story="""<p>Dr. Venkatesh tells of K\u1e5b\u1e63\u1e47a going as the P\u0101\u1e47\u1e0davas' messenger to Duryodhana's court.
Dismissing K\u1e5b\u1e63\u1e47a as "just a cowherd," Duryodhana orders his courtiers not to rise when He enters.
Yet the moment K\u1e5b\u1e63\u1e47a steps into the hall, everyone rises \u2014 even Duryodhana's own loyalists, Kar\u1e47a
and \u015aakuni.</p>
<p>Furious, Duryodhana demands to know why Kar\u1e47a disobeyed him. Kar\u1e47a simply tells him to look at his
own position \u2014 Duryodhana himself had risen first, without even realizing it, and everyone else had
merely followed their king. K\u1e5b\u1e63\u1e47a, as the indwelling controller within every being \u2014 including the
very man plotting to insult Him \u2014 had made even Duryodhana rise involuntarily.</p>""",
        teaching="<em>Va\u1e63a\u1e6dk\u0101ra\u1e25a</em> means the Controller who directs every being from within \u2014 not from outside, issuing visible commands, but from inside each person's own will and impulse. Even Duryodhana, actively plotting to insult K\u1e5b\u1e63\u1e47a, was moved by that same inner Controller to rise in respect without ever realizing it. Dr. Venkatesh's point: the Lord's control operates so intimately that we often mistake His direction for our own free choice.",
        living="This brings humility when things go well, and trust rather than despair when they don't.",
        reflection="Notice one small decision today, and quietly acknowledge the inner Guide behind it.",
        mantra="Om Va\u1e63a\u1e6dk\u0101r\u0101ya Nama\u1e25a",
        connection="The same inner Controller who guided Duryodhana without his knowing is the One who will guide the soul's journey along the Archir\u0101dhi M\u0101rga.",
    ),
    dict(
        num=4, slug="bhutabhavyabhavatprabhuh",
        deva="भूतभव्यभवत्प्रभुः", tamil="பூதபவ்யபவத்ப்ரபு:", iast="Bh\u016btabhavyabhavatprabhu\u1e25",
        meaning="The Master of the past, the present, and the future.",
        story="""<p>Dr. Venkatesh tells of the sage Roma\u015ba, whose body was covered in bear-like hair. Roma\u015ba
asked an astrologer for a life longer than Brahm\u0101's \u2014 not out of greed, but so he could visit and
savor every festival at each of the 108 Divya De\u015bams unhurriedly, again and again, rather than
rushing through them as a checklist.</p>
<p>The astrologer told him only the Lord who rules past, present, and future could grant a boon
beyond time itself, and gave him the mantra <em>Bh\u016bta Bhavya Bhavat Prabhave Nama\u1e25a</em> to recite
daily. Perum\u0101\u1e37 appeared and granted the boon: for every lifetime of Brahm\u0101 that passed, one hair
would fall from Roma\u015ba's body \u2014 and he would live until every hair had fallen.</p>""",
        teaching="<em>Bh\u016bta</em> means the past, <em>bhavya</em> the present, <em>bhavat</em> the future, and <em>prabhu</em> means master. Because He alone rules over all three divisions of time \u2014 yesterday, today, and tomorrow \u2014 only He can grant a boon that exceeds the limits time places on an ordinary lifetime, as He did for Roma\u015ba, whose lifespan was tied to every hair on his own body.",
        living="When we feel rushed to \u201cfinish\u201d our devotion like a checklist, this name reminds us the Lord who holds all time is never in a hurry either.",
        reflection="Slow down one routine act of devotion today, and let it be unhurried.",
        mantra="Om Bh\u016bta Bhavya Bhavat Prabhave Nama\u1e25a",
        connection="The soul's journey home is not a race \u2014 the Master of all three times welcomes the jivatma however long the path takes.",
    ),
    dict(
        num=5, slug="bhutakrit",
        deva="भूतकृत्", tamil="பூதக்ருத்", iast="Bh\u016btak\u1e5bt",
        meaning="The One who is, by Himself, all three causes behind creation.",
        story="""<p>Dr. Venkatesh tells of a conference on Kail\u0101\u015ba where sages ask \u015aiva how many causes the
universe has. Every ordinary object needs three: a material cause, a maker, and tools \u2014 a dosa
needs batter, a cook, and a griddle.</p>
<p>\u015aiva answers: for the universe as a whole, there is only one cause \u2014 N\u0101r\u0101ya\u1e47a alone. Like a spider
spinning its web from its own body, Perum\u0101\u1e37 is simultaneously the material, the maker, and the
means of the entire creation.</p>""",
        teaching="Every ordinary object needs three distinct causes: an <em>up\u0101d\u0101na k\u0101ra\u1e47a</em> (material cause \u2014 the dosa batter), a <em>nimitta k\u0101ra\u1e47a</em> (efficient cause, the maker \u2014 the cook), and a <em>sahak\u0101ri k\u0101ra\u1e47a</em> (instrumental cause \u2014 the griddle and tools). Dr. Venkatesh's answer to why the universe needs only one cause: like a spider that draws its web's material from its own body, is the web's maker, and uses its own body as the instrument, Perum\u0101\u1e37 alone is simultaneously the material, the maker, and the means of all creation. <em>K\u1e5bt</em> means the one who causes or creates.",
        living="Nothing we create is ever truly separate from us \u2014 in the same way, all creation remains inseparable from Him.",
        reflection="Notice one thing you made or grew today, and see your own hand in it as He sees His.",
        mantra="Om Bh\u016btak\u1e5bt\u0101ya Nama\u1e25a",
        connection="Since He is the source of all creation, the soul returning to Him is simply returning to its own origin.",
    ),
    dict(
        num=6, slug="bhutabhrit",
        deva="भूतभृत्", tamil="பூதப்ருத்", iast="Bh\u016btabh\u1e5bt",
        meaning="The One who feeds and sustains every being He has created.",
        story="""<p>Dr. Venkatesh tells of a poor devotee in Srirangam who, with a large family to feed, kept
asking for extra pras\u0101dam without offering any recitation in return \u2014 until temple staff turned him
away. R\u0101m\u0101nuja discovered he knew only the first six names of the Sahasran\u0101ma, and told him simply
to recite <em>Bh\u016btabh\u1e5bte Nama\u1e25a</em> daily \u2014 food would find him.</p>
<p>The man stopped coming to the temple, yet a portion of pras\u0101dam began mysteriously disappearing
each day. Investigation revealed it was being delivered to him by a servant introducing himself as
"Ra\u1e45gan\u0101than" \u2014 R\u0101m\u0101nuja's disciple. R\u0101m\u0101nuja realized Lord Ra\u1e45gan\u0101tha Himself had taken that
form, keeping His word to the humble devotee.</p>""",
        teaching="Dr. Venkatesh draws a direct line from the previous name: <em>Bh\u016btak\u1e5bt</em> (name 5) is the One who creates every being; <em>Bh\u016btabh\u1e5bt</em> (this name) is the One who continues to sustain and nourish what He created. <em>Bh\u1e5bt</em> means to bear, feed, or sustain. A poor devotee who knew only this name recited it daily, as R\u0101m\u0101nuja instructed \u2014 and pras\u0101dam began mysteriously reaching him each day, delivered by Lord Ra\u1e45gan\u0101tha Himself in disguise, proving the name's promise in the most literal way.",
        living="Even the smallest devotion, offered sincerely, is enough for the Lord to provide for what we truly need.",
        reflection="Recite this name once today, trusting that what you need will find you.",
        mantra="Om Bh\u016btabh\u1e5bte Nama\u1e25a",
        connection="Just as He sustained that devotee daily, He sustains the soul through every stage of the Archir\u0101dhi M\u0101rga.",
    ),
    dict(
        num=7, slug="bhavah",
        deva="भावः", tamil="பாவ:", iast="Bh\u0101va\u1e25",
        meaning="The One who unfurls all worlds from within Himself, like a peacock opening its tail.",
        story="""<p>Dr. Venkatesh continues the story of K\u1e5b\u1e63\u1e47a in Duryodhana's court: to trap K\u1e5b\u1e63\u1e47a,
Duryodhana had Him seated over a hidden pit of wrestlers, planning to drop Him in when the cloth
beneath the seat was pulled. When K\u1e5b\u1e63\u1e47a declares the P\u0101\u1e47\u1e0davas dearer to Him than His own life,
Duryodhana in fury has the cloth pulled \u2014 but instead of falling, K\u1e5b\u1e63\u1e47a reveals His Vi\u015bvar\u016bpa.</p>
<p>Every world and being, folded within Him, suddenly appears \u2014 just as a peacock's hidden beauty is
seen only once its tail unfurls. Because He brings forth all worlds from within Himself this way,
He is called <em>Bh\u0101va\u1e25</em>.</p>""",
        teaching="Dr. Venkatesh explains this name through the image of a peacock's tail: folded, it looks ordinary, but unfurled, all its intrinsic beauty is suddenly visible. Before creation, all the worlds exist folded and compact within Perum\u0101\u1e37, just as the peacock's feathers exist compact before opening. At the moment of creation \u2014 and, as this story shows, whenever He chooses \u2014 He unfurls what was always folded within Him, and the worlds spring forth. <em>Bh\u0101va\u1e25</em> means the One who causes all worlds to arise, or unfold, from Himself.",
        living="What looks ordinary and folded-up in us may hold beauty and vastness we haven't yet shown the world.",
        reflection="Let one hidden part of yourself show today, rather than staying folded away.",
        mantra="Om Bh\u0101v\u0101ya Nama\u1e25a",
        connection="The vastness Perum\u0101\u1e37 revealed to Duryodhana is the same vastness the soul beholds on reaching Paramapadam.",
    ),
    dict(
        num=8, slug="bhutatma",
        deva="भूतात्मा", tamil="பூதாத்மா", iast="Bh\u016bt\u0101tm\u0101",
        meaning="The Self who dwells within every created being and thing.",
        story="""<p>Dr. Venkatesh tells of King Janaka's great assembly, where the sage Y\u0101j\u00f1avalkya answers
every question put to him by rival sages, winning the prize of 500 cows. Finally, the sage Udd\u0101laka
asks the decisive question: "Who dwells within and supports all beings and all things?"</p>
<p>Y\u0101j\u00f1avalkya answers: N\u0101r\u0101ya\u1e47a \u2014 dwelling within the earth, the sky, and every element as their
inner support, unknown to them, yet essential to their existence. Because all creation is His body,
he explains, harm in one place is felt elsewhere: cut down the earth's trees, and the sky withholds
rain; overbuild the land, and the sea rises in anger. Every individual soul, too, is His body, with
Him dwelling as its innermost Self.</p>""",
        teaching="<em>Bh\u016bta</em> here means all created things; <em>\u0101tm\u0101</em> means the indwelling soul. Because every element \u2014 earth, water, fire, air, sky \u2014 and every jiv\u0101tma is His body, Dr. Venkatesh explains a striking consequence: harm done to one part of that body is felt in another. Cut down the earth's trees, and the sky withholds its rain in anger; overbuild the land, and the sea rises in anger and sends a tsunami \u2014 because both land and sea are the same body, His body, and a strike on one part is felt in the other.",
        living="Since all creation is His body, harm done in one place is felt elsewhere \u2014 a reminder that nothing we do is ever truly isolated.",
        reflection="Today, treat one part of the natural world around you as part of His body.",
        mantra="Om Bh\u016bt\u0101tmane Nama\u1e25a",
        connection="The jiv\u0101tma making the journey home is itself a body to Him \u2014 the same closeness Y\u0101j\u00f1avalkya described is what welcomes the soul at every stage.",
    ),
    dict(
        num=9, slug="bhutabhavanah",
        deva="भूतभावनः", tamil="பூத பாவன:", iast="Bh\u016btabh\u0101vana\u1e25",
        meaning="The One who not only gives life to every being, but personally nourishes them.",
        story="""<p>Dr. Venkatesh tells of Thiruma\u1e37i\u015bai \u0100\u1e37v\u0101r, who walked from Madras to Kumbakonam under
the harsh Panguni sun to worship \u0100r\u0101vamud\u0101\u1e37v\u0101r. Arriving exhausted at noon, right as sweet pongal
was being offered inside, Perum\u0101\u1e37 instructed the priest to serve the pongal to the tired, hungry
\u0100\u1e37v\u0101r first \u2014 before He Himself partook.</p>
<p>The \u0100\u1e37v\u0101r protested \u2014 a devotee eats only the Lord's leftover pras\u0101dam, never before Him. Perum\u0101\u1e37
explained: just as a hungry body must be fed by the soul within it, He is the soul within every
being, and when the \u0100\u1e37v\u0101r's body was hungry, He as the indwelling Self felt that hunger as His own.
So Perum\u0101\u1e37 fed the body with pongal, and the \u0100\u1e37v\u0101r's soul with the sight of His own beauty \u2014 both
hungers satisfied at once. In honor of this, the devotee came to be called "Thirumazhisai Pir\u0101\u1e47"
(Master), and Perum\u0101\u1e37 came to be called "\u0100r\u0101vamud\u0101\u1e37v\u0101\u1e47" (devotee) \u2014 a loving reversal of roles.</p>""",
        teaching="Perum\u0101\u1e37 Himself explains this name in the story: just as a hungry body depends on its indwelling soul to seek out food for it, He is the soul within every being \u2014 so when the \u0100\u1e37v\u0101r's body grew hungry, He as the indwelling Self felt that hunger as His own and moved to satisfy it, feeding both body (with the pongal) and soul (with the sight of His own beauty) at once. <em>Bh\u0101vana</em> means the One who nurtures and nourishes \u2014 going beyond simply giving life (as in Bh\u016btak\u1e5bt, name 5) to actively caring for what that life needs to flourish.",
        living="The Lord doesn't just sustain us from a distance \u2014 He feels our need as His own and moves to meet it before we've asked.",
        reflection="Today, offer food or care to someone else first, before yourself.",
        mantra="Om Bh\u016bta Bh\u0101van\u0101ya Nama\u1e25a",
        connection="This closes Chapter 1 the way the Journey Home begins \u2014 with a Lord who does not wait to be asked before caring for the one who seeks Him.",
    ),
    dict(
        num=10, slug="putatma",
        deva="पूतात्मा", tamil="பூதாத்மா", iast="P\u016bt\u0101tm\u0101",
        meaning="The Pure Self who purifies whatever is offered to Him.",
        story="""<p>Dr. Venkatesh tells the story behind Uppiliappan Kovil, near Kumbakonam. Perum\u0101\u1e37 once
promised to accept only unsalted offerings there, and kept that word so seriously that even today,
every pras\u0101dam offered to Uppiliappan is prepared entirely without salt.</p>
<p>By Tamil proverb, food without salt belongs in the rubbish \u2014 tasteless, incomplete. Yet Dr.
Venkatesh explains that because Uppiliappan is Himself <em>P\u016bt\u0101tm\u0101</em>, the Pure Self, He makes even
this saltless offering into something sweeter than nectar for those who partake of it. Purity, not
richness, is what transforms the offering.</p>""",
        teaching="<em>P\u016bta</em> means pure; <em>\u0101tm\u0101</em> means self. Because Perum\u0101\u1e37 is Himself pure by nature, He purifies and elevates whatever touches Him or is offered to Him \u2014 even something as plain and \u201cincomplete\u201d as unsalted food becomes, in His hands, more delicious than amuta (nectar). The name teaches that it is His purity acting on the offering, not the offering's own richness, that makes it sacred.",
        living="What matters isn't the richness of what we offer, but the purity of heart behind it.",
        reflection="Offer one small, humble thing today, without worrying whether it's \u201cenough.\u201d",
        mantra="Om P\u016bt\u0101tmane Nama\u1e25a",
        connection="Just as Uppiliappan purifies even a saltless offering, the soul's own imperfect offerings are made pure and worthy on the journey home.",
    ),
    dict(
        num=11, slug="paramatma",
        deva="परमात्मा", tamil="பரமாத்மா", iast="Param\u0101tm\u0101",
        meaning="The Supreme Self, who needs no support beyond Himself, yet supports every soul.",
        story="""<p>Dr. Venkatesh tells of Nārada visiting Badrin\u0101th, where Badrin\u0101r\u0101ya\u1e47a sits in
meditative yogic stillness. Curious who the Lord of the universe could possibly be meditating on,
Nārada asks directly. Perum\u0101\u1e37 sends him across seven seas to \u015aveta Dv\u012bpa, where the people, when
asked, say they meditate on none other than Badrin\u0101r\u0101ya\u1e47a Himself.</p>
<p>Confused, Nārada returns for an answer. Perum\u0101\u1e37 smiles: "I meditate on Myself. You, as j\u012bv\u0101tmas,
may meditate on Me as the indwelling Self within you. But there is no one above Me to be My own
support \u2014 so I am My own support, and I meditate on Myself." This story appears in the Mah\u0101bh\u0101rata's
\u015a\u0101nti Parva.</p>""",
        teaching="Because Perum\u0101\u1e37 is the support (\u0101dh\u0101ra) for every soul, yet has no support above Himself \u2014 unlike every j\u012bv\u0101tma, who depends on Him as antary\u0101m\u012b \u2014 He is <em>Param\u0101tm\u0101</em>, the Supreme Self. Everything that exists ultimately rests on Him; He alone rests on nothing but Himself.",
        living="Everything we rely on ultimately rests on Him \u2014 while He alone rests on nothing but Himself.",
        reflection="Today, notice one thing you're leaning on, and trace it back to its true support.",
        mantra="Om Param\u0101tmane Nama\u1e25a",
        connection="As the soul travels toward Him, it travels toward the one Support that needs no support of its own \u2014 the final resting place at the end of every dependency.",
    ),
    dict(
        num=12, slug="muktanam-parama-gatih",
        deva="मुक्तानां परमा गतिः", tamil="முக்தானாம் பரமா கதி:", iast="Mukt\u0101n\u0101\u1e43 Param\u0101 Gati\u1e25",
        meaning="The One whom liberated souls consider their highest goal \u2014 eternal service to Him.",
        story="""<p>Dr. Venkatesh tells of R\u0101ma, departing for exile, refusing to let S\u012bt\u0101 accompany him onto
thorned forest paths. S\u012bt\u0101 poses a test question first: define heaven and hell. When R\u0101ma gives the
conventional answer \u2014 Indra's world and Yama's world \u2014 S\u012bt\u0101 tells him he's entirely wrong: heaven
and hell mean something different to everyone. To her, she says simply, "Being with you is heaven;
being without you is hell." R\u0101ma relents and takes her.</p>
<p>Meanwhile, Lak\u1e63ma\u1e47a, who had waited outside, now performs \u015bara\u1e47\u0101gati at R\u0101ma's feet, begging to
serve him in exile. When R\u0101ma questions why he must come \u2014 the exile was Kaikeyi's curse on R\u0101ma
alone \u2014 Lak\u1e63ma\u1e47a explains: liberated souls in Vaiku\u1e47\u1e6dha long for the chance to serve R\u0101ma eternally
after death, but he has the rarer fortune of serving Him <em>right now, while still alive on earth</em> \u2014
and he refuses to let that chance slip by. R\u0101ma takes both S\u012bt\u0101 and Lak\u1e63ma\u1e47a with him.</p>""",
        teaching="Lak\u1e63ma\u1e47a's own words give this name its meaning: liberated souls (<em>mukt\u0101s</em>) regard eternal kaink\u0101ryam to the Lord in Vaiku\u1e47\u1e6dha as their supreme goal (<em>param\u0101 gati\u1e25</em>) \u2014 and Lak\u1e63ma\u1e47a realized he had the rarer chance to begin that very service while still living. What liberated souls wait for after death, he refused to postpone.",
        living="The highest goal isn't a distant reward reserved for later \u2014 it's the chance to serve Him today.",
        reflection="Find one small way to serve someone today, as if it were your highest goal.",
        mantra="Om Mukt\u0101n\u0101\u1e43 Param\u0101ya Gataye Nama\u1e25a",
        connection="This name names the very destination of the Journey Home itself \u2014 not a place, but an eternal, joyful service at His feet, which every liberated soul seeks above all else.",
    ),
    dict(
        num=13, slug="avyayah",
        deva="अव्ययः", tamil="அவ்யயஃ", iast="Avyaya\u1e25",
        meaning="The One who holds His devotees close and never lets them slip away.",
        story="""<p>Dr. Venkatesh tells of King Yay\u0101ti, whose many acts of charity earned him a seat in
heaven equal to Indra's own. Jealous, Indra schemes to bring him down: while celestial dancers
perform, he goads Yay\u0101ti into boasting about his own generosity. The moment Yay\u0101ti's pride peaks \u2014
claiming no one in the world has given more than him \u2014 he begins falling from his seat. Bṛhaspati
explains: the fall began the instant the pride did.</p>
<p>Yay\u0101ti lands in the yaj\u00f1a-hall of his own grandson, Pratardana, who explains that Indra acts this
way only out of jealousy toward anyone who becomes his equal \u2014 and that Yay\u0101ti should have sought
N\u0101r\u0101ya\u1e47a's feet instead. When Yay\u0101ti asks whether N\u0101r\u0101ya\u1e47a would cast him down too, Pratardana
answers: Perum\u0101\u1e37 has no such jealousy \u2014 He delights when His devotees become His equals in eight
divine qualities, and never pushes anyone away. Yay\u0101ti meditates on Perum\u0101\u1e37, practices bhakti
yoga, and attains mok\u1e63a \u2014 from where, as the Upani\u1e63ad says, none ever return.</p>""",
        teaching="<em>Vyaya</em> means to slip away or dissipate; <em>Avyaya\u1e25</em> means the One who does not let His devotees slip away \u2014 who holds them firmly within Himself. Unlike Indra, whose jealousy of an equal caused him to cast Yay\u0101ti down, Perum\u0101\u1e37 is delighted, not threatened, when His devotees rise toward becoming like Him, and He never lets go of anyone who reaches Him.",
        living="Growth and closeness to Him are never threats to Him \u2014 only causes for His joy.",
        reflection="Celebrate someone else's progress today without any hint of comparison.",
        mantra="Om Avyay\u0101ya Nama\u1e25a",
        connection="The soul making its way home can trust that once it reaches Him, unlike Yay\u0101ti in Indra's court, it will never be cast down or let slip away again.",
    ),
    dict(
        num=14, slug="purushah",
        deva="पुरुषः", tamil="புருஷஃ", iast="Puru\u1e63a\u1e25",
        meaning="The One who gives Himself entirely to those who love Him.",
        story="""<p>Dr. Venkatesh tells of R\u0101m\u0101nuja visiting the palace of the Sultan of Delhi to reclaim a
deity taken during a raid on Thirun\u0101r\u0101ya\u1e47apuram. Shown every looted idol, R\u0101m\u0101nuja calls out,
"Selvapill\u0101i v\u0101r\u0101i!" ("Come, my dear child!") to each, but none respond. Only one place remains
unchecked: the Sultan's young daughter, who plays in her chambers with what she believes is a doll.</p>
<p>Unable to enter the women's quarters, R\u0101m\u0101nuja calls from outside \u2014 and the deity runs straight
from the princess's lap into his. Reinstalling Him at Thirun\u0101r\u0101ya\u1e47apuram, R\u0101m\u0101nuja notices tears
during the consecration and asks why. Perum\u0101\u1e37 explains: the princess loved Him sincerely, whether
or not she knew Him as God or merely as a doll \u2014 and that love moved Him. R\u0101m\u0101nuja, understanding
her devotion, could not bear to separate them, and brought her too, consecrating her as "Bibi
N\u0101chiy\u0101r" between the deity's two feet, where she is honored to this day.</p>""",
        teaching="<em>Puru\u1e63a\u1e25</em> means the One who gives Himself entirely to those who love Him \u2014 Dr. Venkatesh notes the same root gives Tamil its word for husband (<em>puru\u1e63an</em>), one who gives himself wholly to his wife, keeping nothing back for himself. Just as Perum\u0101\u1e37 left the princess's lap the instant R\u0101m\u0101nuja called, and later refused to be separated from her devotion, He gives Himself completely to whoever truly loves Him \u2014 regardless of how imperfect or unknowing that love may be.",
        living="Love this genuine doesn't go unnoticed \u2014 it draws Him completely to us, however small or uninformed that love may seem.",
        reflection="Express one moment of genuine, uncalculated love today.",
        mantra="Om Puru\u1e63\u0101ya Nama\u1e25a",
        connection="The Journey Home ends not in distance but in total union \u2014 the same completeness with which He gave Himself to Bibi N\u0101chiy\u0101r awaits the soul that reaches Him.",
    ),
    dict(
        num=15, slug="sakshi",
        deva="साक्षी", tamil="ஸாக்ஷீ", iast="S\u0101k\u1e63\u012b",
        meaning="The Witness who watches over all beings as they play the game of life.",
        story="""<p>Dr. Venkatesh tells of sage Kalava, visiting Thentiruperai, who notices something unusual:
Garu\u1e0da's shrine here stands slightly apart from the sanctum, rather than directly in front as in
every other temple, where Garu\u1e0da normally serves as a mirror reflecting Perum\u0101\u1e37's beauty back to
Him.</p>
<p>Asked why, Garu\u1e0da explains: N\u0101mm\u0101\u1e37v\u0101r sang of this town's children, who are taught both
Sanskrit and Tamil Vedas from a young age. When they play the street game <em>sadugudu</em> right in
front of the temple, instead of the usual chant, they recite Vedic mantras and \u0100\u1e37v\u0101r p\u0101surams as
they play. Garu\u1e0da has stepped aside so Perum\u0101\u1e37 can watch, unobstructed, as these children play \u2014
delighting in the sight.</p>""",
        teaching="Dr. Venkatesh draws out the larger point: this game is not the only game. Life itself is the play Perum\u0101\u1e37 has set us all into \u2014 and just as He watches the Thentiruperai children play, delighted, He watches every one of us live out our lives according to the rules He has laid down in the \u015b\u0101stras, present as witness to it all. Because He watches over every being engaged in the play of life, He is <em>S\u0101k\u1e63\u012b</em>, the Witness.",
        living="Living well isn't about being unseen \u2014 it's remembering we're always watched, and delighted in, by the One who set the game.",
        reflection="Do one task today as if you knew He were watching with delight.",
        mantra="Om S\u0101k\u1e63i\u1e47e Nama\u1e25a",
        connection="Every step of the soul's journey home unfolds under His watching, delighted gaze \u2014 nothing on the path happens unseen or unaccompanied.",
    ),
    dict(
        num=16, slug="kshetrajnah",
        deva="क्षेत्रज्ञः", tamil="க்ஷேத்ரஜ்ஞஃ", iast="K\u1e63etraj\u00f1a\u1e25",
        meaning="The One who chooses the exact right place to grant complete grace.",
        story="""<p>Dr. Venkatesh tells of Vibh\u012b\u1e63a\u1e47a, gifted the deity Ra\u1e45gan\u0101tha by R\u0101ma after the coronation,
and granted the honor of nightly worship at Srirangam, where Perum\u0101\u1e37 chose to remain reclining
forever. One night, Vibh\u012b\u1e63a\u1e47a asks whether lying in the same pose eternally isn't tiresome, and
whether Perum\u0101\u1e37 might walk instead. Ra\u1e45gan\u0101tha agrees \u2014 but only at Thirukka\u1e47\u1e47apuram, on the east
coast, on the next Amāvāsya, not at Srirangam.</p>
<p>Puzzled why the two must be separate, Vibh\u012b\u1e63a\u1e47a goes anyway. At Thirukka\u1e47\u1e47apuram, Saurir\u0101ja
Perum\u0101\u1e37 walks for him, and Vibh\u012b\u1e63a\u1e47a is overcome \u2014 trembling, weeping, momentarily fainting. When he
recovers, he realizes: seeing Perum\u0101\u1e37 walk on this particular coast recalled the exact moment of his
own surrender to R\u0101ma at Thiruppu\u1e37\u1e37\u0101\u1e47i's shore, where R\u0101ma had walked toward him declaring refuge
to all who surrender even once. Had Perum\u0101\u1e37 walked at Srirangam instead, that specific memory would
never have surfaced \u2014 only this exact place could complete the experience.</p>""",
        teaching="<em>K\u1e63etram</em> means place; <em>K\u1e63etraj\u00f1a\u1e25</em> means the One who knows the right place. Dr. Venkatesh connects this directly to Thiruva\u1e37\u1e37uvar's teaching that no undertaking should begin without first understanding the right setting for it (<em>idam a\u1e5bithal</em>). Perum\u0101\u1e37 chose Srirangam for daily worship and Thirukka\u1e47\u1e47apuram specifically for revealing His walk \u2014 because only the second location would complete Vibh\u012b\u1e63a\u1e47a's grace with the fullest possible meaning.",
        living="Grace often arrives in a specific place or moment for a reason we don't yet see \u2014 the setting is never incidental to Him.",
        reflection="Notice today where you feel most drawn to Him, and honor that place.",
        mantra="Om K\u1e63etraj\u00f1\u0101ya Nama\u1e25a",
        connection="Just as He chose Thirukka\u1e47\u1e47apuram with precision for Vibh\u012b\u1e63a\u1e47a, He has chosen Paramapadam as the exact right destination for the soul's journey home.",
    ),
    dict(
        num=17, slug="aksharah",
        deva="अक्षरः", tamil="அக்ஷரஃ", iast="Ak\u1e63ara\u1e25",
        meaning="The One who never diminishes \u2014 an ever-constant, unfading light.",
        story="""<p>Dr. Venkatesh tells of Chandra (the Moon), married to all 27 daughters of Dak\u1e63a
Praj\u0101pati \u2014 the 27 nak\u1e63atras \u2014 who favors only Rohi\u1e47\u012b and neglects the rest. Enraged, Dak\u1e63a curses
Chandra with a wasting disease, and Chandra begins losing his kalas one by one \u2014 the origin of the
waning moon \u2014 until nothing remains at Am\u0101v\u0101sy\u0101.</p>
<p>Begging for release, Chandra points out to Dak\u1e63a that the curse harms Dak\u1e63a's own daughters too,
since they are bound to Chandra. Dak\u1e63a relents and directs him to Mayil\u0101duthurai (Thiruindal\u016br),
where Parimala Ra\u1e45gan\u0101than resides. Bathing in the temple's Indu Pu\u1e63kari\u1e47i tank and worshipping the
deity there, Chandra regains his kalas one by one \u2014 the waxing moon \u2014 until he shines full again.
\u0100\u1e37v\u0101r describes Perum\u0101\u1e37 here as a "nand\u0101 vilakku" \u2014 a lamp that never dims \u2014 in contrast to the very
moon He healed.</p>""",
        teaching="<em>K\u1e63aram</em> means to diminish or decay; <em>Ak\u1e63ara\u1e25</em> means without diminishment \u2014 ever full, never wanting. Having cured the Moon's own waning affliction, Perum\u0101\u1e37 Himself remains the opposite of what He healed: a constant, unwaning light, never subject to the cycles of increase and decrease that govern everything else in creation, including the very moon that bears His grace.",
        living="Where the world around us waxes and wanes, He remains completely, reliably constant.",
        reflection="Return today to one steady truth about Him when things around you feel uncertain.",
        mantra="Om Ak\u1e63ar\u0101ya Nama\u1e25a",
        connection="Where the journey itself has stages, phases, and changing light, the destination \u2014 Paramapadam, and the Lord who awaits there \u2014 never diminishes or changes.",
    ),
    dict(
        num=18, slug="yogah",
        deva="योगः", tamil="யோகஃ", iast="Yoga\u1e25",
        meaning="The One who Himself becomes the means to liberation for those who cannot walk any other path.",
        story="""<p>Dr. Venkatesh tells of Dadhipandan, a curd-seller in \u0100yarp\u0101\u1e0di who hides K\u1e5b\u1e63\u1e47a inside an
empty pot when Ya\u015bod\u0101 comes searching for him. After she leaves, K\u1e5b\u1e63\u1e47a asks to be released \u2014 but
Dadhipandan refuses without a boon in return: since K\u1e5b\u1e63\u1e47a frees souls from the cycle of birth,
Dadhipandan now demands his own release be conditional on K\u1e5b\u1e63\u1e47a granting liberation to both himself
<em>and the pot</em>.</p>
<p>K\u1e5b\u1e63\u1e47a agrees \u2014 and the instant He is freed, both Dadhipandan and his pot attain Vaiku\u1e47\u1e6dha. Word
spreads, and villagers ask the elder Garga \u0100c\u0101rya how a pot, or an unlearned man incapable of real
bhakti yoga, could reach mok\u1e63a without the prescribed spiritual practice. Garga \u0100c\u0101rya explains: since
neither could perform bhakti yoga themselves, K\u1e5b\u1e63\u1e47a placed Himself in the position of that very
practice \u2014 becoming the means (yoga) itself, and granting liberation directly.</p>""",
        teaching="<em>Yoga</em> means the means or method (<em>s\u0101dhanam</em>) by which something is attained. Dr. Venkatesh explains that though bhakti yoga is a genuine path to mok\u1e63a, it is difficult \u2014 and for those who cannot practice it, simple surrender is enough, because the Lord Himself becomes the path, the means, and the way there. Because He personally takes the place of the s\u0101dhanam for those who have none, He is called <em>Yoga\u1e25</em>.",
        living="We don't need to earn our way to Him through perfect practice \u2014 for those who cannot, He can become the way itself.",
        reflection="Let go of one thing today you've been trying to \u201cearn\u201d your way toward.",
        mantra="Om Yog\u0101ya Nama\u1e25a",
        connection="For a soul who cannot complete the journey home by its own effort or merit, this name is the promise that He Himself becomes the way there.",
    ),
    dict(
        num=19, slug="yogavidam-neta",
        deva="योगविदां नेता", tamil="யோகவிதாம் நேதா", iast="Yogavid\u0101\u1e43 Net\u0101",
        meaning="The Guide who leads seekers of liberation to the right path.",
        story="""<p>Dr. Venkatesh tells of a celebrated singer at Thirun\u0101r\u0101ya\u1e47apuram whose singing made
Perum\u0101\u1e37 Himself rise and dance \u2014 and who, proud of this, repeatedly disrespected R\u0101m\u0101nuja.
R\u0101m\u0101nuja's disciples ask the singer to put a question to Perum\u0101\u1e37 on their behalf: does R\u0101m\u0101nuja have
mok\u1e63a? Perum\u0101\u1e37 answers yes \u2014 to R\u0101m\u0101nuja and all his devotees.</p>
<p>Delighted, the singer relays this. The disciples then ask him to inquire about his own mok\u1e63a,
certain of a yes given how much Perum\u0101\u1e37 seems to enjoy his singing. Instead, Perum\u0101\u1e37 tells him
plainly: no amount of singing or worship satisfies Him the way devotion channeled through a true
\u0101c\u0101rya does \u2014 only by taking refuge at R\u0101m\u0101nuja's feet will he find mok\u1e63a. Humbled, the singer
becomes R\u0101m\u0101nuja's disciple, and through that guidance, attains liberation.</p>""",
        teaching="<em>Net\u0101</em> means guide \u2014 the same root that gives Subhas Chandra Bose his title \u201cNet\u0101ji,\u201d for guiding India's freedom struggle. Dr. Venkatesh explains that Perum\u0101\u1e37 Himself takes the role of guide for anyone seeking mok\u1e63a, pointing them not necessarily to Himself directly, but to the true \u0101c\u0101rya who can lead them there \u2014 as He did by redirecting the singer's pride toward R\u0101m\u0101nuja.",
        living="Talent or devotion alone doesn't guarantee the right path — sometimes even the most gifted among us need a guide to point the way.",
        reflection="Think of one person who has genuinely guided you, and thank them today.",
        mantra="Om Yogavid\u0101\u1e43 Netre Nama\u1e25a",
        connection="The Archir\u0101dhi M\u0101rga itself is a guided path \u2014 this name reminds us the soul is never left to find the way home alone.",
    ),
    dict(
        num=20, slug="pradhana-purushesvarah",
        deva="प्रधानपुरुषेश्वरः", tamil="பிரதான புருஷேஸ்வரஃ", iast="Pradh\u0101napuru\u1e63e\u015bvara\u1e25",
        meaning="The Lord who controls both sentient souls and insentient matter.",
        story="""<p>Dr. Venkatesh tells of five-year-old Dhruva, denied his father's lap by a jealous
stepmother who declared only her own son had that right. Devastated, Dhruva is told by his mother to
aim higher \u2014 to seek Nar\u0101ya\u1e47a's lap through tapas rather than settle for a father's. Guided by
N\u0101rada with the twelve-syllable V\u0101sudeva mantra, the boy performs such fierce penance that its heat
scorches the heavens.</p>
<p>Perum\u0101\u1e37 appears, touches Dhruva's cheek with His conch, and grants him wisdom. When Dhruva asks for
immediate mok\u1e63a in His lap, Perum\u0101\u1e37 tells him instead to return, become king, and eventually attain
the Dhruva (Pole Star) position before mok\u1e63a. Dhruva protests \u2014 his father and stepmother despise
him, kingship seems impossible. Perum\u0101\u1e37 explains: He alone controls both categories of existence,
sentient and insentient, and with His grace now granted, everything will turn favorable. Dhruva
returns home to find his stepmother welcoming him with \u0101rati and his father crowning him heir.</p>""",
        teaching="<em>Pradh\u0101nam</em> refers to insentient matter (<em>achetana</em>) \u2014 objects without awareness; <em>Puru\u1e63a\u1e25</em> refers to sentient souls (<em>chetana</em>) \u2014 beings with awareness, like us. Because Perum\u0101\u1e37, as \u012a\u015bvara, completely controls both categories \u2014 every object and every soul \u2014 He is <em>Pradh\u0101napuru\u1e63e\u015bvara\u1e25</em>. Once Dhruva had His grace, both categories turned in his favor at once: the people around him, and the circumstances themselves.",
        living="When we're aligned with Him, even the people and circumstances that once opposed us can turn in our favor \u2014 nothing is outside His reach.",
        reflection="Notice one circumstance that feels against you right now, and consider that it might still turn.",
        mantra="Om Pradh\u0101na Puru\u1e63e\u015bvar\u0101ya Nama\u1e25a",
        connection="The same Lord who governs every soul and every circumstance is the One guiding each stage of the soul's journey home, leaving nothing to chance.",
    ),
    dict(
        num=21, slug="narasimhavapuh",
        deva="नारसिंहवपुः", tamil="நாரஸிம்ஹ வபுஃ", iast="N\u0101rasi\u1e43havapu\u1e25",
        meaning="The One who takes on whatever form is needed to protect a devotee in danger.",
        story="""<p>Dr. Venkatesh tells of \u0100di \u015aa\u1e45kara, unprepared for a debate on worldly life having been a
renunciate since childhood, who uses yogic body-transference to enter a dead king's body and learn
what he needs, leaving his own body guarded in a cave. When the king's ministers grow suspicious of
the unusually wise "ruler," they order any renunciate's body found in the forest to be burned \u2014
unknowingly targeting \u015aa\u1e45kara's own.</p>
<p>Soldiers find and set fire to his body in the cave just as he re-enters it, catching his hand in
flames. He prays urgently to Narasimha for rescue. Narasimha appears with sixteen arms \u2014 two holding
conch and discus, two holding \u015aa\u1e45kara steady, two extinguishing the fire, two offering comfort, two
applying healing balm, two lifting him up, and two more offering reassurance \u2014 saving him completely
in that single moment.</p>""",
        teaching="<em>Vapu\u1e25</em> means form or bodily shape. Dr. Venkatesh clarifies that Narasimha here stands as a representative example (<em>upalak\u1e63a\u1e47am</em>) of a broader principle: whenever a devotee cries out in genuine danger, Perum\u0101\u1e37 takes on whatever form \u2014 not necessarily Narasimha specifically \u2014 is exactly suited to protect them in that moment, arriving instantly rather than in some generic or delayed way.",
        living="Help doesn't always come in the form we expect — but it comes in the form that's exactly needed for the danger at hand.",
        reflection="Recall one moment help arrived in an unexpected way, and give thanks for it today.",
        mantra="Om N\u0101rasi\u1e43havapu\u1e63e Nama\u1e25a",
        connection="On the journey home, whatever form of guidance or protection the soul needs at each stage — the Vishnu Dh\u016btas, Agni, the Viraj\u0101 crossing — is provided exactly as needed, the same way Narasimha appeared exactly when \u015aa\u1e45kara needed Him.",
    ),
    dict(
        num=22, slug="sriman",
        deva="श्रीमान्", tamil="ஸ்ரீமான்", iast="\u015ar\u012bm\u0101n",
        meaning="The One whose beauty is defined by how fiercely He protects.",
        story="""<p>Dr. Venkatesh tells of Thirumazhisai Pir\u0101\u1e47 holding a beauty contest among Vi\u1e63\u1e47u's ten
avat\u0101ras. The first three \u2014 Matsya, K\u016brma, Var\u0101ha \u2014 are rejected for non-human form; Vamana for a
"double standard" (small feet to ask, giant feet to measure); Paraśur\u0101ma as "wrong venue" for a
beauty contest. R\u0101ma and K\u1e5b\u1e63\u1e47a are selected, alongside Narasi\u1e43ha. R\u0101ma claims beauty through his
epithet "Sundara R\u0101ma"; K\u1e5b\u1e63\u1e47a claims it through his 16,008 wives. Thirumazhisai Pir\u0101\u1e47 rejects both
\u2014 the "Sundara" title actually belongs to Hanum\u0101n, not R\u0101ma himself, he explains, and mere numbers
of admirers prove nothing.</p>
<p>He declares Narasi\u1e43ha the true beauty, explaining: a wife once said her husband looked most
handsome not on their wedding day, but the moment he fiercely defended her against his own mother \u2014
true beauty is recognized in the moment of protection. Narasi\u1e43ha appeared instantly at every one of
Prahl\u0101da's moments of danger \u2014 fire, a cliff, the sea, snakebite, poison \u2014 and this fierce, immediate
protection is what makes Him alone worthy of the title.</p>""",
        teaching="\u015ar\u012b carries several meanings, one of which is beauty itself. Dr. Venkatesh explains that Mah\u0101lak\u1e63m\u012b, who sits on Perum\u0101\u1e37's chest in every other form (where she cannot see His face clearly), moves specifically to Narasi\u1e43ha's lap so she can gaze directly at this beauty \u2014 a beauty defined not by appearance, but by fierce, instant protection of a devotee. This is why only Narasi\u1e43ha, among all the forms, carries the special epithet \u201c<em>azhagiya singar</em>\u201d (the beautiful lion) \u2014 no other form is called beautiful in quite this way.",
        living="True beauty isn't in how someone looks, but in how fiercely they show up when we need them most.",
        reflection="Show up fiercely for someone today, the way you'd want to be shown up for.",
        mantra="Om \u015ar\u012bmate Nama\u1e25a",
        connection="Just as Mah\u0101lak\u1e63m\u012b moved for a clearer view of this fierce, protective beauty, the soul on its journey home moves toward the same Lord whose beauty is inseparable from His care for those who reach Him.",
    ),
    dict(
        num=23, slug="kesavah",
        deva="केशवः", tamil="கேஶவஃ", iast="Ke\u015bava\u1e25",
        meaning="The One whose beauty served and protected His devotee in a moment of need.",
        story="""<p>Dr. Venkatesh tells of a temple priest at Thirukka\u1e47\u1e47apuram who secretly diverted some of
King Saraboji's garland offerings to his lover instead of the deity. The king, hearing rumors, visits
in disguise to investigate. Unaware, the priest retrieves the very garlands his lover had already
worn and re-offers them to the deity \u2014 and when served as pras\u0101dam, the disguised king finds a long
strand of a woman's hair among the flowers, confirming his suspicion and revealing himself.</p>
<p>The priest insists the hair is Perum\u0101\u1e37's own \u2014 the king demands proof, permitting him to view the
deity from behind during the next day's procession, threatening punishment if unproven. The priest
prays desperately to Perum\u0101\u1e37. The next day, during the Am\u0101v\u0101sy\u0101 procession, Perum\u0101\u1e37 Himself appears
with long, flowing hair \u2014 vindicating the priest's claim and sparing him the king's punishment.</p>""",
        teaching="<em>Ke\u015bam</em> means hair. Dr. Venkatesh notes that this name doesn't celebrate physical beauty for its own sake \u2014 it commemorates a specific act of protection, where Perum\u0101\u1e37 personally intervened, taking on an unusual and specific form (long hair, matching the priest's claim exactly) purely to save a devotee from unjust punishment. The deity at Thirukka\u1e47\u1e47apuram is still called \u201cSaurir\u0101ja Perum\u0101\u1e37\u201d in honor of this event.",
        living="He steps in personally to protect those who serve Him, even in the smallest, most unexpected ways \u2014 down to a detail as specific as a strand of hair.",
        reflection="Defend someone today who can't defend themselves.",
        mantra="Om Ke\u015bav\u0101ya Nama\u1e25a",
        connection="This name shows a Lord who intervenes in exact, specific detail for a devotee in trouble \u2014 the same attentiveness that accompanies the soul through each precise stage of its journey home.",
    ),
    dict(
        num=24, slug="purushottamah",
        deva="पुरुषोत्तमः", tamil="புருஷோத்தமஃ", iast="Puru\u1e63ottama\u1e25",
        meaning="The One supreme above every category of soul — bound, liberated, and eternal.",
        story="""<p>Dr. Venkatesh tells of Garu\u1e0da's sworn enemy, the snake Sumukhan, fleeing to heaven and
hiding near the throne of Perum\u0101\u1e37 (as Upendra). Garu\u1e0da demands his prey; Perum\u0101\u1e37 refuses \u2014 He never
abandons anyone who has taken refuge at His feet. Furious, Garu\u1e0da boasts of his own strength, noting
he carries Perum\u0101\u1e37 on his shoulders daily \u2014 surely proof he is the stronger of the two.</p>
<p>Perum\u0101\u1e37 smiles and presses just His left hand down on Garu\u1e0da's shoulder \u2014 and Garu\u1e0da cannot bear
even that weight alone. Realizing his error, Garu\u1e0da admits that the very strength to carry Perum\u0101\u1e37
was itself Perum\u0101\u1e37's gift to him, not his own. He is then told to carry the very snake he wanted to
kill on his own shoulder from then on \u2014 depicted today at Thiruvellarai as a sculpture titled
\u201cGaru\u1e0da's pride destroyed.\u201d</p>""",
        teaching="Dr. Venkatesh lays out three categories of soul: <em>Puru\u1e63as</em> \u2014 bound souls still living on earth; <em>Puru\u1e63ottu</em> (Muktas) \u2014 souls liberated after living here and surrendering; and <em>Puru\u1e63ottarar</em> (Nityas) \u2014 eternal souls like Garu\u1e0da and \u0100di\u015be\u1e63a who never entered sa\u1e43s\u0101ra at all. Because Perum\u0101\u1e37 is superior to all three categories \u2014 as He proved even to the eternal, exalted Garu\u1e0da \u2014 He is <em>Puru\u1e63ottama\u1e25</em>, supreme above every kind of being.",
        living="What we take pride in as \u201cour own\u201d strength often has a source beyond us worth acknowledging.",
        reflection="Credit one strength of yours today to where it truly came from.",
        mantra="Om Puru\u1e63ottam\u0101ya Nama\u1e25a",
        connection="Even the eternal attendants of Vaiku\u1e47\u1e6dha owe their strength to Him \u2014 a reminder that the soul's journey home ends not in self-sufficiency, but in recognizing the Source of everything, always.",
    ),
    dict(
        num=25, slug="sarvah",
        deva="सर्वः", tamil="ஸர்வஃ", iast="Sarva\u1e25",
        meaning="The One who has the entire universe as His own body.",
        story="""<p>Dr. Venkatesh tells of \u015ar\u012bniv\u0101sa Kaly\u0101\u1e47am at Tirumala \u2014 unusually named after the groom
rather than the bride, because \u015ar\u012bniv\u0101sa personally sponsored the entire wedding, borrowing from
Kubera to feed 33 crore devas, 66 crore asuras, and countless sages. He appoints Agni as cook and
uses the temple's sacred tanks as cooking vessels.</p>
<p>Worried about the delay of feeding such an enormous crowd before the procession can depart,
Perum\u0101\u1e37 Himself sits in the front row and eats everything meant for everyone. The assembled sages,
initially offended that the groom ate before them, soon find themselves completely satisfied without
having eaten at all. When Brahm\u0101 asks how this is possible, Perum\u0101\u1e37 explains: just as only the mouth
eats, yet nourishment reaches every part of the body, the entire universe is His body \u2014 so His
eating alone satisfies every being within it.</p>""",
        teaching="<em>Sarvam</em> means everything. Dr. Venkatesh draws the analogy directly: a single mouth eating nourishes an entire body without every organ needing to eat separately, because the body is one interconnected whole. In the same way, because the entire universe and every being in it is Perum\u0101\u1e37's own body, His single act reaches and satisfies all of it at once \u2014 hence <em>Sarva\u1e25</em>.",
        living="What nourishes the whole eventually reaches every part — care given anywhere ripples everywhere, even where we can't see it land.",
        reflection="Do one act of care today, trusting it reaches further than you can see.",
        mantra="Om Sarv\u0101ya Nama\u1e25a",
        connection="Just as one act at \u015ar\u012bniv\u0101sa's wedding nourished every guest across every world, the Lord's grace on the soul's journey home reaches every stage at once, not one at a time.",
    ),
    dict(
        num=26, slug="sarvah-destroyer",
        deva="शर्वः", tamil="ஶர்வஃ", iast="\u015aarva\u1e25",
        meaning="The One who destroys sin and sorrow at their root.",
        story="""<p>Dr. Venkatesh tells of a time when both Brahm\u0101 and \u015aiva had five heads each. When Brahm\u0101's
fifth head spoke arrogantly, \u015aiva angrily plucked it off \u2014 but the skull stuck permanently to \u015aiva's
own hand, along with the sin of Brahmahatti (harming a Brahmin figure). Unable to free himself
despite visiting countless holy waters and worlds, \u015aiva eventually wanders, as a mendicant, to
Thirukkandiyur, where Perum\u0101\u1e37 resides as "Hara \u015aapa Vimochana Perum\u0101\u1e37."</p>
<p>Bathing in the temple's Kamala Pu\u1e63kari\u1e47i tank and praying, \u015aiva receives Perum\u0101\u1e37's grace: with
Mother Kamal\u0101mbik\u0101's intercession, Perum\u0101\u1e37 Kamal\u0101n\u0101than casts His glance at the skull, instantly
destroying the sin and freeing it from \u015aiva's hand \u2014 complete \u015b\u0101pa vimocanam. \u0100\u1e37v\u0101r praises this
event, calling the Lord of Kandiy\u016br the medicine (<em>marunthu</em>) that removes even the gravest sin.</p>""",
        teaching="From the root <em>\u015bru</em> \u2014 to destroy \u2014 comes <em>\u015barvan</em>, the destroyer of sins and sorrows. Dr. Venkatesh distinguishes this from the previous name, <em>Sarva\u1e25</em> (having everything as His body): this name, <em>\u015barva\u1e25</em>, is specifically about destruction of affliction at its root. Though \u015aiva himself carries the name \u015aarvan too, it is Narayana \u2014 who removed even \u015aiva's own sorrow \u2014 who is praised as <em>\u015barva\u1e25</em> in the Sahasran\u0101ma.",
        living="No burden is too old or too deeply stuck to be released — even the mightiest among us sometimes need this same grace.",
        reflection="Name one thing you're still carrying, and consciously set it down today.",
        mantra="Om \u015aarv\u0101ya Nama\u1e25a",
        connection="If even \u015aiva's ancient affliction could be destroyed at Thirukkandiy\u016br, no burden the soul carries on its journey home is too heavy to be released before reaching Him.",
    ),
    dict(
        num=27, slug="sivah",
        deva="शिवः", tamil="சிவஃ", iast="\u015aiva\u1e25",
        meaning="The auspicious One who showers only good fortune on His devotees.",
        story="""<p>Dr. Venkatesh tells of P\u0101rvat\u012b asking \u015aiva on Kail\u0101sa whom He constantly meditates on.
\u015aiva reveals he meditates ceaselessly on the name of R\u0101ma and \u015ar\u012bman N\u0101r\u0101ya\u1e47a. Astonished at the
Vi\u1e63\u1e47u Sahasran\u0101ma's thousand names, P\u0101rvat\u012b asks if there's an easier equivalent path to the same
merit. \u015aiva teaches her the famous verse: reciting the name "R\u0101ma" once equals reciting all thousand
names of the Sahasran\u0101ma together.</p>
<p>P\u0101rvat\u012b then asks why \u015aiva's own name, "\u015aiva\u1e25," appears among Vi\u1e63\u1e47u's thousand names. \u015aiva explains:
<em>\u015bivam</em> means auspiciousness, and N\u0101r\u0101ya\u1e47a \u2014 the supreme auspicious being, untouched by any evil,
who showers every kind of good fortune upon those who take refuge in Him \u2014 is rightly called
<em>\u015aiva\u1e25</em> for this reason.</p>""",
        teaching="<em>\u015aiva</em> means the auspicious one, and also the one who generates auspiciousness for others. Dr. Venkatesh closes Chapter 3 on this note: Perum\u0101\u1e37 doesn't merely avoid harm \u2014 He actively showers only good fortune upon devotees who come to Him, making this name a fitting close to the theme of protection that runs through this entire chapter.",
        living="This name reminds us: the Protector's ultimate gift isn't just safety from harm, but auspiciousness and good fortune itself.",
        reflection="Wish someone well today, and mean it as a genuine offering, not just a phrase.",
        mantra="Om \u015aiv\u0101ya Nama\u1e25a",
        connection="As Chapter 3 closes, this name carries the soul's journey forward into Chapter 4 — protection given not just to spare us from harm, but to fill our path home with auspiciousness at every step.",
    ),
    dict(
        num=28, slug="sthanuh",
        deva="स्थाणुः", tamil="ஸ்தாணுஃ", iast="Sthāṇuḥ",
        meaning="The steady One, firm and unwavering in raising His devotees upward.",
        story="""<p>Dr. Venkatesh tells of the flood at Madhurantakam, where Perumāḷ Himself held back the
breach in the lake's bund, earning the name "Āḷikāththa Rāmar." Pilgrims from Tirunelveli camped on
that very bund to cook and eat, being orthodox devotees who would not eat outside food. A young
boy among them rinsed his mouth after the meal, and that water happened to fall on a monitor
lizard resting nearby.</p>
<p>Because that water carried the merit of a devotee's leavings (<em>thīrtham</em>), the lizard was
reborn in its next life as the scholar Yādava Prakāśar of Kāṅcheepuram — who became Rāmānuja's
first teacher. Though Yādava Prakāśar later wronged Rāmānuja over doctrinal differences, he eventually
repented and asked his mother for a penance. She told him to circle the entire earth three times
— an impossible task. Varadarāja Perumāḷ appeared in his dream and said: "I consider Rāmānuja
Himself to be the whole world; circling Rāmānuja three times is the same as circling the earth three
times." Yādava Prakāśar did exactly that, became Rāmānuja's disciple, and attained mokṣa by His grace
— a lizard raised, step by patient step across lifetimes, all the way to liberation, with no effort of
its own at any stage.</p>""",
        teaching="<em>Sthāṇuḥ</em> means steady, like a firm pillar. Dr. Venkatesh explains that Perumāḷ is steadfastly, unwaveringly committed to raising His devotees higher and higher, stage by stage, however long it takes — patiently waiting through a lizard's birth, then a scholar's pride, then a disciple's surrender, until mokṣa is finally granted. The One who began the lizard's journey never once wavered in His resolve to finish it.",
        living="Growth in devotion rarely happens in one leap — it happens in patient, unglamorous stages, each one preparing the next, none of them wasted.",
        reflection="Notice one small, unfinished stage of your own growth today, and trust the steadiness guiding it.",
        mantra="Om Sthāṇavē Namaḥa",
        connection="Just as the lizard was carried, lifetime after lifetime, toward Rāmānuja and mokṣa without ever having to find the way itself, the soul's journey home is guided by this same unwavering steadiness — the Guide who never lets go partway.",
    ),
    dict(
        num=29, slug="bhutadih",
        deva="भूतादिः", tamil="பூதாதிஃ", iast="Bhūtādiḥ",
        meaning="The Origin of all beings, who draws every heart to Him without being known.",
        story="""<p>Dr. Venkatesh tells of Kṛṣṇa in Āyarpāḍi, happily eating with His cowherd friends. Watching from
heaven, the devas grew envious: "These cowherds eat with Kṛṣṇa, and we have no such fortune!" Hoping to at
least receive the leftovers the boys would wash from their hands into the Yamunā, all thirty-three crore devas
came to the river as fish. Kṛṣṇa, knowing this, playfully told His friends that bhagavat prasāda must never be
washed off the hands — wipe them on a cloth or a pillar instead. The disappointed devas went to Brahmā, who
promised to teach Kṛṣṇa a lesson.</p>
<p>Brahmā hid Kṛṣṇa's friends and calves in a cave and left for Satyaloka. Kṛṣṇa, finding them gone, answered
with a līlā of His own. At Satyaloka the guard turned Brahmā away as a "duplicate" — another Brahmā was already
seated inside — and he fell back to earth to find Kṛṣṇa, the friends and the calves all there, and all still in the
cave as well. By the time he came down, a full year had passed on earth. Bewildered, Brahmā prayed for forgiveness,
opened his eyes, and saw the friends, the cows, even the lunch boxes, and the Brahmā above, all four-armed with
conch and discus. Kṛṣṇa Himself had become every one of them. Brahmā realized it, begged pardon, and was
forgiven; he returned the hidden friends and calves, and Kṛṣṇa drew back the duplicate creation into Himself.</p>
<p>Dr. Venkatesh adds a tender detail: for that whole year, Kṛṣṇa lived in each home as each boy. Parents showered
unusual affection on their children; a mother who beat her son daily doted on him for a year; a maid who scolded
a lunch box scrubbed it lovingly. They did not know it was Kṛṣṇa, yet He was in those forms, and love rose in them
unbidden.</p>""",
        teaching="<em>Būta</em> means all created beings, and <em>ādiḥ</em> means the origin. Dr. Venkatesh teaches that because the Lord is the origin of every being, we are drawn to Him the moment we meet Him — an attraction, a love, rising within us even when we do not know who He is. Being the source of all, He attracts all, and so He is called <em>Bhūtādiḥ</em>.",
        living="The pull we feel toward what is good and beautiful may be older than we know — a quiet homing instinct toward our Source.",
        reflection="Notice one thing today that draws your heart without reason, and thank its Source.",
        mantra="Om Bhūtādayē Namaḥa",
        connection="The parents loved without knowing why; the soul, too, feels the pull toward its Origin long before it knows the way, and that pull is the first step of the journey home.",
    ),
    dict(
        num=30, slug="nidhiravyayah",
        deva="निधिरव्ययः", tamil="அவ்யயநிதிஃ", iast="Nidhiravyayaḥ",
        meaning="The imperishable Treasure, the one wealth that can never be stolen or destroyed.",
        story="""<p>Dr. Venkatesh tells of Kubera and Rāvaṇa. Kubera, lord of the north and king of the nine
treasuries, possessed boundless wealth — the śaṅkha Nidhi, the Padma Nidhi, every treasure
imaginable. His half-brother Rāvaṇa, consumed by arrogance, attacked Kubera, seized his Puṣpaka
Vimāna, and plundered every treasure he owned.</p>
<p>Grief-stricken, Kubera went to sage Nārada and cried: "I was lord of all wealth in the world, and
my own brother has reduced me to nothing! Is no worldly treasure permanent?" Nārada explained:
every worldly treasure is perishable — stolen by thieves, eroded by time, passed from hand to hand.
But there is one treasure no one can ever plunder, one wealth that never diminishes: the lotus feet
of Śrīman Nārāyaṇa Himself. Nārada counseled Kubera to take refuge in Him alone. Following this, Kubera
worshipped Perumāḷ and found, in Him, the one treasure that could never be taken from him again.</p>""",
        teaching="<em>Nidhi</em> means treasure; <em>avyayaḥ</em> means that which never perishes or diminishes at any time. Dr. Venkatesh pairs this with the Āḷvārs' own experience: however vast one's worldly wealth, it is destined to end one day, but Perumāḷ alone is the imperishable treasure that pours out undiminished bliss and liberation to His devotees across every age, never running dry.",
        living="Every worldly treasure we hold can be taken from us — by time, by circumstance, by someone else's greed. Only what we build in devotion can never be plundered.",
        reflection="Name one thing you treasure today that could be lost, and one that never can be.",
        mantra="Om Avyayanidhayē Namaḥa",
        connection="Kubera learned that even a king of treasuries can be robbed of everything but one — the same undiminishing treasure the soul finds waiting at the end of its journey home, never to be taken away again.",
    ),
    dict(
        num=31, slug="sambhavah",
        deva="सम्भवः", tamil="ஸம்பவஃ", iast="Sambhavaḥ",
        meaning="The One who takes on whatever form is fitting to draw His devotees to Him.",
        story="""<p>Dr. Venkatesh tells of a farmer in the village of Chilkur, between Hyderabad and Secunderabad,
in present-day Telangana, who for years offered a portion of his harvest to Tirumalai Tiṣṇuēm
Perumāḷ. As he grew old — past seventy — he could no longer climb the seven hills to make his
offering, and wept before Perumāḷ at home, asking what he should do now. That night, Tiruvenēkaṭam
Perumāḷ appeared in his dream: "Near your field there is a śiva liṅgam. Dig beside it — I will come and
appear to you there, since you can no longer come searching for Me."</p>
<p>The farmer and villagers dug at the spot; blood suddenly began to flow from the earth, because
their tools had struck the very idol buried below. They poured milk to beg forgiveness, and lifting
the idol out, found Śrīnivāsa Perumāḷ Himself, flanked by Śrīdevi and Bhūdevi, consecrated right there
at Chilkur — worshipped since as "Chilkur Bālāji," and today known as "Chilkur Visa Bālāji," because
devotees who circle Him and recite the Viṣṇu Sahasranāma there are said to quickly receive visas and
good employment abroad.</p>""",
        teaching="<em>Sambhavaḥ</em> means one who appears in the exact form fitting each age. Dr. Venkatesh traces this across the four yugas — Naraśiṃha and Vāmana in Kṛta Yuga, Rāma in Trētā, Kṛṣṇa in Dvāpara — and, with warm humor, suggests that for today's generation, drawn to visas and careers abroad, Perumāḷ meets them exactly where they are, as 'Visa Bālāji.' He is not rigid about the form He takes — only about reaching the devotee.",
        living="The Lord doesn't insist we come to Him in one fixed way — He meets each of us, each generation, where our actual longings are, and draws us forward from there.",
        reflection="Notice what you're genuinely longing for today, and bring that honestly into your prayer.",
        mantra="Om Sambhavāya Namaḥa",
        connection="The farmer who could no longer climb the hill found that Perumāḷ came down to dig Himself out and meet him halfway — just as the Guide meets the soul partway on the journey home, however far it has fallen behind.",
    ),
    dict(
        num=32, slug="bhavanah",
        deva="भावनः", tamil="பாவனஃ", iast="Bhāvanaḥ",
        meaning="The One who arises within a devotee's sincere devotion and fulfills it personally.",
        story="""<p>Dr. Venkatesh tells of Sena Nhavi, a barber-saint of Maharāshtra and a devoted servant of
the king, who was also a fervent devotee of Viṭṭhala (Kṛṣṇa). One day, lost in ecstatic bhajan and
meditation at home, Sena lost track of time while the king waited angrily for his shave. Perceiving
His devotee's danger, Viṭṭhala Himself took Sena's form, rushed to the palace with razor and bowl in
hand, and shaved the king — whose body shivered with divine bliss at the touch.</p>
<p>Looking in the mirror, the king saw not Sena's face but Perumāḷ's own form, conch and discus and
all, and showered gold coins on Him in wonder, asking who he truly was. Kṛṣṇa took the coins and
vanished. When the real Sena finally arrived, panicked and apologizing for his lateness, the baffled
king described what had just happened — and Sena realized, weeping, that Perumāḷ Himself had
come in his form to protect his worship from interruption.</p>""",
        teaching="<em>Bhāvanaḥ</em> means the One who arises within His devotees' sincere inner feeling (<em>bhāva</em>) and personally fulfills it. Dr. Venkatesh teaches that Perumāḷ takes whatever form is needed — even taking on a devotee's own identity — the instant loving devotion calls for it, so that nothing can come between a devotee and their worship.",
        living="When our devotion is sincere, help arrives in forms we never expect — sometimes protecting the very thing we were worried about losing.",
        reflection="Trust one act of devotion today, even an interrupted or imperfect one, to be completed by grace.",
        mantra="Om Bhāvanāya Namaḥa",
        connection="Sena never had to choose between duty and devotion — Perumāḷ Himself stepped in; the same Guide who steps into the gaps on the soul's journey home when devotion alone cannot carry it all the way.",
    ),
    dict(
        num=33, slug="bharta",
        deva="भर्ता", tamil="பர்தா", iast="Bhartā",
        meaning="The One who bears and sustains all who take refuge in Him.",
        story="""<p>Dr. Venkatesh tells of a poor brāhmaṇa's wife in Thiruvarangam-era Melkote, where Rāmānuja
had been uplifting the oppressed with the five sacraments. With her husband away begging alms,
and not even a handful of rice at home, she wept when Rāmānuja and his disciples arrived seeking
alms, unable to send away her Acārya empty-handed.</p>
<p>A wealthy man in the village, who had long desired her, offered her grain on the condition that
she spend that night alone with him. Reasoning that turning away the world-teacher Rāmānuja was
the greater wrong, she agreed, cooked the meal, and fed Rāmānuja and his disciples. Her husband,
himself a true devotee, understood her sacrifice and honored the bargain by escorting her to the
man's house that evening. But when she entered, a divine radiance — from the merit of Rāmānuja's
prasadam and her own chastity — shone from her face; the wealthy man saw in her nothing but a
mother, Mahalakshī herself, and fell at her feet begging forgiveness, his lust entirely dissolved. He
later became a disciple of Rāmānuja himself.</p>""",
        teaching="<em>Bhartā</em> means the One who bears, sustains, and protects. Dr. Venkatesh teaches that Perumāḷ never abandons those who trust Him and His devotees, holding up their honor, their life, and their dharma intact even in the most desperate circumstances — carrying them, like an eyelid shields the eye, through situations they could never have survived alone.",
        living="When we act rightly out of devotion, even at real personal cost, we are never carrying that risk alone.",
        reflection="Do one right thing today that costs you something, trusting you are held through it.",
        mantra="Om Bhartrē Namaḥa",
        connection="She risked everything to feed her Acārya and was carried safely through it — the same bearing, sustaining grace that holds the soul through every uncertain stage of its journey home.",
    ),
    dict(
        num=34, slug="prabhavah",
        deva="प्रभवः", tamil="ப்ரபவஃ", iast="Prabhavaḥ",
        meaning="The One whose birth is exalted, extraordinary, and utterly unlike ordinary birth.",
        story="""<p>Dr. Venkatesh describes Kṛṣṇa's birth at midnight in Kamsa's prison, under impossible
security — Vasudeva chained, the doors bolted. Yet Kṛṣṇa appeared, as śukabrahma describes, as a
wondrous infant with lotus eyes, already with four arms bearing conch and discus, Śrīvatsa and the
Kaustubha jewel on His chest, and Mahalakshī already present with Him — as if He arrived already
married, already adorned, needing nothing added. Even child Brahmā appeared seated on His navel
lotus.</p>
<p>The instant He was born, Vasudeva's shackles fell away on their own, the prison doors swung
open, and the Yamunā river parted to let them cross to Gokulam, with Ādiśēṣa shielding the infant
from the rain. No ordinary child is born already armed, already adorned, already attended by a
river's own reverence. Dr. Venkatesh notes this is not an ordinary birth caused by karma, like ours
— it is a descent chosen entirely out of His own compassion, exalted above and beyond anything we
could call "birth."</p>""",
        teaching="<em>Prabhavaḥ</em> comes from <em>bhavaḥ</em> (birth) with the prefix <em>pra</em> (exalted, elevated) — birth that rises above ordinary birth. Dr. Venkatesh explains that where we are born bound by karma, Perumāḷ chooses His own parents, His own form, His own moment, descending purely out of grace — making even His \"birth\" a a gift rather than a bondage.",
        living="Where we have no choice over the circumstances of our own birth, the Lord's every descent is chosen freely, purely for our sake — a reminder that grace, not compulsion, moves Him toward us.",
        reflection="Reflect today on one way grace, not obligation, has shaped your life.",
        mantra="Om Prabhavāya Namaḥa",
        connection="However humble our own birth, this name promises it can still be elevated by grace — just as the soul's journey home lifts an ordinary life into something extraordinary by the time it arrives.",
    ),
    dict(
        num=35, slug="prabhuh",
        deva="प्रभुः", tamil="ப்ரபுஃ", iast="Prabhuḥ",
        meaning="The Master who governs all rules, yet is bound by none of them.",
        story="""<p>Dr. Venkatesh tells of śiśupāla, born to Kṛṣṇa's aunt Śrutaśravā with four arms like Perumāḷ
and three eyes like śiva — a strange "cocktail" of a birth. A voice from the sky declared that
whoever's touch made the extra limbs and eye vanish would become this child's cause of death.
When young Kṛṣṇa affectionately picked up his cousin, the extra arms and eye disappeared instantly.
Śrutaśravā, alarmed, asked if Kṛṣṇa would kill her son. Kṛṣṇa reassured her: so long as śiśupāla behaved,
there was nothing to fear — and granted a remarkable concession: ninety-nine offenses a day would
be forgiven; only the hundredth would bring death.</p>
<p>For years, śiśupāla insulted Kṛṣṇa daily, always stopping carefully at ninety-nine. But at Yudhiṣṭhira's
Rājasūya sacrifice, swept up by others egging him on, he crossed the line on his hundredth insult.
Kṛṣṇa released His discus and ended him — yet sent him straight to Vaikuṇṭha, a liberation even great
yogis rarely attain. When people protested the unfairness, Vyāsa explained: śiśupāla, in truth, was
one of Perumāḷ's own gatekeepers, Jaya or Vijaya, cursed to three earthly births (Hiraṇyākṣa-
Hiraṇyakaśipu, Rāvaṇa-Kumbhakarṇa, śiśupāla-Dantavakra) before returning to his post. Once the third
birth ended, he had to return to Vaikuṇṭha — and no rule, not even the rules of justice as others saw
them, could bind Perumāḷ's own decision about when that happened.</p>""",
        teaching="<em>Prabhuḥ</em> means the One who commands and controls everyone, yet whom no rule can ever bind. Dr. Venkatesh teaches that every law, every scripture, every cosmic ordinance operates under Perumāḷ's authority — but His own will is never subject to them; He grants concessions, mercy, even liberation, entirely on His own terms.",
        living="Rules and consequences govern our lives, but grace itself is never bound by our sense of what's fair — it can arrive on terms we'd never have calculated.",
        reflection="Let go of one expectation today about how grace \"should\" work, and simply receive it.",
        mantra="Om Prabhavē Namaḥa",
        connection="śiśupāla's long-delayed homecoming was never in doubt, however long the detour — a reminder that the Guide's own authority over the soul's journey home is never bound by how long or winding the path looks from here.",
    ),
    dict(
        num=36, slug="isvarah",
        deva="ईश्वरः", tamil="ஈஶ்வரஃ", iast="Īśvaraḥ",
        meaning="The One who exercises absolute command and authority over everything, everywhere.",
        story="""<p>Dr. Venkatesh tells of Kṛṣṇa's gurukula years under sage Sāndīpani, where He mastered all
sixty-four arts in just sixty-four days. When Kṛṣṇa asked what guru-dakṣiṇā he wished, Sāndīpani
deferred to his wife, who revealed that their son had drowned at sea, swallowed by a great fish
during a bath years earlier, and asked that he be restored.</p>
<p>Kṛṣṇa dove beneath the ocean searching for the fish, cut it open, found the boy gone, and traced him
further and further until He reached Yamapurī itself — the realm of Death. There, He simply asked
Yamadharmarāja for Sāndīpani's son, and Yamadharmarāja returned him without resistance. Kṛṣṇa
brought the boy back and restored him to his teacher, a feat Thirumangai Āḷvār later sings of at
Nācciyār Kŋvil near Kumbakonam. No one else, Dr. Venkatesh notes, could command Yama himself
and reverse death — yet Kṛṣṇa's authority reached even there, and reached just as fully into His own
earthly avatāra as it does in Vaikuṇṭha itself.</p>""",
        teaching="<em>Īśvaraḥ</em> means the One who exercises absolute command (<em>āḷumai</em>) — the capacity to govern and direct everything. Dr. Venkatesh emphasizes that Perumāḷ's command is not limited to Vaikuṇṭha; the same full authority travels with Him into every avatāra, so that even as a human child in Gokulam, He could command Death itself without diminishment.",
        living="True authority isn't a position we occupy — it travels with us into every circumstance, humble or grand, because it comes from character and grace, not just rank.",
        reflection="Exercise one act of quiet, caring authority today over something only you can steady.",
        mantra="Om Īśvarāya Namaḥa",
        connection="If Perumāḷ's command over Yama Himself never wavered even in a humble gurukula story, Chapter 4 closes on this certainty: the same unbroken authority governs every stage of the soul's journey home, right to the very end.",
    ),
    dict(
        num=37, slug="svayambhuh",
        deva="स्वयम्भूः", tamil="ஸ்வயம்பூஃ", iast="Svayambh\u016b\u1e25",
        meaning="The One who appears in the divine form of His own choosing.",
        story="""<p>Dr. Venkatesh tells of a br\u0101hma\u1e47a who came to K\u1e5b\u1e63\u1e47a's court in Dv\u0101rak\u0101, protesting that the kingdom was ill-governed: five of his children had vanished into the sky the moment they were born, and his wife was expecting a sixth. Arjuna, stung by the charge, vowed to protect the child and built a cage of arrows from G\u0101\u1e47\u1e0d\u012bva around the mother. The child was born \u2014 and vanished all the same. Bound by his vow, Arjuna prepared to enter the fire.</p>
<p>K\u1e5b\u1e63\u1e47a stopped him, took Arjuna and the br\u0101hma\u1e47a into His chariot, and had it driven straight toward Vaiku\u1e47\u1e6dha. There, on the laps of \u015ar\u012bdev\u012b, Bh\u016bdev\u012b and N\u012b\u1e37\u0101dev\u012b, sat all six children. The Mothers explained: on earth He had taken a body unlike ours, and they had longed to see it, so they had staged this l\u012bl\u0101 to bring Him. K\u1e5b\u1e63\u1e47a gently asked them to stop, returned the children to the br\u0101hma\u1e47a, and brought him home to Dv\u0101rak\u0101. Dr. Venkatesh cites \u0100\u1e37v\u0101r's verse in the Tiruv\u0101ymo\u1e5bi on how He restored the br\u0101hma\u1e47a's sons.</p>""",
        teaching="<em>Svayambh\u016b\u1e25</em> means the One who appears as He wishes. Dr. Venkatesh explains the Mothers' point: we are born in bodies of the five elements, shaped by our karma, but when Perum\u0101\u1e37 descends He takes a divine form made of pure <em>sattva</em> (<em>pa\u00f1ca-upani\u1e63ad-maya</em>), entirely by His own will.",
        living="Our bodies come to us shaped by our past; His form is chosen out of love alone. That difference is the whole difference between bondage and grace.",
        reflection="Pause once today and give thanks for your body, then remember it is only a loan for the journey.",
        mantra="Om Svayambhav\u0113 Nama\u1e25a",
        connection="As we begin Chapter 5, the Lord who needs no body of karma comes among us in a form of His own choosing, and that same freedom is what He holds out to the soul at the end of its journey home.",
    ),
    dict(
        num=38, slug="sambhuh",
        deva="शम्भुः", tamil="ஶம்புஃ", iast="\u015aambhu\u1e25",
        meaning="The One who bestows true, lasting spiritual joy.",
        story="""<p>Dr. Venkatesh opens by noting that ordinary happiness and true peace are different. He recalls Kamal Haasan asking Rajinikanth why he keeps going to the Himalayas, and Rajinikanth answering that there is happiness here, but not peace, so he goes in search of peace. The word <em>\u015bam</em> names that real spiritual joy.</p>
<p>He then tells of Pi\u1e37\u1e37ai Ura\u1e45k\u0101vil\u0101\u1e0di D\u0101sar of Srirangam, a bodyguard to the Chola king, so devoted to his wife that he walked behind her holding an umbrella against the sun. R\u0101m\u0101nuja asked why. He said he was captivated by her eyes. R\u0101m\u0101nuja asked: if I showed you more beautiful eyes, what would you do? D\u0101sar said he would be their slave from that day. R\u0101m\u0101nuja led him before Ra\u1e45ganatha and prayed that the Lord reveal the eye-beauty He had shown the \u0100\u1e37v\u0101rs. The moment Periyaperum\u0101\u1e37 did so, D\u0101sar became a servant of Ra\u1e45ganatha and R\u0101m\u0101nuja, and his wife Pon\u1e47\u0101cciy\u0101r became R\u0101m\u0101nuja's disciple.</p>""",
        teaching="<em>\u015aam</em> is true spiritual joy, and <em>\u015aambhu\u1e25</em> is the One who gives it. Dr. Venkatesh teaches that D\u0101sar did not give up love; in one glance he saw where real joy lives. The delight found in family, friends and the world does not hold it. It is found in Perum\u0101\u1e37 alone. He cites Ma\u1e47av\u0101\u1e37a M\u0101mu\u1e49i's verse on how He draws His devotees close.",
        living="Joys of the world are real, but they are small windows. This name points to the light they were all opening onto.",
        reflection="Ask yourself today which of your joys leave you at peace, and spend a little more time there.",
        mantra="Om \u015aambhav\u0113 Nama\u1e25a",
        connection="D\u0101sar's change happened in a single glance. On the soul's journey home, one true sight of the Lord is enough to turn every other attachment into service.",
    ),
    dict(
        num=39, slug="adityah",
        deva="आदित्यः", tamil="ஆதித்யஃ", iast="\u0100ditya\u1e25",
        meaning="The One who dwells within the sun as its inner Self, watching over His devotees.",
        story="""<p>Dr. Venkatesh retells the well-known scene of Draupad\u012b dragged into the Kaurava court after Dharmaraja lost her at dice. She argued that the game was invalid, since Yudhi\u1e63\u1e6dhira had already lost himself and could not stake her. Duryodhana brushed this aside and ordered Du\u1e25\u015b\u0101sana to strip her. Seeing that her husbands and the elders, Bh\u012b\u1e63ma and Dro\u1e47a, were silent, she turned to the One refuge of the helpless and cried out: <em>\u015aa\u1e45kha cakra gad\u0101p\u0101\u1e47\u0113, Dv\u0101rak\u0101 nilaya, Acyuta, Govinda, Pu\u1e47\u1e0dar\u012bk\u0101k\u1e63a, rak\u1e63a m\u0101\u1e43 \u015bara\u1e47\u0101gat\u0101m.</em></p>
<p>At once K\u1e5b\u1e63\u1e47a caused the sari to flow without end, until Du\u1e25\u015b\u0101sana collapsed in exhaustion. Dr. Venkatesh says it flowed from the sun's centre, where N\u0101r\u0101ya\u1e47a abides, as in <em>dhy\u0113yassad\u0101 savit\u1e5bma\u1e47\u1e0dala madhyavart\u012b N\u0101r\u0101ya\u1e47a\u1e25</em>, looking down on His devotees from there. He closes with the old Tamil saying that between the 'hole-handed' (Dv\u0101rak\u0101) and the elephant (Hastin\u0101pura) lie a thousand miles, yet a sari trade went on between them, like online shopping.</p>""",
        teaching="<em>\u0100dityah</em> is the One who stands at the centre of the sun as its <em>antary\u0101mi</em>. Dr. Venkatesh explains that from there He watches over every devotee, so that no distance, a thousand miles included, stands between a cry for help and His answer. He also notes that He holds the conch and discus in hand so no time is lost when someone calls.",
        living="Help is never far when it is truly called for. The distance we imagine between us and the Lord is only ours.",
        reflection="Next time you feel alone in a difficulty today, say His name once and trust it has been heard.",
        mantra="Om \u0100dity\u0101ya Nama\u1e25a",
        connection="Draupad\u012b was rescued across a thousand miles; the soul on its journey home is likewise watched from the sun's centre, and none of its calls go unanswered.",
    ),
    dict(
        num=40, slug="pushkarakshah",
        deva="पुष्कराक्षः", tamil="புஷ்கராக்ஷஃ", iast="Pu\u1e63kar\u0101k\u1e63a\u1e25",
        meaning="The One whose lotus eyes captivate every heart.",
        story="""<p>Dr. Venkatesh picks up the question left at the end of the last episode. In Pa\u00f1cava\u1e6di, \u015aurpa\u1e47akh\u0101, struck by R\u0101ma's beauty, asked him to marry her. R\u0101ma sent her to Lak\u1e63ma\u1e47a; Lak\u1e63ma\u1e47a, calling himself R\u0101ma's servant, sent her back. Believing S\u012bt\u0101 was the obstacle, she rushed to devour her, and at R\u0101ma's word Lak\u1e63ma\u1e47a drew his sword and cut off her nose and ears.</p>
<p>The puzzle: \u015aurpa\u1e47akh\u0101 was a powerful, shape-changing r\u0101k\u1e63as\u012b. Why did she just stand there? Dr. Venkatesh says V\u0101lm\u012bki answers it: she never saw Lak\u1e63ma\u1e47a or the blade. Her eyes were fixed on R\u0101ma's lotus eyes, and she stood spellbound. Even afterward, weeping in front of R\u0101va\u1e47a, she described the brothers as <em>pu\u1e47\u1e0dar\u012bka vi\u015b\u0101l\u0101k\u1e63au</em>, with wide lotus eyes. Even mutilated, it was their eyes she remembered.</p>""",
        teaching="<em>Pu\u1e63kara</em> means lotus and <em>ak\u1e63a</em> means eye. Dr. Venkatesh teaches that if those eyes could hold even a r\u0101k\u1e63as\u012b so completely, no devotee can fail to be drawn by them. Through His glance (<em>kat\u0101k\u1e63a</em>) He removes the devotee's every shortcoming and draws them to Himself.",
        living="What we look at shapes us. A single glance at what is truly beautiful can hold the heart more firmly than anything else.",
        reflection="Rest your eyes today for one minute on something beautiful and offer that looking to Him.",
        mantra="Om Pu\u1e63kar\u0101k\u1e63\u0101ya Nama\u1e25a",
        connection="The first sight of His eyes is what turns the soul from all else; on the journey home, His glance is the very thing that draws it forward.",
    ),
    dict(
        num=41, slug="mahasvanah",
        deva="महास्वनः", tamil="மஹாஸ்வனஃ", iast="Mah\u0101svana\u1e25",
        meaning="The One whose great, resounding voice is the source of the Vedas.",
        story="""<p>Dr. Venkatesh explains that <em>svana</em> means sound, so <em>Mah\u0101svana\u1e25</em> is the One who makes a great sound. He gives two examples. First, the Var\u0101ha avat\u0101ra: the demon Hira\u1e47y\u0101k\u1e63a had rolled up the earth like a mat and hidden it in the depths of the ocean. Var\u0101ha emerged from Brahm\u0101's nostril the size of a thumb, then grew as large as a mountain, leapt into the sea, and let out a mighty roar. That roar carried the sound of the four Vedas, including S\u0101ma Veda; the worlds trembled and the demon armies scattered, while the sages and devas felt great peace.</p>
<p>Second, at Kuruk\u1e63etra, K\u1e5b\u1e63\u1e47a lifted the P\u0101\u00f1cajanya conch and sounded it. As the G\u012bt\u0101 says, that sound split the hearts of Dh\u1e5btar\u0101\u1e63\u1e6dra's sons. The same sound that frightens the enemy gives courage to His own.</p>""",
        teaching="<em>Mah\u0101svana\u1e25</em> is the One whose voice is the origin of the Vedas and of the <em>pra\u1e47ava</em> (Om). Dr. Venkatesh teaches that He lets this sound ring out both when He creates and when He protects, and it brings fearlessness to the devoted and dread to the hostile.",
        living="Speech that comes from a steady heart carries weight. Fear loosens its grip where the Lord's name is sounded.",
        reflection="Say one thing today slowly, clearly and kindly, as if it mattered.",
        mantra="Om Mah\u0101svan\u0101ya Nama\u1e25a",
        connection="The roar that lifted the earth from the ocean is the same sound that lifts the soul out of fear and carries it onward on its journey home.",
    ),
    dict(
        num=42, slug="anadinidhanah",
        deva="अनादिनिधनः", tamil="அனாதிநிதனஃ", iast="An\u0101dinidhana\u1e25",
        meaning="The One with no beginning and no end, beyond birth and death.",
        story="""<p>Dr. Venkatesh explains that <em>\u0101di</em> is beginning (birth) and <em>nidhana</em> is end (death). Every being, even the devas, is subject to both. Brahm\u0101's life ends after one hundred Brahma-years; Indra holds office only for one manvantara. Perum\u0101\u1e37 alone is without either.</p>
<p>He tells of the sage M\u0101rka\u1e47\u1e0deya, tossed about in the floods of the great dissolution (<em>pralaya</em>). In that endless water he saw a small child lying on a banyan leaf, sucking His toe in yoga-sleep. When M\u0101rka\u1e47\u1e0deya asked who He was, the child opened His mouth, and the sage saw all the worlds and all the devas safely moving inside. He understood that the Lord existed before creation and remains after dissolution. The \u0100\u1e37v\u0101rs sing of Him as the great light without beginning or end.</p>""",
        teaching="<em>An\u0101dinidhana\u1e25</em> is the One who has neither origin nor end. Dr. Venkatesh teaches that we turn between birth and death under the grip of time, while He holds time in His hand, the Lord of the wheel of time (<em>k\u0101la cakra</em>), and is Himself untouched by it.",
        living="Everything we cling to has a beginning and an end. Only the One we are turning toward has neither.",
        reflection="Think of one thing that worries you and ask whether it will matter a thousand years from now. Then rest in the One who will.",
        mantra="Om An\u0101dinidhan\u0101ya Nama\u1e25a",
        connection="The child on the banyan leaf is still there when all else has dissolved. That is the place the soul is heading to: the one home that does not end.",
    ),
    dict(
        num=43, slug="dhata",
        deva="धाता", tamil="தாதா", iast="Dh\u0101t\u0101",
        meaning="The One who sows and creates, planting the seed of all creation.",
        story="""<p>Dr. Venkatesh tells of Vi\u015bv\u0101mitra's sacrifice, which R\u0101ma and Lak\u1e63ma\u1e47a guarded, as Kamban sings, the way eyelids guard the eye. He notes the elders' reading: R\u0101ma was the upper lid, taller and moving about, while Lak\u1e63ma\u1e47a was the lower lid, steady in one place. The lid closes before anything touches the eye, just as they met every danger before it arrived.</p>
<p>For six days all was quiet. On the seventh, M\u0101r\u012bca and Sub\u0101hu rained flesh and blood on the sacrificial ground. R\u0101ma killed Sub\u0101hu but only hurled M\u0101r\u012bca into the sea. Why spare him? Dr. Venkatesh cites Villur Swamy's verse in his Ma\u00f1ju R\u0101m\u0101ya\u1e47a: the story of R\u0101ma is a wish-fulfilling tree, and R\u0101ma wanted that tree to grow. Had M\u0101r\u012bca died then, there would be no golden deer, no abduction of S\u012bt\u0101, no great epic. So R\u0101ma planted M\u0101r\u012bca like a seed in the sea, and from it the R\u0101m\u0101ya\u1e47a grew.</p>""",
        teaching="<em>Dh\u0101t\u0101</em> means the One who sows. Dr. Venkatesh teaches that just as R\u0101ma sowed M\u0101r\u012bca so the epic could flourish, before creation the Lord wished the world to spread into many branches, and sowed Brahm\u0101 as a seed in the primal matter (<em>m\u016bla prak\u1e5bti</em>), so that all creation could grow through him.",
        living="Some things that seem to be left unfinished are in fact seeds being planted for a larger growth later.",
        reflection="Name one unfinished thing in your life and ask what it might be growing toward.",
        mantra="Om Dh\u0101tr\u0113 Nama\u1e25a",
        connection="Even what looked like a pause in the story was a seed. On the journey home, no delay is wasted in His hands.",
    ),
    dict(
        num=44, slug="vidhata",
        deva="विधाता", tamil="விதாதா", iast="Vidh\u0101t\u0101",
        meaning="The One who creates in a special way and arranges each soul's fruits of karma.",
        story="""<p>Dr. Venkatesh takes up the question left last time: if <em>Dh\u0101t\u0101</em> and <em>Vidh\u0101t\u0101</em> both mean creator, what is the difference? <em>Vi</em> means special, so <em>Vidh\u0101t\u0101</em> is the One who creates in a special way. He turns to the Mah\u0101bh\u0101rata. When Yudhi\u1e63\u1e6dhira was born to Kunt\u012b before Gandh\u0101r\u012b had borne a child, Gandh\u0101r\u012b, consumed with jealousy, struck her own womb. What came out was a mass of flesh. Vy\u0101sa divided it into one hundred and one pieces and placed them in jars of ghee, and in time the hundred Kauravas and the daughter Du\u1e25\u015bal\u0101 were born.</p>
<p>By ordinary law a child comes only from a mother's womb. So who arranged life, body and karma in those jars? Dr. Venkatesh says it was not an ordinary act of Brahm\u0101, but a special creation by the Lord who is within him. Even though Vy\u0101sa performed it, N\u0101r\u0101ya\u1e47a stood within Vy\u0101sa and did it.</p>""",
        teaching="<em>Dh\u0101t\u0101</em> creates the world in general from its source material; <em>Vidh\u0101t\u0101</em> goes beyond the usual laws to arrange each soul's creation and its fruits according to its own past karma. That is why He is also called the One who fixes destiny (<em>vidhi</em>).",
        living="What looks like fate, even the harshest, is held in hands that arrange it with care. We are never just the leftover of chance.",
        reflection="Think of one hard circumstance of your life and pray for the grace to see it as arranged, not accidental.",
        mantra="Om Vidh\u0101tr\u0113 Nama\u1e25a",
        connection="The same One who arranges each soul's destiny is the One who arranges its way home, bending even karma toward the end of the path.",
    ),
    dict(
        num=45, slug="dhaturuttamah",
        deva="धातुरुत्तमः", tamil="தாதுருத்தமஃ", iast="Dh\u0101turuttama\u1e25",
        meaning="The foremost Creator, greater than Brahm\u0101 himself.",
        story="""<p>Dr. Venkatesh tells that when Brahm\u0101 once set out to create the most beautiful woman in the world, the result was Ahaly\u0101. The devas, Indra among them, all asked for her hand. Brahm\u0101 set a contest: whoever first circled the world would win her. Indra set out on his elephant Air\u0101vata. But the sage Gautama, as a cow in his hermitage was calving, simply circled the cow, which by the \u015b\u0101stras equals circling the whole earth. Brahm\u0101, impressed, gave Ahaly\u0101 to Gautama.</p>
<p>Indra, cheated, took the form of a cock and crowed before dawn to send Gautama off to the river, then came in Gautama's own form to Ahaly\u0101. Gautama returned, learned the truth, and cursed them both. Ahaly\u0101 was to lie as a stone for thousands of years, until the son of Da\u015baratha, R\u0101ma, came there, and the dust of His feet touched her. When R\u0101ma passed that way with Vi\u015bv\u0101mitra, the dust of His feet touched the stone, and Ahaly\u0101 rose again in her beauty.</p>""",
        teaching="<em>Dh\u0101tu</em> is the creator, here Brahm\u0101, and <em>uttama\u1e25</em> means the highest. Dr. Venkatesh points out the secret: Brahm\u0101 made Ahaly\u0101 out of the elements, bone, flesh and skin. But R\u0101ma gave life afresh to a lifeless rock with the dust of His feet and renewed her, lifting a curse that even Brahm\u0101 could not remove.",
        living="Nothing is so hardened that it cannot be softened by grace. What feels like stone in us can be brought to life.",
        reflection="Name one thing in you that feels stuck like stone, and offer it to Him.",
        mantra="Om Dh\u0101turuttam\u0101ya Nama\u1e25a",
        connection="With Dh\u0101turuttama\u1e25, Chapter 5 closes on a stone brought to life by His feet, as the soul on its journey home is raised and made new at the end.",
    ),
    dict(
        num=46, slug="aprameyah",
        deva="अप्रमेयः", tamil="அப்ரமேயஃ", iast="Aprameyaḥ",
        meaning="The immeasurable One, whom no yardstick, mind or word can contain.",
        story="""<p>Dr. Venkatesh tells of a king in Karnataka who loved to debate with scholars. One day he asked his court pandits how big Perumāḷ really was, what He weighed, what area He covered, and whether anyone could measure Him. The scholars said the Supreme cannot be measured with worldly scales. The king refused to accept a God who could not be measured and insisted on a demonstration.</p>
<p>A simple devotee, a wise man, stepped forward. He said it was easy, but first the king must do him a small favour: measure all the water of the great ocean into one small pot, and count every star in the night sky one by one. The king was stunned and said that was impossible. The sage smiled: if you cannot measure the nature the Lord made, how can you measure the One who holds all the worlds within His body? He recalled that as Vāmana, the Lord measured the earth with one step and the heavens with another, as Trivikrama. The king saw his ignorance, bowed his head, and took refuge in Him.</p>""",
        teaching="<em>Prameya</em> is what can be measured, and <em>Aprameyaḥ</em> is the One who cannot. Dr. Venkatesh cites the Veda, <em>yato vāco nivartante aprāpya manasā saha</em>, where speech and mind turn back unable to reach Him, and the Āḷvārs' invitation to keep savouring His endless qualities.",
        living="Our small worries and narrow thinking come from trying to hold everything inside our own measure. Letting go of that measure is a relief.",
        reflection="Name one thing you are trying to fully understand today, and offer the rest to the One beyond measure.",
        mantra="Om Aprameyāya Namaḥa",
        connection="The final chapter opens on a Lord no one can fit into a measure; the journey home leads to Someone we will keep discovering forever.",
    ),
    dict(
        num=47, slug="hrishikeshah",
        deva="हृषीकेशः", tamil="ஹ்ருஷீகேஶஃ", iast="Hṛṣīkēśaḥ",
        meaning="The Master of the senses, who turns His devotees' senses toward Himself.",
        story="""<p>Dr. Venkatesh explains that <em>hṛṣīka</em> means the senses and mind, and <em>īśa</em> is the lord. Controlling the senses is hard for people: the eye wants to see, the tongue to taste, the mind to wander. But Perumāḷ draws His devotees' senses to Himself and guides them well.</p>
<p>He brings the elders' picture of Pārvatī asking Śiva about the Lord's beauty. Śiva tells her that once the eyes have seen His face and smile, they want to see nothing else; ears that have heard His flute and His names do not want worldly talk; the nose that has smelt the tulasi offered to Him seeks no other fragrance; and the mind that has taken refuge at His feet does not wander. And at Kurukṣetra, when Arjuna's senses failed and he dropped his bow, Kṛṣṇa, as charioteer, took control of Arjuna's mind and senses, taught the Gītā, and raised him again as a warrior. That is why the Gītā so often calls Him Hṛṣīkēśa.</p>""",
        teaching="<em>Hṛṣīkēśaḥ</em> is the Lord of the senses. Dr. Venkatesh teaches that if we want our senses not to lead us astray, we must hand the reins to Him, the One who moves the senses of every being.",
        living="Rather than fighting the senses alone, we can give them something worth turning toward.",
        reflection="Choose one sense today, such as sight or hearing, and give it only something that points to Him.",
        mantra="Om Hṛṣīkēśāya Namaḥa",
        connection="On the journey home the senses are not silenced but turned to Him; they become the ways in which the soul finally sees, hears and savours Him.",
    ),
    dict(
        num=48, slug="padmanabhah",
        deva="पद्मनाभः", tamil="பத்மநாபஃ", iast="Padmanābhaḥ",
        meaning="The One from whose navel-lotus Brahmā is born, bearing the creation of all worlds.",
        story="""<p>Dr. Venkatesh tells that at the time of dissolution all worlds were submerged. Nārāyaṇa lay in yoga-sleep on Ādiśēṣa in the milk ocean and resolved to create again. From His navel a golden lotus grew, and on it appeared Brahmā, four-faced. Looking around, Brahmā saw only darkness and water and wondered who he was and where he was. He went down the lotus stalk for thousands of years seeking its origin and could not find it.</p>
<p>He returned to the lotus and heard a voice: <em>ta-pa, ta-pa</em>, perform tapas. After long penance he saw, with the eye of knowledge, the Lord who was his support. The Lord taught him the Vedas and gave him the power and means to create, as the Bhāgavatam records. Dr. Venkatesh adds that one can still see this at Tiruvananthapuram, where Brahmā sits on the lotus rising from the Lord's navel.</p>""",
        teaching="<em>Padma</em> is lotus and <em>nābhi</em> is navel. Dr. Venkatesh teaches that the Lord is the source of all worlds, mother and father of all beings, who carries Brahmā on the lotus of His navel so that creation can begin.",
        living="Every new beginning, however creative, rests on something we did not make.",
        reflection="Before starting something new today, pause and thank the One who is its source.",
        mantra="Om Padmanābhāya Namaḥa",
        connection="Brahmā searched for the lotus's root and found it only by turning to Him in tapas; the soul too finds its source not by searching downward, but by looking up to Him.",
    ),
    dict(
        num=49, slug="amaraprabhuh",
        deva="अमरप्रभुः", tamil="அமரப்ரபுஃ", iast="Amaraprabhuḥ",
        meaning="The Lord of the devas, who rushes to protect even the gods in danger.",
        story="""<p>Dr. Venkatesh recalls that when Madhu and Kaiṭabha stole the Vedas from Brahmā, Perumāḷ ran to him and crushed them like bedbugs. He then tells of Bhasmāsura, who gained from Śiva the boon that whoever's head he touched would burn to ash, and then tried it on Śiva himself. Śiva fled, and Perumāḷ stopped the demon. He told Bhasmāsura he must first perform <em>ācamana</em> before using the boon, taught him the twelve names (Keśava, Nārāyaṇa, Mādhava and so on) touched to twelve parts of the body, and as the demon did so, he touched his own head and turned to ash. The Āḷvār sings of this as the Lord removing the trouble of Kumaran's father, that is, Śiva.</p>
<p>Dr. Venkatesh gives the picture of a family where the head steps in when any member is in trouble, or a company where the MD comes to fix a worker's problem. So the Lord, as head of the devas, comes when they are in danger. He says this can be seen at Tiruvananthapuram: at the Lord's head is a Śiva liṅgam, to whom He says do not worry, I will protect you from Bhasmāsura, and on His navel lotus is Brahmā, to whom He says I will look after you too.</p>""",
        teaching="<em>Amara</em> are the immortals, the devas, and <em>prabhuḥ</em> their master. Dr. Venkatesh teaches that Perumāḷ protects even Brahmā and Śiva whenever they are in danger, because He is the leader of the whole family.",
        living="Even the greatest need a protector. There is no shame in asking for refuge.",
        reflection="Let someone know today that you need help with something you have been carrying alone.",
        mantra="Om Amaraprabhavē Namaḥa",
        connection="If even Brahmā and Śiva were protected by Him, no soul on the journey home is too small to be sheltered.",
    ),
    dict(
        num=50, slug="visvakarma",
        deva="विश्वकर्मा", tamil="விஶ்வகர்மா", iast="Viśvakarmā",
        meaning="The great Architect who fashioned all the worlds, in all their variety.",
        story="""<p>Dr. Venkatesh takes up the question: Viśvakarmā is the name of the divine carpenter, so how does it belong to the Lord? He plays on the English word GOD: Generation, Operation, Destruction, creation, protection and dissolution, all done by Nārāyaṇa alone.</p>
<p>An ordinary sculptor needs stone (the material cause), tools such as chisel and hammer (the instrumental cause), a place to work, and himself as the maker. But when the Lord made the universe, nothing else existed. He was the material, He was the instrument, and He was the sculptor. Dr. Venkatesh cites Vedānta Deśika and the ācāryas, who describe Him as both the efficient and the material cause. Look at a person's eye, a fingerprint: no two are alike. The whole universe is a gallery carved by His hands.</p>""",
        teaching="<em>Viśva</em> is the world and <em>karma</em> is work or creation. Dr. Venkatesh teaches that the divine carpenter known as Viśvakarmā is only a small portion of Him; the original Architect is Perumāḷ Himself, who fashioned everything by His will alone.",
        living="Nothing about you is accidental; every detail, down to a fingerprint, is the work of a Maker who does not repeat Himself.",
        reflection="Look closely at your own hand today and remember the One who made it.",
        mantra="Om Viśvakarmaṇē Namaḥa",
        connection="The One who fashioned every world is the One who prepares the way home; the journey is designed, not left to chance.",
    ),
    dict(
        num=51, slug="manuh",
        deva="मनुः", tamil="மனுஃ", iast="Manuḥ",
        meaning="The One whose mere will creates and governs everything.",
        story="""<p>Dr. Venkatesh tells that after Kṛṣṇa killed Kaṃsa, Kaṃsa's father-in-law Jarāsandha attacked Mathurā seventeen times, and each time Kṛṣṇa and Balarāma destroyed his armies. The eighteenth time he came with Kālayavana. Kṛṣṇa, seeing the people of Mathurā, children and elders, losing their peace, decided to move them all somewhere no enemy could easily reach, a new city in the sea.</p>
<p>He called Viśvakarmā, received twelve yojanas of land from the ocean at the Gujarat coast, and had Dvārakā built in a single night, with gold and jewelled walls, palaces, gardens and pillars. Then, with His yoga power, He lifted the sleeping Yādavas of Mathurā, with their children, cows, beds and homes, and brought them into Dvārakā. They woke to ocean waves and golden palaces, safe and amazed.</p>
<p>Viśvakarmā built with outside tools. Kṛṣṇa arranged it all by His will alone. Dr. Venkatesh also cites Yājñavalkya telling Gārgī in the Bṛhadāraṇyaka Upaniṣad that it is at the command of the Imperishable that sun and moon stand in their places.</p>""",
        teaching="<em>Manuḥ</em> is the One who contemplates, who governs by His resolve. Dr. Venkatesh teaches that He is also the inner Self of the sage Manu who gave the law, and that the sun, the moon, the earth, the wind and the sea keep their courses only by His will.",
        living="Order in the world is not an accident; it rests on a will that cares for us.",
        reflection="Notice one steady thing today, like sunrise or breath, and see it as held by His will.",
        mantra="Om Manavē Namaḥa",
        connection="He carried a whole sleeping city to safety in one night; the soul on its way home is carried in the same way, by His will and not by its own strength.",
    ),
    dict(
        num=52, slug="tvashta",
        deva="त्वष्टा", tamil="த்வஷ்டா", iast="Tvaṣṭā",
        meaning="The Sculptor who chisels away what is rough, and draws the soul into its true form.",
        story="""<p>Dr. Venkatesh tells of Tirupputṛkuli near Kāñcīpuram, where the Lord is Vijayarāghava Perumāḷ and where Rāma performed the last rites for Jaṭāyu. During renovation, the people decided to make a grand horse vehicle for Him, and a king or chief invited the two best sculptors, promising honour and reward for the finest, most lifelike work.</p>
<p>One sculptor carved the wood finely and decorated it with ornaments and saddle. The other meditated on the Lord, removed unwanted parts of the wood one by one, and made a horse with hidden mechanisms inside. On the day, both looked splendid. The second sculptor said, test it yourself, and turned a small knob near the ear: the horse stamped, shook its head, and stood like a living horse. Everyone marvelled. Vijayarāghava Perumāḷ mounted that horse for the Brahmotsava, and the horse vehicle is celebrated there still.</p>""",
        teaching="<em>Tvaṣṭā</em> is the carpenter or sculptor who chips away what is rough and reveals form. Dr. Venkatesh teaches that as the sculptor removes waste wood, the Lord removes our karma, ego, desire and anger with the chisel of His grace, and shapes us into pure souls. At dissolution He also draws the whole universe back into Himself.",
        living="What feels like loss in us, the rough edges being taken off, may be the sculptor at work.",
        reflection="Think of one rough habit and ask the Sculptor to take it away, gently.",
        mantra="Om Tvaṣṭrē Namaḥa",
        connection="The journey home is a long carving: at each stage something false is removed until only the soul's true form stands in His presence.",
    ),
    dict(
        num=53, slug="sthavishthah",
        deva="स्थविष्ठः", tamil="ஸ்தவிஷ்டஃ", iast="Sthaviṣṭhaḥ",
        meaning="The most vast One, whose cosmic form holds all the worlds.",
        story="""<p>Dr. Venkatesh tells of a simple devotee who longed to visit every holy place in India: Kāśī, Gaṅgā, Badrināth, Kēdārnāth, Ayodhyā, Dvārakā, Srirangam, all on foot. He kept both Ekādaśīs every month with full fasting, and broke the fast the next day, through all seasons. Years of walking aged him. India's holy places are beyond number and no lifetime can cover them. In a forest he lost his way, his legs gave out, and he fell and wept: my body is spent and my life is ending; must my wish go unfulfilled?</p>
<p>Unable to bear His devotee's longing, the Lord appeared in person and showed him the Viśvarūpa, as He did for Arjuna. In it the devotee saw the sky and stars turning on His heads, all the holy rivers, Gaṅgā, Yamunā, Gōdāvari, Kāvēri, flowing through His body, all the mountains, Meru and Himalaya, all the holy places, and the thirty-three crore devas within His limbs. In that one place, seeing His body, he received the fruit of bathing in every holy water and seeing every holy place. He fell at the Lord's feet and attained Paramapadam.</p>""",
        teaching="<em>Sthaviṣṭhaḥ</em> is the One of the most vast form. Dr. Venkatesh teaches that reciting the eleventh chapter of the Gītā, the Viśvarūpa Darśana Yoga, or contemplating this name, gives the fruit of beholding the cosmic form, and that those who cannot go on pilgrimage receive the merit of all the holy waters.",
        living="The places we long to reach are already held within Him; no journey is wasted when the heart is turned toward Him.",
        reflection="If there is a place you have always wanted to go, offer that longing to Him today.",
        mantra="Om Sthaviṣṭāya Namaḥa",
        connection="This devotee reached Paramapadam at the end of a journey he could not finish on his own; the Lord came to him. That is the promise of the road home.",
    ),
    dict(
        num=54, slug="sthavirah-dhruvah",
        deva="स्थविरो ध्रुवः", tamil="ஸ்தவிரோ த்ருவஃ", iast="Sthavirо Dhruvaḥ".replace("о","o"),
        meaning="The most ancient One, who never ages and ever stays the same.",
        story="""<p>Dr. Venkatesh takes this name as <em>Sthaviraḥ</em>, or <em>Sthaviro Dhruvaḥ</em>, as the verse reads. He brings it to the child Kṛṣṇa at Āyarpāḍi, who went from house to house stealing butter and playing pranks, while the gopīs came to Yaśodā to complain that He had stolen their butter and broken their curd pots. Even in their complaints, they loved Him so much that they could not bear to be apart from Him for a moment, and stood spellbound by His face and His childish laughter.</p>
<p>But in truth, he says, who is this child? He is the original Supreme Being who made all the worlds, the grandfather of Brahmā, the Ancient One before all devas and sages. No one can count how many yugas and kalpas have passed for Him: He is the eldest of all. And yet, as people age, wrinkles come, strength fades, beauty fades, and sometimes they are set aside. Perumāḷ is the oldest of all and yet in His divine form there is no change, no weakness, no wrinkle. Time does not touch Him; He is ever young.</p>""",
        teaching="<em>Sthaviraḥ</em> means the most ancient, and <em>Dhruvaḥ</em> the unmoving, unchanging. Dr. Venkatesh teaches that the Lord is both the eldest of all and always in His eternal youth, and that this delights His devotees forever. He also says that reciting the name brings steadiness of mind and spiritual strength in old age.",
        living="Age takes much from us, but not our relationship with Him. That is the one thing that does not grow old.",
        reflection="Think of someone older than you today and treat them with the kind of care you would want when you are old.",
        mantra="Om Sthavirāya Namaḥa, or Om Sthavirāya Dhruvāya Namaḥa",
        connection="The journey home ends with Him as He is: the Ancient One, ever young, and unchanging. There is nothing left to lose and nothing that ever fades.",
    ),
]

by_num = {n["num"]: n for n in DIVINE_NAMES}
TOTAL_NAMES = 54

DISCOURSE_PLAYLIST_URL = "https://www.youtube.com/playlist?list=PLZOtgrSp1tzDpF-yqTRcib5F_dlMwccZ8"

DISCOURSE_LINKS = {
    11: "https://www.youtube.com/watch?v=ThuaeigLrDM",
    12: "https://www.youtube.com/watch?v=VlB3yojfML4",
    14: "https://www.youtube.com/watch?v=Dd-tDi38ttg",
    18: "https://www.youtube.com/watch?v=QV9xX6PdlYU",
    1: "https://youtu.be/tED6qRHTPFU",
    2: "https://youtu.be/xAgLDgGos-Y",
    3: "https://youtu.be/sjt65v9zZWk",
    4: "https://youtu.be/DnVm0J9mS-s",
    5: "https://youtu.be/6yVPTorEr6M",
    6: "https://youtu.be/QBgDfeRmHgo",
    7: "https://youtu.be/JL52QwCnCS8",
    8: "https://youtu.be/Z1bg9vi_jVg",
    9: "https://youtu.be/rlIwlDL_lqI",
    10: "https://www.youtube.com/watch?v=PvmMhD0yy4M&list=PLZOtgrSp1tzDpF-yqTRcib5F_dlMwccZ8&index=10",
    13: "http://www.youtube.com/watch?v=ycKQilsHFG4",
    15: "http://www.youtube.com/watch?v=nx8nAUu-F4Q",
    16: "http://www.youtube.com/watch?v=KuOepmhU0AE",
    17: "http://www.youtube.com/watch?v=k7gxhHin2w4",
    19: "http://www.youtube.com/watch?v=JchoBFIUF10",
    20: "http://www.youtube.com/watch?v=0bEZcYq3jU0",
    21: "http://www.youtube.com/watch?v=81l4OYYJTSQ",
    22: "http://www.youtube.com/watch?v=nEAKgi-KKSc",
    23: "http://www.youtube.com/watch?v=LNabV8EwW0g",
    24: "http://www.youtube.com/watch?v=ntIXYWDE3lM",
    25: "http://www.youtube.com/watch?v=8QgFNyXF77M",
    26: "http://www.youtube.com/watch?v=-5U9EijNw9Q",
    27: "http://www.youtube.com/watch?v=eUx8diFbLro",
    28: "https://www.youtube.com/watch?v=JPPCQ1Z39o8",
    29: "https://www.youtube.com/watch?v=9wr4pKmRe7I",
    30: "https://www.youtube.com/watch?v=Mfi4OXKOtkU",
    31: "https://www.youtube.com/watch?v=Si_6v8wiycA",
    32: "https://www.youtube.com/watch?v=fx2Bll7itCE",
    33: "https://www.youtube.com/watch?v=lhDFGI1wq7A",
    34: "https://www.youtube.com/watch?v=PVokGjYbFWU",
    35: "https://www.youtube.com/watch?v=T29RnDD9jis",
    36: "https://www.youtube.com/watch?v=bxwiLenCLV4",
    37: "https://www.youtube.com/watch?v=W-fDTAqeyK8",
    38: "https://www.youtube.com/watch?v=zw0M-CSyB7E",
    39: "https://www.youtube.com/watch?v=X4NFSXVudlA",
    40: "https://www.youtube.com/watch?v=f2YR1fIK9Sg",
    41: "https://www.youtube.com/watch?v=SKTAOzYw7X8",
    42: "https://www.youtube.com/watch?v=5th_ghzo3EQ",
    43: "https://www.youtube.com/watch?v=xWVaeL-0buA",
    44: "https://www.youtube.com/watch?v=mkWFQt_WjRI",
    45: "https://www.youtube.com/watch?v=07VMh78J__c",
    46: "https://www.youtube.com/watch?v=rvw1AO91XLI",
    47: "https://www.youtube.com/watch?v=w-_fiDPCk1w",
    48: "https://www.youtube.com/watch?v=VFOdqSUPDM0",
    49: "https://www.youtube.com/watch?v=-6f_UBfV-fs",
    50: "https://www.youtube.com/watch?v=rl0E0srYZhI",
    51: "https://www.youtube.com/watch?v=4R05E8Dxmow",
    52: "https://www.youtube.com/watch?v=VVCMxVkJoe4",
    53: "https://www.youtube.com/watch?v=fkDqt5o3v30",
    54: "https://www.youtube.com/watch?v=5V2wapsL3yM",
}

STAGES = [
    ("1", "the-soul-leaves-the-body", "The Soul Leaves the Body"),
    ("2", "vishnu-dhootas-arrive", "Vishnu Dhootas Arrive"),
    ("3", "agni-and-the-path-of-light", "Agni and the Path of Light"),
    ("4", "day-shukla-paksha-uttarayana", "Day, \u015aukla Pak\u1e63a and Uttar\u0101ya\u1e47a"),
    ("5", "sun-moon-lightning", "Sun, Moon and Lightning"),
    ("6", "amanava-purusha", "Am\u0101nava Purusha"),
    ("7", "viraja-river", "Vir\u0101j\u0101 River"),
    ("8", "paramapadam", "Paramapadam"),
]

# ------------------------------------------------------------------
# Divine Name detail pages (folder + index.html for pretty URLs)
# ------------------------------------------------------------------

for n in DIVINE_NAMES:
    chapter = chapter_for(n["num"])
    code = pathram_code(n["num"])
    prev_n = by_num.get(n["num"] - 1)
    next_n = by_num.get(n["num"] + 1)
    prev_link = f'<a href="../{prev_n["slug"]}/index.html">&larr; {prev_n["iast"]}</a>' if prev_n else '<a href="../index.html">&larr; All names</a>'
    next_link = f'<a href="../{next_n["slug"]}/index.html">{next_n["iast"]} &rarr;</a>' if next_n else '<a href="../index.html">All names &rarr;</a>'

    related = [x for x in (prev_n, next_n) if x]
    related_html = "".join(
        f'<a href="../{r["slug"]}/index.html">{r["iast"]}</a>' for r in related
    ) or '<span>More names coming soon</span>'

    body = f"""
<article>
  <div class="name-header">
    <span class="pathram-code">{code} &middot; Chapter {chapter['num']}: {chapter['title']}</span>
    <p class="eyebrow" style="color:var(--gold-light)">Name {n['num']} of {TOTAL_NAMES}</p>
    <div class="script-stack">
      <span class="script-devanagari">{n['deva']}</span>
      <span class="script-tamil">{n['tamil']}</span>
      <span class="script-iast">{n['iast']}</span>
    </div>
    <p class="meaning-line">{n['meaning']}</p>
  </div>

  <div class="panel">
    <p class="section-title">Acharya's Teaching</p>
    <p>{n['teaching']}</p>
  </div>

  <div class="panel story-panel">
    <p class="section-title">The Story</p>
    {n['story']}
  </div>

  <div class="panel">
    <p class="section-title">Living This Divine Name</p>
    <p>{n['living']}</p>
  </div>

  <div class="panel practice-panel">
    <p class="section-title">Today's Reflection &amp; Practice</p>
    <p>{n['reflection']}</p>
  </div>

  <div class="panel mantra-panel">
    <p class="section-title">Chant</p>
    <p class="mantra-text">{n['mantra']}</p>
  </div>

  <div class="panel">
    <p class="section-title">Connection to the Journey Home</p>
    <p>{n['connection']}</p>
  </div>

  <div class="panel discourse-panel">
    <p class="section-title">Learn from the Original Discourse</p>
    <p>This page is a concise learning companion. For the complete teaching, listen to Dr. Venkatesh
    Swamin's original discourse on this name:</p>
    <a class="discourse-link" href="{DISCOURSE_LINKS.get(n['num'], DISCOURSE_PLAYLIST_URL)}" target="_blank" rel="noopener">Watch the original discourse on {n['iast']} &rarr;</a>
    <p class="disclaimer">Any simplification or presentation error on this page is entirely ours.
    Please listen to the original discourse for complete understanding.</p>
  </div>

  <div class="panel">
    <p class="section-title">Related Divine Names</p>
    <div class="related-row">{related_html}</div>
  </div>

  <div class="nav-between">
    {prev_link}
    {next_link}
  </div>
</article>
"""
    html = page(f"{n['iast']} \u2014 The Journey Home", "names", body, depth=2)
    name_folder = os.path.join(NAMES_DIR, n["slug"])
    os.makedirs(name_folder, exist_ok=True)
    with open(os.path.join(name_folder, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)

# ------------------------------------------------------------------
# Divine Name Collection index
# ------------------------------------------------------------------

names_index_body = [
    '<p class="section-title" style="text-align:center;">N\u0101r\u0101ya\u1e47a Anugraha Patram</p>',
    '<p class="meaning-line" style="text-align:center;margin:0 auto 6px;">54 Divine Names for the Journey Home</p>',
    '<p style="text-align:center;color:rgba(248,240,218,0.8);max-width:520px;margin:0 auto 20px;">'
    'Each Pathram presents one Divine Name of Sriman Narayana. It is not a fortune or prediction. '
    'It is an invitation to reflect, chant, and live the teaching revealed through that Name.</p>',
]

for c in CHAPTERS:
    names_index_body.append(f'<div class="collection-block"><p class="collection-title">Chapter {c["num"]} &mdash; {c["title"]}</p>')
    names_index_body.append(f'<p class="chapter-desc">{c["desc"]}</p><div class="name-grid">')
    lo, hi = c["range"]
    for num in range(lo, hi + 1):
        n = by_num.get(num)
        if n:
            names_index_body.append(
                f'<a class="name-tile" href="{n["slug"]}/index.html"><span class="tile-num">{pathram_code(num)}</span><span class="tile-name">{n["iast"]}</span></a>'
            )
        else:
            names_index_body.append(
                f'<div class="name-tile pending"><span class="tile-num">{pathram_code(num)}</span><span class="tile-name">Coming soon</span></div>'
            )
    names_index_body.append("</div></div>")

names_index_html = page("Divine Name Collection \u2014 The Journey Home", "names", "\n".join(names_index_body), depth=1)
with open(os.path.join(NAMES_DIR, "index.html"), "w", encoding="utf-8") as f:
    f.write(names_index_html)

# ------------------------------------------------------------------
# Home page
# ------------------------------------------------------------------

home_body = """
<div class="panel intro-panel">
  <p>The Journey Home is our family's humble Golu kainkaryam, inspired by Nammalwar's S\u016b\u1e37 Visumbu,
  Sri Ramanuja's \u015aara\u1e47\u0101gati, Vishnu Sahasranama, and the teachings of our Acharyas.</p>
</div>

<div class="cta-row">
  <a class="cta-button primary" href="golu-story.html">Explore the Golu</a>
  <a class="cta-button secondary" href="journey-home/index.html">Follow the Journey Home</a>
</div>
<div class="cta-row">
  <a class="cta-button secondary" href="divine-names/index.html">Discover the 54 Divine Names</a>
  <a class="cta-button secondary" href="audio-guides.html">Listen to the Audio Guide</a>
</div>

<div class="panel">
  <p class="section-title">Guiding Principle</p>
  <p>We are not authors of the sampradaya. We are students sharing what we have learned from our
  &Acirc;ch&amacr;ryas. Every theological explanation on this site is based on traditional teachings,
  especially the discourses of Dr. Venkatesh Swamin &mdash; our contribution is only to organize,
  present, and make the teachings accessible.</p>
</div>
"""
home_html = page("The Journey Home", "home", home_body, depth=0,
                  description="The soul's journey to the lotus feet of Sriman Narayana \u2014 a Navaratri Golu 2026 family kainkaryam.")
with open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8") as f:
    f.write(home_html)

# ------------------------------------------------------------------
# The Golu Story
# ------------------------------------------------------------------

golu_story_body = """
<div class="panel">
  <p class="story-section-label">Section A &middot; Dining Room</p>
  <p class="story-section-title">Grace and Surrender</p>
  <ul class="story-list">
    <li>Nammalwar's Thiruvadi Thozhal</li>
    <li>Nammalwar's return for loka-k\u1e63emam</li>
    <li>Panguni Uttiram</li>
    <li>Sri Ramanuja's \u015aara\u1e47\u0101gati</li>
    <li>Gadya Trayam</li>
  </ul>
</div>

<div class="panel">
  <p class="story-section-label">Section B &middot; Pooja Room</p>
  <p class="story-section-title">The Journey of the J\u012bv\u0101tma</p>
  <ul class="story-list">
    <li>Departure from the body</li>
    <li>Vishnu Dhootas</li>
    <li>Archir\u0101di M\u0101rgam</li>
    <li>Viraj\u0101</li>
    <li>Paramapadam</li>
    <li>Eternal kainkaryam</li>
  </ul>
</div>

<p class="connecting-statement">Sri Ramanuja shows us the path of surrender. Nammalwar reveals the
destination and the Lord's loving reception of the soul.</p>

<div class="cta-row">
  <a class="cta-button primary" href="virtual-tour.html">Take the Virtual Tour &rarr;</a>
</div>
<div class="cta-row">
  <a class="cta-button secondary" href="journey-home/index.html">Follow the Journey Home &rarr;</a>
</div>
"""
golu_story_html = page("The Golu Story \u2014 The Journey Home", "golu-story", golu_story_body, depth=0)
with open(os.path.join(ROOT, "golu-story.html"), "w", encoding="utf-8") as f:
    f.write(golu_story_html)

# ------------------------------------------------------------------
# Journey Home overview + 8 stage placeholder pages
# ------------------------------------------------------------------

exec(open(os.path.join(ROOT, "journey_section.py"), encoding="utf-8").read())

exec(open(os.path.join(ROOT, "malai_section.py"), encoding="utf-8").read())

# ------------------------------------------------------------------
# Audio Guides
# ------------------------------------------------------------------

audio_body = """
<div class="panel">
  <p class="section-title" style="text-align:center;">Audio Guides</p>
  <div class="audio-choice-row">
    <div class="audio-choice">
      <span class="audio-badge">For Everyone</span>
      <h3>5&ndash;7 Minute Narration</h3>
      <ul>
        <li>Simple explanation</li>
        <li>No prior Sri Vaishnava knowledge needed</li>
      </ul>
      <p style="margin-top:12px;"><em>Audio player coming soon.</em></p>
    </div>
    <div class="audio-choice">
      <span class="audio-badge">Deeper Journey</span>
      <h3>10&ndash;15 Minute Narration</h3>
      <ul>
        <li>S\u016b\u1e37 Visumbu</li>
        <li>Prapatti</li>
        <li>Gadya Trayam</li>
        <li>Archir\u0101di M\u0101rgam</li>
        <li>Paramapadam and kainkaryam</li>
      </ul>
      <p style="margin-top:12px;"><em>Audio player coming soon.</em></p>
    </div>
  </div>
</div>
"""
audio_html = page("Audio Guides \u2014 The Journey Home", "audio", audio_body, depth=0)
with open(os.path.join(ROOT, "audio-guides.html"), "w", encoding="utf-8") as f:
    f.write(audio_html)

# ------------------------------------------------------------------
# Virtual Tour (A-Frame 360 walkaround, VR-headset capable)
# ------------------------------------------------------------------

TOUR_ROOMS = [
    dict(id="dining-room", label="Dining Room", sublabel="Grace and Surrender",
         img="assets/panoramas/dining-room.jpg"),
    dict(id="pooja-room", label="Pooja Room", sublabel="The Journey of the J\u012bv\u0101tma",
         img="assets/panoramas/pooja-room.jpg"),
]

tour_body = f"""
<div class="panel">
  <p class="section-title" style="text-align:center;">Step Inside the Golu</p>
  <p style="text-align:center;">A 360&deg; virtual walkaround of the exhibition &mdash; drag to look
  around on desktop, or tilt your phone to look around like you're standing in the room.</p>
</div>

<div class="tour-room-switch" id="room-switch">
  {"".join(f'<button class="tour-room-btn{" active" if i==0 else ""}" data-room="{r["id"]}">{r["label"]}</button>' for i, r in enumerate(TOUR_ROOMS))}
</div>

<div class="tour-wrap">
  <div class="tour-scene-frame" id="panorama"></div>
  <p class="tour-instructions">{TOUR_ROOMS[0]['label']} &mdash; {TOUR_ROOMS[0]['sublabel']}</p>
</div>

<p class="tour-vr-note">This is a placeholder 360&deg; scene. Once real photos of the finished Golu are
taken (using a phone's Panorama mode), they'll drop in here without changing anything else on this
page.</p>

<div class="cta-row">
  <a class="cta-button secondary" href="golu-story.html">&larr; Back to the Golu Story</a>
</div>

<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/pannellum@2.5.6/build/pannellum.css">
<script src="https://cdn.jsdelivr.net/npm/pannellum@2.5.6/build/pannellum.js"></script>
<script>
(function() {{
  var rooms = {{
    {", ".join(f'"{r["id"]}": {{label: "{r["label"]}", sublabel: "{r["sublabel"]}", img: "{r["img"]}"}}' for r in TOUR_ROOMS)}
  }};
  var buttons = document.querySelectorAll('.tour-room-btn');
  var instructions = document.querySelector('.tour-instructions');
  var viewer = null;

  function loadRoom(roomId) {{
    var r = rooms[roomId];
    if (viewer) {{ viewer.destroy(); }}
    viewer = pannellum.viewer('panorama', {{
      type: 'equirectangular',
      panorama: r.img,
      autoLoad: true,
      compass: false,
      orientationOnByDefault: true,
      showZoomCtrl: true,
      showFullscreenCtrl: true
    }});
    instructions.textContent = r.label + ' \u2014 ' + r.sublabel;
  }}

  buttons.forEach(function(btn) {{
    btn.addEventListener('click', function() {{
      buttons.forEach(function(b) {{ b.classList.remove('active'); }});
      btn.classList.add('active');
      loadRoom(btn.getAttribute('data-room'));
    }});
  }});

  loadRoom('{TOUR_ROOMS[0]['id']}');
}})();
</script>
"""
tour_html = page("Virtual Tour \u2014 The Journey Home", "tour", tour_body, depth=0,
                  description="Step inside the Navaratri Golu 2026 exhibition with a 360-degree virtual walkaround.")
with open(os.path.join(ROOT, "virtual-tour.html"), "w", encoding="utf-8") as f:
    f.write(tour_html)

# ------------------------------------------------------------------
# About & Acknowledgements
# ------------------------------------------------------------------

about_body = """
<div class="panel">
  <p class="section-title">About &amp; Acknowledgements</p>
  <p>This website and exhibition are a humble family learning project and kainkaryam. We do not
  present ourselves as independent interpreters of the samprad&#257;ya. The theological content is
  drawn from the teachings of our &Acirc;ch&amacr;ryas and presented in a concise, visitor-friendly
  format.</p>
</div>

<div class="panel">
  <p class="section-title">Sources &amp; Acknowledgements</p>
  <ul class="story-list">
    <li>Nammalwar and Divya Prabandham</li>
    <li>Sri Ramanuja and Gadya Trayam</li>
    <li>Vishnu Sahasranama</li>
    <li>Dr. Venkatesh Swamin's 1008 Divine Name discourse series</li>
    <li>Our family's contribution in curation, artwork, technology, and presentation</li>
  </ul>
  <p style="margin-top:16px;">Any simplification or presentation error is entirely ours. Visitors are
  encouraged to listen to the original discourses for complete understanding.</p>
</div>

<div class="panel">
  <p class="section-title">The Family</p>
  <p><strong>Hema</strong> &mdash; Creative Direction, Project Management, Content Editing<br>
  <strong>Venkatesh</strong> &mdash; Display, Construction, Lighting, Technology<br>
  <strong>Sriram</strong> &mdash; Research, Pronunciation, Technology<br>
  <strong>Sana</strong> &mdash; Artwork, Creative Design, a Child's Perspective<br>
  <strong>Thatha</strong> &mdash; Traditional Guidance, Stories, Review, Blessings</p>
</div>

<div class="panel">
  <p class="section-title">Technology Philosophy</p>
  <p>Technology serves devotion, not the other way around. AI is used here to organize, illustrate,
  design, summarize, and build &mdash; never to replace the &Acirc;ch&amacr;rya.</p>
</div>
"""
about_html = page("About & Acknowledgements \u2014 The Journey Home", "about", about_body, depth=0)
with open(os.path.join(ROOT, "about.html"), "w", encoding="utf-8") as f:
    f.write(about_html)

print(f"Built {len(DIVINE_NAMES)} name pages, {len(PASURAMS)} pasuram pages, and all top-level pages.")

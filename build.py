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
    ("journey", "Journey Home", "/journey-home/index.html"),
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
]

by_num = {n["num"]: n for n in DIVINE_NAMES}
TOTAL_NAMES = 54

DISCOURSE_PLAYLIST_URL = "https://www.youtube.com/playlist?list=PLZOtgrSp1tzDpF-yqTRcib5F_dlMwccZ8"

DISCOURSE_LINKS = {
    1: "https://youtu.be/tED6qRHTPFU",
    2: "https://youtu.be/xAgLDgGos-Y",
    3: "https://youtu.be/sjt65v9zZWk",
    4: "https://youtu.be/DnVm0J9mS-s",
    5: "https://youtu.be/6yVPTorEr6M",
    6: "https://youtu.be/QBgDfeRmHgo",
    7: "https://youtu.be/JL52QwCnCS8",
    8: "https://youtu.be/Z1bg9vi_jVg",
    9: "https://youtu.be/rlIwlDL_lqI",
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
  <a class="cta-button primary" href="journey-home/index.html">Follow the Journey Home &rarr;</a>
</div>
"""
golu_story_html = page("The Golu Story \u2014 The Journey Home", "golu-story", golu_story_body, depth=0)
with open(os.path.join(ROOT, "golu-story.html"), "w", encoding="utf-8") as f:
    f.write(golu_story_html)

# ------------------------------------------------------------------
# Journey Home overview + 8 stage placeholder pages
# ------------------------------------------------------------------

stage_tiles = []
for num, slug, title in STAGES:
    stage_tiles.append(
        f'<a class="stage-tile" href="{slug}/index.html"><span class="stage-num">{num}</span><span class="stage-name">{title}</span></a>'
    )

journey_overview_body = f"""
<div class="panel">
  <p class="section-title">The Archir\u0101dhi M\u0101rga</p>
  <p>This is the digital companion to the Golu's Sriman Narayana Journey Home display &mdash; the
  soul's path along the Archir\u0101dhi M\u0101rga to Paramapadam, based on Nammalvar's S\u016b\u1e37 Visumbu Pasuram.
  Each of the eight physical QR codes on the display links to one of the stages below.</p>
</div>
<div class="stage-grid">
{''.join(stage_tiles)}
</div>
"""
journey_overview_html = page("Journey Home \u2014 The Journey Home", "journey", journey_overview_body, depth=0)
with open(os.path.join(JOURNEY_DIR, "index.html"), "w", encoding="utf-8") as f:
    f.write(journey_overview_html)

for i, (num, slug, title) in enumerate(STAGES):
    prev_stage = STAGES[i - 1] if i > 0 else None
    next_stage = STAGES[i + 1] if i < len(STAGES) - 1 else None
    prev_link = f'<a href="../{prev_stage[1]}/index.html">&larr; {prev_stage[2]}</a>' if prev_stage else '<a href="../index.html">&larr; Journey overview</a>'
    next_link = f'<a href="../{next_stage[1]}/index.html">{next_stage[2]} &rarr;</a>' if next_stage else '<a href="../index.html">Journey overview &rarr;</a>'

    stage_body = f"""
<article>
  <div class="name-header">
    <span class="pathram-code">Stage {num} of 8</span>
    <p class="meaning-line" style="font-size:1.6rem;">{title}</p>
  </div>
  <div class="panel">
    <p class="section-title">Relevant S\u016b\u1e37 Visumbu Pasuram</p>
    <p><em>Pasuram text coming soon.</em></p>
  </div>
  <div class="panel">
    <p class="section-title">Pasuram Meaning</p>
    <p><em>Content coming soon.</em></p>
  </div>
  <div class="panel">
    <p class="section-title">Simple Explanation</p>
    <p><em>For a general audience, no prior Sri Vaishnava knowledge needed \u2014 content coming soon.</em></p>
  </div>
  <div class="panel">
    <p class="section-title">Deeper Sri Vaishnava Explanation</p>
    <p><em>Content coming soon.</em></p>
  </div>
  <div class="nav-between">
    {prev_link}
    {next_link}
  </div>
</article>
"""
    stage_html = page(f"{title} \u2014 The Journey Home", "journey", stage_body, depth=1)
    stage_folder = os.path.join(JOURNEY_DIR, slug)
    os.makedirs(stage_folder, exist_ok=True)
    with open(os.path.join(stage_folder, "index.html"), "w", encoding="utf-8") as f:
        f.write(stage_html)

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

print(f"Built {len(DIVINE_NAMES)} name pages, {len(STAGES)} journey stage pages, and all top-level pages.")

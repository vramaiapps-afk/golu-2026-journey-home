# Journey Home: intro + 11 pasuram pages, parsed from source/deeper-explanations.md
import re, html as _h, shutil

def _inline(t):
    t = _h.escape(t.strip(), quote=False)
    t = re.sub(r'\*\*\*(.+?)\*\*\*', r'<strong><em>\1</em></strong>', t)
    t = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', t)
    t = re.sub(r'\*(.+?)\*', r'<em>\1</em>', t)
    return t

def _bullets(lines):
    out, sub = [], False
    for ln in lines:
        if re.match(r'^\s{2,}\d+\.', ln):
            if not sub: out.append('<ol>'); sub = True
            out.append('<li>' + _inline(re.sub(r'^\s*\d+\.\s*', '', ln)) + '</li>')
        elif ln.startswith('- '):
            if sub: out.append('</ol></li>'); sub = False
            elif out: out.append('</li>')
            out.append('<li>' + _inline(ln[2:]))
    if sub: out.append('</ol>')
    out.append('</li>')
    return '<ul class="deep-list">' + ''.join(out) + '</ul>'

_src = open(os.path.join(ROOT, "source", "deeper-explanations.md"), encoding="utf-8").read()
_intro_txt = _src.split("## The decad in one frame")[1].split("\n---")[0]
_intro_lines = [l for l in _intro_txt.split("\n") if l.startswith("- ")]
_pas_blocks = re.split(r'\n## Pasuram ', _src)[1:]
PASURAMS = []
for blk in _pas_blocks:
    blk = blk.split("\n---")[0]
    head, *rest = blk.split("\n")
    m = re.match(r'(\d+) — \*(.+?)\*', head)
    n, first = int(m.group(1)), m.group(2)
    reason = [l for l in rest if l.startswith("**Reason given:")][0]
    reason = re.sub(r'^\*\*Reason given:\s*', '', reason).rstrip('*').strip()
    reason = reason.rstrip('"') if reason.count('"') % 2 else reason
    vi = [i for i, l in enumerate(rest) if l.startswith("**Verse")][0]
    verse, flag = [], []
    for l in rest[vi + 1:]:
        if l.startswith("**Deeper"): break
        if l.startswith("*(") : flag.append(l.strip().strip('*').strip('()'))
        elif l.strip(): verse.append(l.strip())
    di = [i for i, l in enumerate(rest) if l.startswith("**Deeper")][0]
    PASURAMS.append(dict(n=n, first=first, reason=re.sub(r'^\*\*|\*\*$', '', _inline(reason)) if False else _inline(reason),
                         verse=verse, flag=flag, deep=_bullets(rest[di + 1:])))
assert len(PASURAMS) == 11, len(PASURAMS)

_table_rows = [l for l in _src.split("The ten \"reasons\" at a glance")[1].split("\n") if re.match(r'^\| \d+ ', l)]
_table = ''.join('<tr>' + ''.join(f'<td>{_inline(c)}</td>' for c in [x.strip() for x in r.strip('|').split('|')]) + '</tr>' for r in _table_rows)

def _pslug(n): return f"pasuram-{n:02d}"

# remove stale placeholder stage folders
for _n, _s, _t in STAGES:
    shutil.rmtree(os.path.join(JOURNEY_DIR, _s), ignore_errors=True)

_tiles = ''.join(
    f'<a class="stage-tile" href="{_pslug(p["n"])}/index.html"><span class="stage-num">{p["n"]}</span><span class="stage-name">{p["first"]}</span></a>'
    for p in PASURAMS)
_intro_items = ''.join('<li>' + _inline(l[2:]) + '</li>' for l in _intro_lines)

_overview = f"""
<div class="panel">
  <p class="section-title">Sūḷ Visumbu &mdash; Thiruvāymoṛi 10.9</p>
  <p>The digital companion to the Golu's Sriman Narayana Journey Home display &mdash; the soul's path along the Archirādhi Mārga to Paramapadam, as shown by Sammāḻārvār in eleven pasurams. Choose a pasuram below.</p>
</div>
<div class="panel">
  <p class="section-title">The decad in one frame</p>
  <ul class="deep-list">{_intro_items}</ul>
</div>
<div class="stage-grid" style="margin-top:22px;">{_tiles}</div>
<div class="panel" style="margin-top:22px;">
  <p class="section-title">The reasons at a glance</p>
  <table class="reasons-table"><thead><tr><th>#</th><th>Word in the verse</th><th>Reason the Lord leads the soul</th></tr></thead><tbody>{_table}</tbody></table>
</div>
<p class="source-note">Source: Dr. Venkatesh Swamin's discourses (Kavasam Connect). Verses are from his recitation; please verify against a printed Divya Prabandham.</p>
"""
with open(os.path.join(JOURNEY_DIR, "index.html"), "w", encoding="utf-8") as f:
    f.write(page("Journey Home — The Journey Home", "journey", _overview, depth=1))

for i, p in enumerate(PASURAMS):
    prv = PASURAMS[i-1] if i > 0 else None
    nxt = PASURAMS[i+1] if i < 10 else None
    pl = f'<a href="../{_pslug(prv["n"])}/index.html">&larr; Pasuram {prv["n"]}</a>' if prv else '<a href="../index.html">&larr; Journey overview</a>'
    nl = f'<a href="../{_pslug(nxt["n"])}/index.html">Pasuram {nxt["n"]} &rarr;</a>' if nxt else '<a href="../index.html">Journey overview &rarr;</a>'
    verse = '<br>'.join(_h.escape(v) for v in p["verse"])
    flags = ''.join(f'<p class="source-note">Please verify &mdash; {_inline(re.sub(r"^(Check|Flag):\s*","",f))}</p>' for f in p["flag"])
    body = f"""
<article>
  <div class="name-header">
    <span class="pathram-code">Pasuram {p['n']} of 11</span>
    <p class="meaning-line" style="font-size:1.6rem;">{p['first']}</p>
  </div>
  <div class="panel">
    <p class="section-title">The Pasuram</p>
    <p class="verse">{verse}</p>
    {flags}
  </div>
  <div class="panel">
    <p class="section-title">Why the Lord leads the soul</p>
    <p>{p['reason']}</p>
  </div>
  <div class="panel">
    <p class="section-title">Simple Explanation</p>
    <p><em>Carried by the audio guide (coming soon).</em></p>
  </div>
  <div class="panel">
    <p class="section-title">Deeper Sri Vaishnava Explanation</p>
    {p['deep']}
  </div>
  <div class="nav-between">{pl}{nl}</div>
</article>
"""
    d = os.path.join(JOURNEY_DIR, _pslug(p["n"]))
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "index.html"), "w", encoding="utf-8") as f:
        f.write(page(f"Pasuram {p['n']} — {p['first']} — The Journey Home", "journey", body, depth=2))

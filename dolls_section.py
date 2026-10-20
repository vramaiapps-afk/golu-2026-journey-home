# "Meet the Perumals" page: one full-view photo + each Perumal explained, top-left to end. English default, Tamil toggle.
# Content lives in assets/golu/perumals.json (edit it and re-run build.py).
import json as _json
_pf = os.path.join(ROOT, "assets", "golu", "perumals.json")
_items = _json.load(open(_pf, encoding="utf-8"))
import html as _html
_cards = []
for _e in _items:
    _cards.append(f"""<section class="pm-card" id="p{_e['n']}">
  <p class="pm-num">{_e['n']}</p>
  <div class="pm-body">
    <h2 class="pm-title"><span class="lang-en">{_html.escape(_e['title_en'])}</span><span class="lang-ta" lang="ta">{_html.escape(_e['title_ta'])}</span></h2>
    <p class="lang-en">{_html.escape(_e['en'])}</p>
    <p class="lang-ta" lang="ta">{_html.escape(_e['ta'])}</p>
  </div>
</section>""")
_jump = "".join(f'<a href="#p{_e["n"]}">{_e["n"]}</a>' for _e in _items)
_dolls_body = f"""
<style>
.pm-toggle{{display:flex;gap:8px;justify-content:center;margin:0 0 14px}}
.pm-toggle button{{font:inherit;padding:8px 18px;border-radius:999px;border:1px solid rgba(201,162,39,.7);background:transparent;color:inherit;cursor:pointer}}
.pm-toggle button[aria-pressed="true"]{{background:#c9a227;color:#2b1a05;font-weight:600}}
body[data-lang="en"] .lang-ta{{display:none}}
body[data-lang="ta"] .lang-en{{display:none}}
.pm-photo{{display:block;width:100%;height:auto;border-radius:10px;border:1px solid rgba(201,162,39,.5)}}
.pm-jump{{display:flex;flex-wrap:wrap;gap:6px;margin-top:12px}}
.pm-jump a{{min-width:34px;text-align:center;padding:6px 8px;border:1px solid rgba(201,162,39,.5);border-radius:8px;text-decoration:none;color:inherit}}
.pm-card{{display:flex;gap:14px;align-items:flex-start;padding:16px;margin-top:14px;border:1px solid rgba(201,162,39,.4);border-radius:12px;background:rgba(255,255,255,.04)}}
.pm-num{{flex:0 0 auto;width:38px;height:38px;border-radius:50%;background:#c9a227;color:#2b1a05;font-weight:700;display:flex;align-items:center;justify-content:center;margin:0}}
.pm-title{{font-size:1.15rem;margin:0 0 6px}}
.pm-body p{{margin:0;line-height:1.6}}
.pm-card:target{{outline:2px solid #c9a227}}
</style>
<div class="panel">
  <div class="pm-toggle" role="group" aria-label="Language">
    <button type="button" id="pm-en" aria-pressed="true">English</button>
    <button type="button" id="pm-ta" aria-pressed="false" lang="ta">தமிழ்</button>
  </div>
  <p class="section-title">Meet the Perum&#257;ls of Our Golu</p>
  <p class="lang-en">The Perum&#257;ls, Th&#257;y&#257;rs, &#256;lw&#257;rs and &#256;ch&#257;ryas on our Golu steps, in order from the top left of the stage. Tap a number to jump to one.</p>
  <p class="lang-ta" lang="ta">எங்கள் கொலுப் படிகளில் உள்ள பெருமாள், தாயார், ஆழ்வார்கள், ஆசார்யர்கள் – மேல் இடப்புறத்திலிருந்து வரிசையாக. ஒரு எண்ணைத் தொட்டால் அதற்குச் செல்லலாம்.</p>
  <a href="../assets/golu/full-view.jpg" target="_blank" rel="noopener"><img class="pm-photo" src="../assets/golu/full-view.jpg" alt="Our Navaratri Golu 2026, full view of all the steps" loading="lazy"/></a>
  <p class="source-note"><span class="lang-en">Tap the photo to enlarge.</span><span class="lang-ta" lang="ta">படத்தைப் பெரிதாகக் காணத் தொடவும்.</span></p>
  <div class="pm-jump">{_jump}</div>
</div>
{''.join(_cards)}
<p class="source-note" style="text-align:center;margin-top:16px;"><span class="lang-en">Details are from the temples' public histories and tradition. Any error in simplifying is entirely ours.</span><span class="lang-ta" lang="ta">விவரங்கள் கோயில்களின் பொது வரலாறு, மரபிலிருந்து எடுக்கப்பட்டவை. எளிமைப்படுத்தலில் ஏதேனும் பிழை இருந்தால் அது எங்களுடையதே.</span></p>
<script>
(function(){{
  var b=document.body,en=document.getElementById('pm-en'),ta=document.getElementById('pm-ta');
  function set(l){{b.setAttribute('data-lang',l);en.setAttribute('aria-pressed',l==='en');ta.setAttribute('aria-pressed',l==='ta');try{{localStorage.setItem('golu-lang',l)}}catch(e){{}}}}
  var s='en';try{{s=localStorage.getItem('golu-lang')||'en'}}catch(e){{}}
  if(location.hash==='#ta')s='ta';
  set(s);en.onclick=function(){{set('en')}};ta.onclick=function(){{set('ta')}};
}})();
</script>
"""
os.makedirs(os.path.join(ROOT, "dolls"), exist_ok=True)
with open(os.path.join(ROOT, "dolls", "index.html"), "w", encoding="utf-8") as _f:
    _f.write(page("Meet the Perumals — The Journey Home", "dolls", _dolls_body, depth=1))

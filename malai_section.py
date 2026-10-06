# Malai Nadu Divya Desam - one QR page: 13 temples in route order (north to south), photo + audio each.
# Photos:  assets/malai-nadu/01.jpg ... 13.jpg      Audio: assets/malai-nadu/audio/01.mp3 ... 13.mp3
MALAI_NADU = [
    ("Thiruvanparisaram", "Kanyakumari", "Thiruvazhmarban"),
    ("Thiruvattar", "Kanyakumari", "Adikesava Perumal"),
    ("Thiruvananthapuram", "Thiruvananthapuram", "Sri Padmanabhaswamy"),
    ("Thiruvalla (Thiruvallavazh)", "Pathanamthitta", "Sri Vallabha (Kolapiran)"),
    ("Thirukkadittanam", "Kottayam", "Adbhuta Narayana Perumal"),
    ("Thiruchengunroor (Chengannur)", "Alappuzha", "Imayavarappan"),
    ("Thiruppuliyur", "Kuttanad, Alappuzha", "Mayapiran"),
    ("Aranmula (Thiruvaranvilai)", "Pathanamthitta", "Parthasarathy"),
    ("Thiruvanvandoor", "Alappuzha", "Pambanaiyappan"),
    ("Thirumoozhikkalam", "Ernakulam", "Lakshmana Perumal"),
    ("Thirukkadkarai (Thrikkakara)", "Ernakulam", "Vamana Moorthy"),
    ("Thiruvithuvakodu", "Palakkad", "Uyyavandha Perumal"),
    ("Thirunavaya", "Malappuram", "Navamukunda Perumal"),
]
assert len(MALAI_NADU) == 13
_cards = []
for i, (name, place, perumal) in enumerate(MALAI_NADU, 1):
    n = f"{i:02d}"
    _cards.append(f"""
<section class="dd-card" id="dd{i}">
  <div class="dd-photo"><span class="dd-ph-num">{i}</span><img src="../assets/malai-nadu/{n}.jpg" style="width:100%;height:100%;object-fit:contain" alt="{perumal}, {name}" loading="lazy" onerror="this.remove()"></div>
  <div class="dd-body">
    <span class="pathram-code">Divya Desam {i} of 13</span>
    <h2 class="dd-name">{i}. {name}</h2>
    <p class="dd-sub">{perumal} &middot; {place}</p>
    <audio controls preload="none" src="../assets/malai-nadu/audio/{n}.mp3" onerror="this.outerHTML='<p class=&quot;source-note&quot;>Audio coming soon.</p>'"></audio>
  </div>
</section>""")
_jump = ''.join(f'<a href="#dd{i}">{i}</a>' for i in range(1, 14))
malai_body = f"""
<div class="panel">
  <p class="section-title">Malai Nadu Divya Desam</p>
  <p>The thirteen sacred Perum&#257;l temples of Kerala and the far south, in order of the pilgrimage route, from the far south to the north. Tap a number to jump to a temple, then press play to listen.</p>
  <a href="../assets/malai-nadu/route-map.png" target="_blank" rel="noopener"><img class="dd-map" style="display:block;width:100%;max-width:100%;height:auto" src="../assets/malai-nadu/route-map.png" alt="Route map of the 13 Malai Nadu Divya Desams" onerror="this.remove()"></a>
  <p class="source-note">Tap the map to enlarge.</p>
  <div class="dd-jump">{_jump}</div>
</div>
{''.join(_cards)}
"""
os.makedirs(os.path.join(ROOT, "malai-nadu"), exist_ok=True)
os.makedirs(os.path.join(ROOT, "assets", "malai-nadu", "audio"), exist_ok=True)
with open(os.path.join(ROOT, "malai-nadu", "index.html"), "w", encoding="utf-8") as f:
    f.write(page("Malai Nadu Divya Desam — The Journey Home", "malai", malai_body, depth=1))

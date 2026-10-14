# Film & Gallery page: the AI film (YouTube embed) + photo/video gallery driven by assets/gallery/gallery.json
FILM_ID = "VWVPO2m6Guc"
_fg_body = f"""
<style>
.fg-video{{position:relative;width:100%;aspect-ratio:16/9;border-radius:12px;overflow:hidden;border:1px solid rgba(201,162,39,.5);background:#000}}
.fg-video iframe{{position:absolute;inset:0;width:100%;height:100%;border:0}}
.fg-grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(210px,1fr));gap:14px;margin-top:14px}}
.fg-item{{margin:0}}
.fg-item img{{width:100%;aspect-ratio:4/3;object-fit:cover;border-radius:8px;border:1px solid rgba(201,162,39,.4);cursor:zoom-in;display:block}}
.fg-item figcaption{{font-size:.9rem;opacity:.85;margin-top:6px}}
.fg-vgrid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:18px;margin-top:14px}}
.fg-vgrid video{{width:100%;border-radius:8px;background:#000}}
.fg-box{{position:fixed;inset:0;background:rgba(0,0,0,.88);display:none;align-items:center;justify-content:center;z-index:50;cursor:zoom-out;padding:16px}}
.fg-box img{{max-width:100%;max-height:100%;border-radius:8px}}
.fg-empty{{font-style:italic;opacity:.8}}
.fg-pgrid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));gap:16px;margin-top:14px}}
.fg-pcard{{display:block;text-decoration:none;color:inherit;border:1px solid rgba(201,162,39,.45);border-radius:10px;overflow:hidden;background:rgba(255,255,255,.5)}}
.fg-pcard img{{width:100%;aspect-ratio:16/9;object-fit:cover;display:block}}
.fg-pcard .y{{font-family:Georgia,serif;font-size:1.5rem;color:#8b1a1a;margin:8px 12px 0}}
.fg-pcard .t{{margin:2px 12px 12px;font-size:.92rem;opacity:.9}}
.panel .source-note a{{color:#8b1a1a;text-decoration:underline}}
</style>

<div class="panel">
  <p class="section-title">The Film &mdash; S&#363;&#7739; Visumbu, imagined</p>
  <div class="fg-video">
    <iframe src="https://www.youtube-nocookie.com/embed/{FILM_ID}" title="The Journey Home film" loading="lazy"
      allow="accelerometer; encrypted-media; picture-in-picture; fullscreen" allowfullscreen></iframe>
  </div>
  <p style="margin-top:14px;">A short film that visualises the journey described in Namm&#257;&#7739;v&#257;r's
  S&#363;&#7739; Visumbu (Thiruv&#257;ymo&#7771;i 10.9): the soul led along the path of light to Vaiku&#7751;&#7789;ha,
  where the Lord and Th&#257;y&#257;r wait to receive it. We made it for this year's Golu using AI video tools.</p>
  <p class="source-note">The images are our imagination, made with AI. They are not a depiction fixed by tradition.
  The meaning of each verse is on the <a href="../journey-home/index.html">Journey Home pages</a>, taken from the discourses of Dr. Venkatesh Swamin.
  Not loading? <a href="https://www.youtube.com/watch?v={FILM_ID}" target="_blank" rel="noopener">Watch on YouTube</a>.</p>
</div>

<div class="panel">
  <p class="section-title">Photos</p>
  <div id="fg-photos" class="fg-grid"><p class="fg-empty">Loading&hellip;</p></div>
</div>

<div class="panel">
  <p class="section-title">Videos</p>
  <div id="fg-videos" class="fg-vgrid"><p class="fg-empty">Loading&hellip;</p></div>
</div>

<div class="panel">
  <p class="section-title">Previous Golus</p>
  <div id="fg-prev" class="fg-pgrid"><p class="fg-empty">Loading&hellip;</p></div>
</div>

<div class="fg-box" id="fg-box"><img id="fg-big" alt=""></div>

<script>
(function(){{
  var esc=function(s){{return String(s||'').replace(/[&<>"]/g,function(c){{return {{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}}[c]}})}};
  var PR=document.getElementById('fg-prev'),P=document.getElementById('fg-photos'),V=document.getElementById('fg-videos'),box=document.getElementById('fg-box'),big=document.getElementById('fg-big');
  box.onclick=function(){{box.style.display='none'}};
  fetch('../assets/gallery/gallery.json',{{cache:'no-cache'}}).then(function(r){{return r.json()}}).then(function(d){{
    var ph=d.photos||[],vd=d.videos||[],pv=d.previous||[];
    PR.innerHTML=pv.length?pv.map(function(x){{var href=x.url||('https://www.youtube.com/watch?v='+encodeURIComponent(x.youtube));var img=x.cover?('../assets/gallery/photos/'+encodeURI(x.cover)):(x.youtube?'https://i.ytimg.com/vi/'+encodeURIComponent(x.youtube)+'/hqdefault.jpg':'');return '<a class="fg-pcard" href="'+esc(href)+'" target="_blank" rel="noopener">'+(img?'<img loading="lazy" src="'+img+'" alt="">':'')+'<div class="y">'+esc(x.year)+'</div><div class="t">'+esc(x.title)+' &rarr;</div></a>'}}).join(''):'<p class="fg-empty">Coming soon.</p>';
    P.innerHTML=ph.length?ph.map(function(p){{return '<figure class="fg-item"><img loading="lazy" src="../assets/gallery/photos/'+encodeURI(p.file)+'" alt="'+esc(p.caption)+'" data-full="1">'+(p.caption?'<figcaption>'+esc(p.caption)+'</figcaption>':'')+'</figure>'}}).join(''):'<p class="fg-empty">Photos coming soon.</p>';
    V.innerHTML=vd.length?vd.map(function(v){{
      var cap=v.caption?'<p style="margin:6px 0 0;font-size:.9rem;opacity:.85">'+esc(v.caption)+'</p>':'';
      if(v.youtube)return '<div><div class="fg-video"><iframe loading="lazy" src="https://www.youtube-nocookie.com/embed/'+encodeURIComponent(v.youtube)+'" allowfullscreen></iframe></div>'+cap+'</div>';
      return '<div><video controls preload="metadata" src="../assets/gallery/videos/'+encodeURI(v.file)+'"></video>'+cap+'</div>';
    }}).join(''):'<p class="fg-empty">Videos coming soon.</p>';
    P.querySelectorAll('img[data-full]').forEach(function(im){{im.onclick=function(){{big.src=im.src;big.alt=im.alt;box.style.display='flex'}}}});
  }}).catch(function(){{PR.innerHTML='<p class="fg-empty">Coming soon.</p>';P.innerHTML='<p class="fg-empty">Photos coming soon.</p>';V.innerHTML='<p class="fg-empty">Videos coming soon.</p>'}});
}})();
</script>
"""
os.makedirs(os.path.join(ROOT, "gallery"), exist_ok=True)
with open(os.path.join(ROOT, "gallery", "index.html"), "w", encoding="utf-8") as f:
    f.write(page("Film & Gallery — The Journey Home", "gallery", _fg_body, depth=1,
                 description="The Journey Home film and photos from our Navaratri Golu 2026."))
os.makedirs(os.path.join(ROOT, "assets", "gallery", "photos"), exist_ok=True)
os.makedirs(os.path.join(ROOT, "assets", "gallery", "videos"), exist_ok=True)
_gj = os.path.join(ROOT, "assets", "gallery", "gallery.json")
if not os.path.exists(_gj):
    with open(_gj, "w", encoding="utf-8") as f:
        f.write('{\n  "previous": [],\n  "photos": [],\n  "videos": []\n}\n')

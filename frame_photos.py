# Frames every photo in orig/NN.jpg to the same size + border -> site assets/malai-nadu/NN.jpg
import glob, os
from PIL import Image, ImageDraw
W,H=900,1125; INDIGO=(23,26,53); GOLD=(201,162,39); GOLDL=(230,199,101)
OUT="/home/claude/site2/assets/malai-nadu"
for p in sorted(glob.glob("/home/claude/mm/orig/*.jpg")):
    n=os.path.basename(p)
    im=Image.open(p).convert("RGB")
    pad=44                                   # constant border thickness
    bw,bh=W-2*pad,H-2*pad
    s=min(bw/im.width,bh/im.height)
    im=im.resize((round(im.width*s),round(im.height*s)),Image.LANCZOS)
    c=Image.new("RGB",(W,H),INDIGO); d=ImageDraw.Draw(c)
    d.rectangle([8,8,W-9,H-9],outline=GOLD,width=6)
    d.rectangle([22,22,W-23,H-23],outline=GOLDL,width=2)
    c.paste(im,((W-im.width)//2,(H-im.height)//2))
    c.save(os.path.join(OUT,n),quality=90)
    print(n,"->",im.size)

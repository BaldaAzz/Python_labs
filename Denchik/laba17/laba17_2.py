from PIL import Image, ImageDraw

image = Image.new('RGB',(200,200), (43,141,36))
idraw = ImageDraw.Draw(image)
idraw.rectangle((0,0,200,100),fill=(127,199,255))
idraw.rectangle((60,70,140,150),fill=(245, 245, 180), outline=(0,0,0))
idraw.rectangle((70,120,90,150),fill=(180,112,0), outline=(0,0,0))
idraw.ellipse((82,135,86,140),fill=(255,215,0),outline=(0,0,0))
idraw.polygon((60,70,140,70,100,50),fill=(255,10,10))
idraw.line((60,70,100,50),fill=(0,0,0))
idraw.line((140,70,100,50),fill=(0,0,0))
idraw.line((60,70,140,70),fill=(0,0,0))
image.save('Denchik/laba17/img/house.png')
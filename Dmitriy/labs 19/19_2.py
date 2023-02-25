from PIL import Image, ImageDraw
img = Image.new("RGB", (300,300),(255,255,255))
draw = ImageDraw.Draw(img)
draw.ellipse((0,0,150,150), fill = "black", outline = "black")
draw.rectangle((155,10,300,145), fill = "black")
draw.polygon([(150,150), (200, 300), (100,300)], fill = "black")
img.show()

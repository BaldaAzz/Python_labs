from wand.image import Image
from wand.color import Color
from wand.drawing import Drawing
from wand.display import display
from wand.image import BaseImage


img = Image(width=500, height=500, background=Color("white"))
draw = Drawing()

draw.stroke_color = Color("black")
draw.fill_color = Color("black")

draw.circle((250, 250), (250, 270))
draw.circle((125, 370), (125, 390))
draw.circle((410, 270), (410, 290))
draw.circle((200, 100), (200, 120))

draw.fill_color = Color("none")
draw.stroke_width = 6

draw.ellipse((250, 250), (80, 200), rotation=(0, 360))

draw.draw(img)
img.save(filename="Denchik/laba19Var2/laba19_1.bmp")
draw.clear()
img.rotate(60)
draw.stroke_color = Color("black")
draw.fill_color = Color("none")
draw.stroke_width = 6

draw.ellipse((350, 350), (80, 200), rotation=(0, 360))

draw.draw(img)
img.save(filename="Denchik/laba19Var2/laba19_1.bmp")
draw.clear()
img.rotate(60)
draw.stroke_color = Color("black")
draw.fill_color = Color("none")
draw.stroke_width = 6

draw.ellipse((470, 470), (80, 200), rotation=(0, 360))

draw.draw(img)
img.rotate(240)
img.save(filename="Denchik/laba19Var2/laba19_1.bmp")

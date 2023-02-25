from wand.image import Image as Wandlmage
from wand.color import Color
from wand.drawing import Drawing
from wand.display import display
img = Wandlmage(width = 300, height = 300, background = Color("white"))
draw = Drawing()
draw.stroke_color = Color("black")
draw.fill_color = Color("black")
draw.ellipse((60, 60), (60,60))
draw.draw(img)
draw.rectangle(left = 130, top = 0 , right = 250, bottom = 120)
draw.draw(img)
draw.polygon( [ (500, 150), (350, 50), (350, 250), (30, 200)])
draw.draw(img)
display(img)

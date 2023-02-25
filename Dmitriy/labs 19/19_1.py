from wand.image import Image as Wandlmage
from wand.color import Color
from wand.drawing import Drawing
from wand.display import display

img = Wandlmage(width=400, height=400, background=Color("white"))
draw = Drawing()
draw.stroke_color = Color("black")
draw.fill_color = Color("white")

def pricel():
    draw.stroke_width = 3
    draw.ellipse((230, 80), (60, 60))
    draw.draw(img)

    draw.stroke_width = 1
    draw.ellipse((230, 80), (45, 45))
    draw.draw(img)

    draw.stroke_width = 1
    draw.stroke_opacity = 0.5
    draw.line((230, 0), (230, 160))
    draw.draw(img)

    draw.stroke_opacity = 1
    draw.stroke_width = 3
    draw.line((230, 0), (230, 60))
    draw.draw(img)

    draw.line((230, 100), (230, 160))
    draw.draw(img)

    draw.stroke_width = 1
    draw.stroke_opacity = 0.5
    draw.line((140, 80), (320, 80))
    draw.draw(img)

    draw.stroke_width = 3
    draw.stroke_opacity = 1
    draw.line((140, 80), (210, 80))
    draw.draw(img)

    draw.line((250, 80), (320, 80))
    draw.draw(img)

    draw.line((215, 80), (225, 80))
    draw.draw(img)

    draw.line((235, 80), (245, 80))
    draw.draw(img)
    
    draw.line((230, 65), (230, 75))
    draw.draw(img)

    draw.line((230, 85), (230, 95))
    draw.draw(img)
    display(img)
pricel()


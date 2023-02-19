from wand.image import Image as Wandlmage
from wand.color import Color
from wand.drawing import Drawing

img = Wandlmage(height=400, width=400, background=Color('white'))
draw = Drawing()
draw.fill_color = Color('white')
draw.stroke_color = Color('black')

center = (200, 200)

circlies = {3: (80, 80),
            2: (100, 100)}



for i, j in circlies.items():
    print(i)
    draw.stroke_width = i
    draw.circle(center, j)
    draw.draw(img)



img.save(filename='sdfs.bmp')
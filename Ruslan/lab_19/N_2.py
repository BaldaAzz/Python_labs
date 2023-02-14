from wand.image import Image as Wandlmage
from wand.color import Color
from wand.drawing import Drawing
from wand.display import display

center_coords = (200, 200)
            # Толщина: радиус
circles = {2: (80, 80),
           3: (100, 100)}
            # Толщина: (Начало, конец)
lines = {1: (((30, 200), (370, 200)), 
             ((200, 30), (200, 370))),
         3: (((30, 200), (130, 200)),
             ((200, 30), (200, 370)),
             ((200, 30), (200, 130)),
             ((200, 270), (200, 370)),
             ((180, 200), (190, 200)),
             ((210, 200), (220, 200)),
             ((200, 180), (200, 190)),
             ((200, 210), (200, 220)))}

img = Wandlmage(height=400, width=400, background=Color('white'))
draw = Drawing()
draw.fill_color = Color('white')
draw.stroke_color = Color('black')

for sk_width, radius in circles.items():
    print(radius, sk_width)
    draw.stroke_width = sk_width
    draw.ellipse(center_coords, radius)
# draw.stroke_width = 3
# draw.ellipse((200, 200), (100, 100))
# draw.stroke_width = 2
# draw.ellipse((200, 200), (80, 80))

# draw.stroke_width = 1
# draw.line((30, 200), (370, 200))
# draw.line((200, 30), (200, 370))

# draw.stroke_width = 3
# draw.line((30, 200), (130, 200))
# draw.line((270, 200), (370, 200))

# draw.line((200, 30), (200, 130))
# draw.line((200, 270), (200, 370))

# draw.line((180, 200), (190, 200))
# draw.line((210, 200), (220, 200))
# draw.line((200, 180), (200, 190))
# draw.line((200, 210), (200, 220))
draw.draw(img)
display(img)
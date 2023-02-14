from wand.image import Image as Wandlmage
from wand.color import Color
from wand.drawing import Drawing
from wand.display import display

radius = (15, 15)
ellipsis_coords = {1: ((30, 50), (30, 110), (30, 170)), 
                   2: ((150, 40), (150, 90), (150, 140), (150, 190)),
                   3: ((270, 90), (270, 140))}

                 # Коорд. начала линии: коорд. конца линии  
lines_coords = {((45, 50), (45, 110), (45, 170)): ((135, 40), (135, 90), (135, 140), (135, 190)),
                ((165, 40), (165, 90), (165, 140), (165, 190)): ((255, 90), (255, 140))}

img = Wandlmage(width=300, height=300, background=Color('white'))
draw = Drawing()
draw.stroke_color = Color('green')
draw.stroke_width = 3
draw.fill_color = Color('white')


for i in ellipsis_coords.values():
    for coords in i:
      draw.ellipse(coords, radius) 

for start, finish in lines_coords.items():
    for i in start:
        for j in finish:
            draw.line(i, j)

draw.draw(img)
display(img)             

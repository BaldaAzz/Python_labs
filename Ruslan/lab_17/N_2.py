from PIL import Image, ImageDraw


triengle = ((80, 200, 200, 50),
          (200, 50, 320, 200),
          (320, 200, 80, 200))

regtangles = {'yellow': (100, 200, 300, 350),
              'blue': (180,250, 220, 300)}
 

img = Image.new('RGBA', (400, 400), 'white')
idraw = ImageDraw.Draw(img)

for coord in triengle:
    idraw.line(coord, fill='red')

for color, coord in regtangles.items():
    idraw.rectangle(coord, fill=color)

img.save(r'img\house.png')

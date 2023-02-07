from PIL import Image, ImageDraw, ImageFont, ImageFilter

my_dict = { # цвет, координаты медуз, градус поворота, назв. для сохранения
    'синий': ((30, 15, 190, 380), 50, 'blue'),          
    'розовый': ((180, 80, 340, 445), 90, 'pink'),
    'зелёный': ((340, 30, 510, 430), 135, 'green')
}

image = Image.open(r'ЛР 17\медуза.jpg')
font = ImageFont.truetype('arial.ttf', size=18)

for color, param in my_dict.items():
    medusa = image.crop(param[0])
    medusa = medusa.rotate(param[1])
    medusa = medusa.filter(ImageFilter.BLUR)

    idraw = ImageDraw.Draw(medusa)
    idraw.text((20, 330), color, font=font)
    medusa.save(f'img\{param[2]}_medusa.jpg')


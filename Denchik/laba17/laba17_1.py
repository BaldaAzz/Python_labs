from PIL import Image, ImageDraw, ImageFont, ImageFilter

image = Image.open('Denchik/laba17/img/Медуза.jpg')
cropped_img = image.crop((0, 20, 200, 400))
idraw = ImageDraw.Draw(cropped_img)
texts = 'Blue'
font = ImageFont.truetype('arial.ttf', size=100)
idraw.text((25, 350), texts, fill='Blue')
cropped_img_rotate = cropped_img.rotate(50)
cropped_img_filter = cropped_img.filter(ImageFilter.MedianFilter)
cropped_img.save('Denchik/laba17/img/Blue.png')
cropped_img_rotate.save('Denchik/laba17/img/BlueRotade.png')
cropped_img_filter.save('Denchik/laba17/img/BlueFilter.png')
...
image = Image.open('Denchik/laba17/img/Медуза.jpg')
cropped_img = image.crop((175, 100, 340, 400))
idraw = ImageDraw.Draw(cropped_img)
texts = 'Pink'
font = ImageFont.truetype('arial.ttf', size=100)
idraw.text((25, 280), texts, fill='Pink')
cropped_img_rotate = cropped_img.rotate(135)
cropped_img_filter = cropped_img.filter(ImageFilter.BLUR)
cropped_img.save('Denchik/laba17/img/Pink.png')
cropped_img_rotate.save('Denchik/laba17/img/PinkRotade.png')
cropped_img_filter.save('Denchik/laba17/img/PinkFilter.png')
...
image = Image.open('Denchik/laba17/img/Медуза.jpg')
cropped_img = image.crop((335, 30, 520, 370))
idraw = ImageDraw.Draw(cropped_img)
texts = 'Green'
font = ImageFont.truetype('arial.ttf', size=100)
idraw.text((25, 280), texts, fill='Green')
cropped_img_rotate = cropped_img.rotate(90)
cropped_img_filter = cropped_img.filter(ImageFilter.UnsharpMask)
cropped_img.save('Denchik/laba17/img/Green.png')
cropped_img_rotate.save('Denchik/laba17/img/GreenRotade.png')
cropped_img_filter.save('Denchik/laba17/img/GreenFilter.png')
...

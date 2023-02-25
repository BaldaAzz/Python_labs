from PIL import Image, ImageFilter, ImageDraw ,ImageFont

image = Image.open('labs 17/PythonApplication17_1/meduza.jpg')

#Синяя медуза
def blue():
    cropped = image.crop((0, 0, 200, 400))
    cropped.save('labs 17/PythonApplication17_1/cropped_Медуза1.jpg')
    cropped1 = Image.open('labs 17/PythonApplication17_1/cropped_Медуза1.jpg')
    rotated = cropped.rotate(50)
    rotated.save('labs 17/PythonApplication17_1/rotated_Медуза1.jpg')
    blur1 = Image.open('labs 17/PythonApplication17_1/rotated_Медуза1.jpg')
    blur1 = cropped1.filter(ImageFilter.BLUR)
    idraw = ImageDraw.Draw(blur1)
    text = "blue"
    font = ImageFont.truetype("arial.ttf",size = 18)
    idraw.text((10,350),text, fill ='blue')
    blur1.save('labs 17/PythonApplication17_1/full_Медуза1.jpg')

#Розовая медуза    
def pink():
    cropped = image.crop((175, 0, 350, 400))
    cropped.save('labs 17/PythonApplication17_1/cropped_Медуза2.jpg')
    cropped2 = Image.open('labs 17/PythonApplication17_1/cropped_Медуза2.jpg')
    rotated = cropped.rotate(150)
    rotated.save('labs 17/PythonApplication17_1/rotated_Медуза2.jpg')
    blur2 = Image.open('labs 17/PythonApplication17_1/rotated_Медуза2.jpg')
    blur2 = cropped2.filter(ImageFilter.BLUR)
    idraw = ImageDraw.Draw(blur2)
    text = "pink"
    font = ImageFont.truetype("arial.ttf",size = 18)
    idraw.text((10,350),text, fill ='pink')
    blur2.save('labs 17/PythonApplication17_1/full_Медуза2.jpg')

#Зеленая медуза
def green():
    cropped = image.crop((350, 0, 500, 400))
    cropped.save('labs 17/PythonApplication17_1/cropped_Медуза3.jpg')
    cropped3 = Image.open('labs 17/PythonApplication17_1/cropped_Медуза3.jpg')
    rotated = cropped.rotate(90)
    rotated.save('labs 17/PythonApplication17_1/rotated_Медуза3.jpg')
    blur3 = Image.open('labs 17/PythonApplication17_1/rotated_Медуза3.jpg')
    blur3 = cropped3.filter(ImageFilter.BLUR)
    idraw = ImageDraw.Draw(blur3)
    text = "green"
    font = ImageFont.truetype("arial.ttf",size = 18)
    idraw.text((10,350),text, fill ='green')
    blur3.save('labs 17/PythonApplication17_1/full_Медуза3.jpg')
    
blue()
pink()
green()


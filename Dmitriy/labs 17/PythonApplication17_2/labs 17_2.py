from PIL import Image, ImageDraw

dom = Image.new('RGB', (500, 500), 'white')
draw = ImageDraw.Draw(dom)

draw.rectangle((40,200,240,320), fill='lightgreen' ,outline='Black') 
draw.rectangle((76,96,104,184), fill='darkseagreen') 
draw.polygon((40,200,140,80,240,200), fill='Brown', outline='Black') 
draw.rectangle((64,220,110,272),fill='Cyan', outline='White') 
draw.rectangle((168,220,220,272),fill='Cyan', outline='White') 
draw.rectangle((115,252,160,320),fill='red', outline='Orange')
dom.save('labs 17/PythonApplication17_2/дом_мечты.jpg')
dom.show()

# don't use this it's a bogus scratch file

from PIL import Image, ImageDraw, ImageFont

img = Image.new('RGB', (60, 30), color='red')
img.save('pil_red.png')

fnt = ImageFont.truetype('/Library/Fonts/Impact.ttf', 18)

im2 = Image.open('./pil_red.png')
d = ImageDraw.Draw(im2)
d.text((10, 10), 'Hello World', font=fnt, fill=(255, 255, 0))

im2.save('pil_text.png')

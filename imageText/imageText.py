from PIL import Image, ImageDraw, ImageFont

class Captioner:
    def __init__(self):
        self.font = ImageFont.truetype('./Impact.ttf', 18)
        self.fontFill = (255, 255, 255)

    def open_image(self, path):
        return Image.open(path)

    def write(self, pic, text, xPosition, yPosition):
        writer = ImageDraw.Draw(pic)
        ##FIXME this should accept font & fill args as below, but it keeps throwing an error for some reason...
       ##  writer.text = ((10, 10), 'Hello World', font=self.font, fill=(255,255,255))
        return pic

    def save_image(self, pic, fname):
        pic.save(fname)

from PIL import Image, ImageDraw, ImageFont


class Captioner:
    def __init__(self, path):
        self.image = Image.open(path)
        self.font = ImageFont.truetype('./Impact.ttf', 18)
        self.fontFill = (255, 255, 255)

    def write(self, text, xPosition, yPosition):
        writer = ImageDraw.Draw(self.image)
        ##FIXME this should accept font & fill args as below, but it keeps throwing an error for some reason...
       ##  writer.text = ((10, 10), 'Hello World', font=self.font, fill=(255,255,255))
        return self.image

    def save_image(self, fname):
        self.image.save(fname)

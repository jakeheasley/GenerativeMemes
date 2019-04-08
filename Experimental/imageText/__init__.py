from PIL import Image, ImageDraw, ImageFont
import io

default_font_size = 36
default_font = ImageFont.truetype('./Impact.ttf', default_font_size)
default_font_fill = (0, 0, 0)


def writeText(text, image, xPosition, yPosition, fill=default_font_fill):
    """writes input text on input image at given x/y coordinates
    @:param text: string to be written
    @:param image: image to be written on
    @:param xPosition: x coordinate to start writing
    @:param yPosition: y coordinate to start writing
    @:param fill: optionally specify a text color
    """
    writer = ImageDraw.Draw(image)
    coordinates = (xPosition, yPosition)
    writer.text(coordinates, text, font=default_font, fill=fill)
    return image


def open_image(filepath):
    """opens image located at given filepath and returns as PIL.Image.Image object
    @:param filepath: path to the image to open.
    #TODO: how do we incorporate pathlib//make this cross-platform?
    @:return PIL.Image.Image image object"""
    return Image.open(filepath, 'r')

def open_image(blob):
    """opens image from blob data retrieved from mySQL server"""
    # TODO: make this work
    wrappedimage = io.BytesIO(blob)
    return Image.open(wrappedimage)


def save_image(img, fp=None):
    """writes PIL.Image.Image object to disk as a jpg
    @:param img: PIL.Image.Image object. use after writeText()
    """
    if fp is None:
        fp = img.filename + "_caption.jpg"
        img.save(fp)
    else:
        img.save(fp)


def caption(imgpath, text, xPosition=None, yPosition=None):
    img = open_image(imgpath)
    if xPosition is None:
        xPosition = (img.__getstate__()[2][0]) / 2
    if yPosition is None:
        yPosition = (img.__getstate__()[2][1]) / 2
    captionedImage = writeText(text, img, xPosition, yPosition)
    save_image(captionedImage)

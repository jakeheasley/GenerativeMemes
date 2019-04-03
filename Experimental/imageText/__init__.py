from PIL import Image, ImageDraw, ImageFont

default_font_size = 18
default_font = ImageFont.truetype('./Impact.ttf', default_font_size)
default_font_fill = (255, 255, 255)


def writeText(text, image, xPosition, yPosition):
    """writes input text on input image at given x/y coordinates"""
    # ToDo: make x & y args optional, center text in image if no x/y args are given.
    writer = ImageDraw.Draw(image)
    writer.text(xPosition, yPosition, text, font=default_font, fill=default_font_fill)
    return writer

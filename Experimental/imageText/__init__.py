from PIL import Image, ImageDraw, ImageFont
import io

default_font_size = 36
default_font = ImageFont.truetype('./Impact.ttf', default_font_size)
default_font_fill = (255, 255, 255)
default_rectangle_fill = (0, 0, 0)


def open_image(filepath):
    """opens image located at given filepath and returns as PIL.Image.Image object
    @:param filepath: path to the image to open.
    #TODO: how do we incorporate pathlib//make this cross-platform?
    @:return PIL.Image.Image image object"""
    return Image.open(filepath, 'r')


def open_blob(blob):
    """opens image from blob data retrieved from mySQL server"""
    # TODO: make this work
    wrappedimage = io.BytesIO(blob)
    return Image.open(wrappedimage)


def save_image(img, fp=None):
    """writes PIL.Image.Image object to disk as a jpg
    @:param img: PIL.Image.Image object. use after write_text()
    """
    if fp is None:
        fp = img.filename + "_caption.jpg"
        img.save(fp)
    else:
        img.save(fp)


def write_text(text, image, xposition, yposition, fill=default_font_fill):
    """writes input text on input image at given x/y coordinates
    @:param text: string to be written
    @:param image: image to be written on
    @:param xposition: x coordinate to start writing
    @:param yposition: y coordinate to start writing
    @:param fill: optionally specify a text color
    """
    writer = ImageDraw.Draw(image)
    coordinates = (xposition, yposition)
    writer.text(coordinates, text, font=default_font, fill=fill)
    return image


def overwrite_text(image, xmin, xmax, ymin, ymax, fill=default_rectangle_fill):
    """draws a rectangle at given coordinates on given image. Useful for overwriting existing meme text.
    @:param image: PIL.Image.Image object
    @:param xmin, xmax, ymin, ymax: coordinates of the rectangle to be drawn
    @:param fill: optionally specify a fill color"""
    draw = ImageDraw.Draw(image)
    draw.rectangle(((xmin, ymin), (xmax, ymax)), fill=fill)
    return image


def caption(imgpath, text, xposition=None, yposition=None):
    img = open_image(imgpath)
    if xposition is None:
        xposition = (img.__getstate__()[2][0]) / 2
    if yposition is None:
        yposition = (img.__getstate__()[2][1]) / 2
    captioned_image = write_text(text, img, xposition, yposition)
    save_image(captioned_image)

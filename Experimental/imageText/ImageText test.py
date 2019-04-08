import imageText as it
from PIL import Image
import pathlib

# example usage for imageText module

imgPath = pathlib.Path("./a_Meme.jpg")

# theMeme = Image.open(imgPath, 'r')
#
# captionedMeme = it.writeText("Hello World", theMeme, 100, 100, fill=(0, 0, 0))
# theMeme.save('a_Meme_w_caption.jpg')

it.caption(imgPath, "aaaaaaaaaaaaaaaa")

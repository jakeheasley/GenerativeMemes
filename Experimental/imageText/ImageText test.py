import imageText as it
from PIL import Image
import pathlib

# example usage for imageText module

imgPath = pathlib.Path("./a_Meme.jpg")

# theMeme = Image.open(imgPath, 'r')
#
# captionedMeme = it.write_text("Hello World", theMeme, 100, 100, fill=(0, 0, 0))
# theMeme.save('a_Meme_w_caption.jpg')

# it.caption(imgPath, "aaaaaaaaaaaaaaaa")

foo = it.open_image(imgPath)
it.overwrite_text(foo, 500, 1000, 600, 670)
it.write_text("aaaaaaa", foo, 500, 600)
it.save_image(foo)

# it.overwrite_text(imgPath, 500, 1000, 600, 670)
# it.caption(imgPath, "aaaaaaaaaa", 500, 600)

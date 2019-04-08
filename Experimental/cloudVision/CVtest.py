import cloudVision.cvImageProcessor

# example usage for instantiating and using cvImageProcessor.CV object.


cv = cloudVision.cvImageProcessor.CV()

meme = cv.open_image(input('enter a filepath: '))

memetext = cv.run_ocr(meme, 'text')

memetags = cv.tag_image(meme, 'brief')

print(meme)
print(memetext)
print(memetags)


import cloudVision.cvImageProcessor

# example usage for instantiating and using cvImageProcessor.CV object.


cv = cloudVision.cvImageProcessor.CV()

meme = cv.openImage(input('enter a filepath: '))

memetext = cv.runOCR(meme, 'text')

memetags = cv.tagImage(meme, 'brief')

print(meme)
print(memetext)
print(memetags)


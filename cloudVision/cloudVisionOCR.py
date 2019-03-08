from google.cloud import vision
from google.cloud.vision import types

client = vision.ImageAnnotatorClient.from_service_account_file('/Users/richardgraham/Sources/GenerativeMemes/cloudVision/Meme Generator-802734cd5cac.json')

# img = '/Volumes/GoogleDrive/My Drive/3. COMP 225/MEME VAULT/fish joint.jpg'
img = input('enter filepath to image: ')

with open(img, 'rb') as inputImage:
    content = inputImage.read()

visionImage = vision.types.Image(content=content)
text_response = client.text_detection(image=visionImage)

alltext = [text.description for text in text_response.text_annotations]

print(text_response)
print(alltext[0])
# testing/prototyping for cvImageProcessor.py.
#
# Don't look here for functionality.

from google.cloud import vision
from google.cloud.vision import types
from google.protobuf.json_format import MessageToDict

client = vision.ImageAnnotatorClient.from_service_account_file('Meme Generator-802734cd5cac.json')

# img = '/Volumes/GoogleDrive/My Drive/3. COMP 225/MEME VAULT/fish joint.jpg'
img = input('enter filepath to image: ')

with open(img, 'rb') as inputImage:
    content = inputImage.read()

visionImage = vision.types.Image(content=content)
recogResponse = client.web_detection(image=visionImage)
print("#########################################################")
print(recogResponse)
print("#########################################################")

recogContent = recogResponse.web_detection
print("#########################################################")
print(recogContent.best_guess_labels)
print("#########################################################")

foo = [recogContent.web_entities]

from google.cloud import vision

client = vision.ImageAnnotatorClient.from_service_account_file('/Users/richardgraham/Sources/GenerativeMemes/cloudVision/Meme Generator-802734cd5cac.json')

def openImage(path):
    with open(path, 'rb') as imageFile:
        image_data = imageFile.read()
    return image_data


def runOCR(image):
    vision_image = vision.types.Image(content=image)
    text_response = client.text_detection(image=vision_image)
    output = [text.description for text in text_response.text_annotations]
    return output[0]


def findText(imagefile):
    openImage(imagefile)
    return runOCR()

def cleanOutput(proto):
    # TODO: format web_entities field to prepare for database entry
    # googleCV returns 'RepeatedCompositeContainer' type objects. use the
    # google.protobuf.json_format module to clean this data into a dict
    # or something else usable by python
    return

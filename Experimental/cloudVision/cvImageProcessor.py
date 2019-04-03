from google.cloud import vision


client = vision.ImageAnnotatorClient.from_service_account_file('/Users/richardgraham/Sources/GenerativeMemes/cloudVision/Meme Generator-802734cd5cac.json')


def openImage(path):
    """open a given file and return its data for processing"""
    with open(path, 'rb') as imageFile:
        image_data = imageFile.read()
    return image_data


def runOCR(imgdata):
    """takes in image data, sends it to Google CV for OCR, returns text in the image"""
    vision_image = vision.types.Image(content=imgdata)
    text_response = client.text_detection(image=vision_image)
    output = [text.description for text in text_response.text_annotations]
    return output[0]


def findText(imagefile):
    """wrapper function for runOCR and openImage to be run from one function call."""
    pic = openImage(imagefile)
    return runOCR(pic)


def cleanOutput(self, proto):
    """receives google protocol buffer object containing descriptive information
    about an image, converts the protobuf info to lists and strings for Python to
    use."""
    # TODO: format web_entities field to prepare for database entry
    # googleCV returns 'RepeatedCompositeContainer' type objects. use the
    # google.protobuf.json_format module to clean this data into a dict
    # or something else usable by python
    # https://stackoverflow.com/questions/19734617/protobuf-to-json-in-python
    return

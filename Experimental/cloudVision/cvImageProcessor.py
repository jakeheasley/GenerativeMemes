from google.cloud import vision
from pathlib import Path


class CV:

    def __init__(self):
        self.client = vision.ImageAnnotatorClient.from_service_account_file("./GCV_login.json")

    def open_image(self, path):
        """open a given file and return its data for processing
        @:param path: filepath to open
        @:return vision_image: vision.types.Image - this seems to be different than normal image binary"""
        with open(path, 'rb') as imageFile:
            image_data = imageFile.read()
        vision_image = vision.types.Image(content=image_data)
        return vision_image

    def open_blob(self, blob):
        """convert binary image data for GCV.
        @:param blob: binary image data, i.e. from python's standard open() method. TODO: or from SQL?
        @:return vision.types.Image - this seems to be different than normal image binary"""
        return vision.types.Image(content=blob)

    def run_ocr(self, imgdata, mode='text'):
        """takes in image data, sends it to Google CV for OCR, returns text in the image
        @:param imgdata: google.cloud.vision.types.Image object
        @:param mode: can be either 'text' or 'full'.
        text (default) returns only the OCR text. full returns OCR text accompanied by bounding box.
        @:return for 'text' mode: a string of all text recognized in the image
        @:return for 'full' mode: a protobuf (?) object containing recognized text
        and the coordinates of its bounding box in the image. useful for replacing text."""

        # ToDo: format protobuf output for 'full' mode so that it doesn't deliver
        #  4000 lines of information that we don't need.

        text_response = self.client.text_detection(image=imgdata)
        text_only = [text.description for text in text_response.text_annotations]
        if mode == 'text':
            return text_only[0]
        elif mode == 'full':
            return text_response

    def tag_image(self, imgdata, mode='brief'):
        """takes in image data, sends it to Google CV for image recognition,
        returns list of tagged objects.
        @:param imgdata: google.cloud.vision.types.Image object.
        @:param mode: can either be 'brief' or 'full'.
        'brief' (default) returns only the best guess at what the image is and the language if recognized.
        'full' returns a full list of tags and their match scores
        along with URLs and page names of locations with exact matches, partial matches, and visually similar images.
        Some of these may be useful for database entry."""
        recog_response = self.client.web_detection(image=imgdata)
        output = recog_response.web_detection.best_guess_labels
        if mode == 'brief':
            return output
        elif mode == 'full':
            return recog_response

    def clean_output(self, proto):
        """receives google protocol buffer object containing descriptive information
        about an image, converts the protobuf info to lists and strings for Python to
        use."""
        # TODO: format web_entities field to prepare for database entry
        #   googleCV returns 'RepeatedCompositeContainer' type objects. use the
        #   google.protobuf.json_format module to clean this data into a dict
        #   or something else usable by python
        #   https://stackoverflow.com/questions/19734617/protobuf-to-json-in-python
        return

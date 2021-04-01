import cv2


class ContourFinder :
    def __init__(self, image):
        self.img = image
        pass

    def findContours(self):
        a = cv2.findContours(self.img)

# https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_contours/py_table_of_contents_contours/py_table_of_contents_contours.html

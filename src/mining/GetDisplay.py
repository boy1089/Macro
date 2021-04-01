
from PIL import ImageGrab
import numpy as np

class GetDisplay:

    def __init__(self):
        self.img = np.zeros([1, 1, 3])
        pass

    def grabDisplay(self):
        self.img = ImageGrab.grab()
        pass

    def img(self):
        return self.img

    def getSize(self):
        self.grabDisplay()
        return self.img.width, self.img.height


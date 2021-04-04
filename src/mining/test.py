import cv2
from PIL import ImageGrab
import matplotlib.pyplot as plt
import numpy as np

from PyQt5 import QtGui

a = ImageGrab.grab()
img = np.asarray(a)
w, h, c = img.shape
qImg = QtGui.QImage(img, w, h, w, QtGui.QImage.Format_RGB888)

pixmap = QtGui.QPixmap.fromImage(qImg)


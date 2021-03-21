import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
from PIL import ImageGrab


img = ImageGrab.grab()
img = np.asarray(img)[0:500, 0:500]
edges = cv.Canny(img,100,200)
plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.show()

# https://docs.opencv.org/master/da/d22/tutorial_py_canny.html
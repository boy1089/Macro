import threading
import numpy as np

import ImageAnalyzer

import cv2
from PyQt5 import QtGui

import matplotlib.pyplot as plt

class DisplayManager :

    def __init__(self, grabber, label, label2):
        self.running = False
        self.grabber = grabber
        self.label = label
        self.label2 = label2
        self.ImageAnalyzer = ImageAnalyzer.ImageAnalyzer()

        pass

    def isRunning(self):
        return self.running

    def run(self):
        a = 0
        while self.running :

            self.grabber.grabDisplay()
            self.img = np.asarray(self.grabber.img)[:500, :500]
            # print(self.img[0, 0])
            added_image = cv2.addWeighted(self.img, 0.5, self.img, 0.5, 0)

            h, w, c = self.img.shape
            # print(self.img)
            qImg = QtGui.QImage(added_image, w, h, w*c, QtGui.QImage.Format_RGB888 )
            # qImg = QtGui.QImage(self.img, w, h, w*c)

            pixmap = QtGui.QPixmap.fromImage(qImg)
            self.label.setPixmap(pixmap)
            try:
                self.label2.setPixmap(self.pixmap2)
            except :
                self.label2.setPixmap(pixmap)
                pass



    def start(self):
        self.running = True
        th = threading.Thread(target = self.run)
        th.start()
        print("started..")

    def stop(self):

        self.running = False

    def onExit(self):
        print("exit")
        self.stop()

    def analyzeImage(self):
        self.ImageAnalyzer.getImage(self.img)
        print('a')
        self.ImageAnalyzer.findContours()
        # print(self.ImageAnalyzer.img())
        # plt.imshow(self.ImageAnalyzer.img())
        # plt.imsave(self.ImageAnalyzer.img(), r'C:\Users\boy10\Desktop\git\private\macro\resource\1.png')

        img = np.asarray(self.ImageAnalyzer.img_processed)

        h, w = img.shape
        added_image = cv2.addWeighted(img, 0.5, img, 0.5, 0)
        print(h, w)
        qImg = QtGui.QImage(added_image, w, h, w, QtGui.QImage.Format_Indexed8)

        pixmap = QtGui.QPixmap.fromImage(qImg)

        self.pixmap2 = pixmap
        self.label2.setPixmap(pixmap)
        # return self.ImageAnalyzer.img()



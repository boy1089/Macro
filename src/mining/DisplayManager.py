import threading
import numpy as np

import ImageAnalyzer

import cv2
from PyQt5 import QtGui

import matplotlib.pyplot as plt

class DisplayManager :

    def __init__(self, grabber, label, label2, label3):

        self.running = False
        self.grabber = grabber
        self.label = label
        self.label2 = label2
        self.label3 = label3
        self.ImageAnalyzer = ImageAnalyzer.ImageAnalyzer()

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
                self.analyzeImage()
                self.label2.setPixmap(self.pixmap2)
                self.label3.setPixmap(self.pixmap3)
            except :
                self.label2.setPixmap(pixmap)
                pass
    def run2(self):

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
            self.analyzeImage()
            self.label2.setPixmap(self.pixmap2)
            # self.label3.setPixmap(self.pixmap3)
        except :
            self.label2.setPixmap(pixmap)
            pass
        threading.Timer(0.3, self.run2).start()

    def start(self):
        self.running = True
        # thread with no timing control
        # th = threading.Thread(target = self.run)
        # th.start()
        # print("started..")

        #thread with timer
        self.run2()

    def stop(self):

        self.running = False

    def onExit(self):
        print("exit")
        self.stop()

    def analyzeImage(self):
        self.ImageAnalyzer.getImage(self.img)
        self.ImageAnalyzer.findContours()

        img = np.asarray(self.ImageAnalyzer.img_processed)

        h, w, c = img.shape
        added_image = cv2.addWeighted(img, 0.5, img, 0.5, 0)
        qImg = QtGui.QImage(added_image, w, h, w*c, QtGui.QImage.Format_RGB888)

        pixmap = QtGui.QPixmap.fromImage(qImg)

        self.pixmap2 = pixmap
        self.label2.setPixmap(pixmap)

        # label3

        img = np.asarray(self.ImageAnalyzer.img_inline)

        h, w = img.shape
        added_image = cv2.addWeighted(img, 0.5, img, 0.5, 0)
        qImg = QtGui.QImage(added_image, w, h, w, QtGui.QImage.Format_Indexed8)

        pixmap = QtGui.QPixmap.fromImage(qImg)

        self.pixmap3 = pixmap
        self.label3.setPixmap(pixmap)

        # return self.ImageAnalyzer.img()



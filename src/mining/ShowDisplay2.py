from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout


import cv2
import threading
import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PIL import ImageGrab
import numpy as np

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.running = False

        self.width = 500
        self.height = 500
        self.img_template = cv2.imread(r'C:\Users\boy10\Desktop\git\private\macro\resource\pycharm.PNG')


    def initUI(self):
        self.setWindowTitle('My First Application')

        vbox = QVBoxLayout()
        self.label = QtWidgets.QLabel()

        self.btn_start = QtWidgets.QPushButton("Camera On")
        self.btn_stop = QtWidgets.QPushButton("Camera Off")
        self.btn_patternMatching = QtWidgets.QPushButton("Pattern Matching")
        self.btn_patternMatching.toggle()
        vbox.addWidget(self.label)
        vbox.addWidget(self.btn_start)
        vbox.addWidget(self.btn_stop)
        vbox.addWidget(self.btn_patternMatching)

        self.btn_start.clicked.connect(self.start)
        self.btn_stop.clicked.connect(self.stop)
        self.btn_patternMatching.clicked.connect(self.patternMatching)

        self.setLayout(vbox)
        self.show()

    def run(self):
        global running

        self.cap = ImageGrab.grab()
        self.label.resize(self.width, self.height)

        self.blankOverlay = np.zeros((self.height, self.width, 3), np.uint8)
        self.overlay = self.blankOverlay.copy()

        while running :
            self.img = np.asarray(ImageGrab.grab())[:self.height, :self.width]

            added_image = cv2.addWeighted(self.overlay,0.4,self.img,0.9,0)

            h, w, c = added_image.shapex
            qImg = QtGui.QImage(added_image.data, w, h, w*c, QtGui.QImage.Format_RGB888)
            pixmap = QtGui.QPixmap.fromImage(qImg)
            self.label.setPixmap(pixmap)


        print("Thread end.")

    def start(self):
        global running
        running = True
        th = threading.Thread(target=self.run)
        th.start()
        print('started...')

    def stop(self):
        global running
        self.running = False

    def onExit(self):
        print("exit")
        self.stop()

    def patternMatching(self):
        print('patternmatching started')

        res = cv2.matchTemplate(self.img, self.img_template, cv2.TM_CCOEFF)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        top_left = max_loc
        bottom_right = (top_left[0] + self.img_template.shape[1], top_left[1] + self.img_template.shape[0])
        print(min_val, max_val)
        self.overlay = self.blankOverlay.copy()
        cv2.rectangle(self.overlay, top_left, bottom_right, 255, 2)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())




# 출처: https://blog.xcoda.net/104 [악보쓰는 프로그래머]
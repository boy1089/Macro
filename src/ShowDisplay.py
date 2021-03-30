import cv2
import threading
import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PIL import ImageGrab
import numpy as np

running = False

def run():
    global running
    cap = ImageGrab.grab()
    width = cap.width
    height = cap.height
    label.resize(width, height)
    while running:
        img = np.asarray(ImageGrab.grab())[:500, :500]

        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        h,w,c = img.shape
        qImg = QtGui.QImage(img.data, w, h, w*c, QtGui.QImage.Format_RGB888)
        pixmap = QtGui.QPixmap.fromImage(qImg)
        label.setPixmap(pixmap)

    print("Thread end.")

def stop():
    global running
    running = False
    print("stoped..")

def start():
    global running
    running = True
    th = threading.Thread(target=run)
    th.start()
    print("started..")

def onExit():
    print("exit")
    stop()

def patternMatching():
    img = cv2.imread(r'C:\Users\boy10\Desktop\git\private\macro\resource\pycharm.png')


app = QtWidgets.QApplication([])
win = QtWidgets.QWidget()
vbox = QtWidgets.QVBoxLayout()
label = QtWidgets.QLabel()
btn_start = QtWidgets.QPushButton("Camera On")
btn_stop = QtWidgets.QPushButton("Camera Off")
btn_patternMatching = QtWidgets.QPushButton("Pattern Matching")

vbox.addWidget(label)
vbox.addWidget(btn_start)
vbox.addWidget(btn_stop)
vbox.addWidget(btn_patternMatching)
win.setLayout(vbox)
win.show()

btn_start.clicked.connect(start)
btn_stop.clicked.connect(stop)
btn_patternMatching.clicked.connect(patternMatching)
app.aboutToQuit.connect(onExit)

sys.exit(app.exec_())


# 출처: https://blog.xcoda.net/104 [악보쓰는 프로그래머]
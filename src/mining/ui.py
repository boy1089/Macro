import sys
import GetDisplay
import DisplayManager
import ImageAnalyzer
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout

from PyQt5 import QtWidgets

class MyApp(QWidget):

    def __init__(self):
        super().__init__()

        self.Grabber = GetDisplay.GetDisplay()
        self.initUI()
        self.DisplayManager = DisplayManager.DisplayManager(self.Grabber,
                                                            self.label,
                                                            self.label_processed,
                                                            self.label_inline)
        self.connectUI()


    def initUI(self):
        self.setWindowTitle('My First Application')

        hbox = QHBoxLayout()
        vbox = QVBoxLayout()
        vbox2 = QVBoxLayout()

        self.label = QtWidgets.QLabel()
        self.label_processed = QtWidgets.QLabel()
        self.label_inline = QtWidgets.QLabel()
        self.setImageSize()

        self.btn_start = QtWidgets.QPushButton("Camera On")
        self.btn_stop = QtWidgets.QPushButton("Camera Off")
        self.btn_patternMatching = QtWidgets.QPushButton("Pattern Matching")
        self.btn_patternMatching.toggle()

        vbox.addWidget(self.label)
        vbox.addWidget(self.btn_start)
        vbox.addWidget(self.btn_stop)
        vbox.addWidget(self.btn_patternMatching)

        vbox2.addWidget(self.label_processed)
        vbox2.addWidget(self.label_inline)
        hbox.addLayout(vbox)
        hbox.addLayout(vbox2)

        self.setLayout(hbox)

        self.show()

    def connectUI(self):
        self.btn_start.clicked.connect(self.DisplayManager.start)
        self.btn_stop.clicked.connect(self.DisplayManager.stop)
        self.btn_patternMatching.clicked.connect(self.DisplayManager.analyzeImage)

    def setImageSize(self):
        width, height = self.Grabber.getSize()
        # self.label.resize(width, height)

        self.label.resize(500, 500)
        self.label_processed.resize(500, 500)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
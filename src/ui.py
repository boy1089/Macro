import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('My First Application')
        btn1 = QPushButton('&Button1', self)
        btn1.setCheckable(True)
        btn1.toggle()

        vbox = QVBoxLayout()
        vbox.addWidget(btn1)

        self.setLayout(vbox)

        self.move(300, 300)
        self.resize(400, 200)
        self.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
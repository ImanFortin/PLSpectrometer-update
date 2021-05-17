from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class Root(QMainWindow):

    def __init__(self):
        super(Root,self).__init__()
        self.make_GUI()


    def make_GUI(self):
        self.setGeometry(0,0,1920,1080)
        self.setWindowTitle('Lab GUI')

        self.label = QtWidgets.QLabel(self)
        self.label.setText('this is a label')
        self.label.move(100,100)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText('Press me!')
        self.b1.move(1920/2, 1080/2)
        self.b1.clicked.connect(self.click_b1)


    def click_b1(self):


        if self.label.text() == 'you pressed the button':
            self.label.setText('you pressed again')

        if self.label.text() == 'this is a label':
            self.label.setText('you pressed the button')

        self.update()


    def update(self):
        self.label.adjustSize()

def window():
    app = QApplication(sys.argv)
    win = Root()

    win.show()
    sys.exit(app.exec_())

window()

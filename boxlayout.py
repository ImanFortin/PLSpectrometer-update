import sys
from PyQt5 import QtWidgets


def basicWindow():
    app = QtWidgets.QApplication(sys.argv)
    windowExample = QtWidgets.QWidget()
    buttonA = QtWidgets.QPushButton('Push Me')
    labelA = QtWidgets.QLabel('Look at me')

    h_box = QtWidgets.QHBoxLayout()
    
    h_box.addWidget(labelA)


    h_box.addWidget(buttonA)

    windowExample.setLayout(h_box)

    windowExample.setWindowTitle('PyQt5 Lesson 4')
    windowExample.show()

    sys.exit(app.exec_())

basicWindow()

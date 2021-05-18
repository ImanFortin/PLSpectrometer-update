import sys
from PyQt5 import QtWidgets, QtGui, QtCore

class ButtonWindow(QtWidgets.QMainWindow):

    def __init__(self,**kwargs):

        super().__init__(**kwargs)
        self.resize(500,500)
        self.voltage_button = QtWidgets.QPushButton(self)
        self.voltage_button.setGeometry(QtCore.QRect(100,100,200,200))
        self.voltage_button.setText('turn voltage on')
        self.voltage_button.clicked.connect(turn_on_voltage)



    def turn_on_voltage():
        if self.voltage_button.text()[-3:] == ' on':
            self.voltage_button.setText('turn voltage off')

        elif self.voltage_button.text()[-3:] == 'off':
            self.voltage_button.setText('turn voltage on')
            

if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    win = ButtonWindow()
    win.show()
    sys.exit(app.exec_())

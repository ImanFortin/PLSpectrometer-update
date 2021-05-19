import sys
from PyQt5 import QtWidgets, QtGui, QtCore
import nidaqmx


class ButtonWindow(QtWidgets.QMainWindow):

    def __init__(self):

        super().__init__()
        self.resize(500,500)
        self.voltage_button = QtWidgets.QPushButton('turn voltage on',self)
        self.voltage_button.setGeometry(QtCore.QRect(100,100,200,200))
        self.show()
        self.voltage_button.clicked.connect(self.on_off)

        self.daq = nidaqmx.Task()
        self.daq.ao_channels.add_ao_voltage_chan('Dev1/ao0','my_channel',0,5)
        self.daq.start()

        self.daq.write(0)
        self.daq.stop()






    def on_off(self):


        if self.voltage_button.text()[-3:] == ' on':
            self.daq.start()

            self.daq.write(5)
            self.daq.stop()

            self.voltage_button.setText('turn voltage off')

        elif self.voltage_button.text()[-3:] == 'off':
            
            self.daq.start()

            self.daq.write(0)
            self.daq.stop()
            self.voltage_button.setText('turn voltage on')




if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    win = ButtonWindow()

    sys.exit(app.exec_())

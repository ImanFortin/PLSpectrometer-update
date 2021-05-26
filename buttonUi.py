import sys
from PyQt5 import QtWidgets, QtGui, QtCore
import nidaqmx
import time
from nidaqmx.types import CtrTime
from nidaqmx.constants import LineGrouping, Edge, AcquisitionType
class ButtonWindow(QtWidgets.QMainWindow):

    def __init__(self):

        super().__init__()
        self.resize(500,500)
        self.voltage_button = QtWidgets.QPushButton('turn voltage on',self)
        self.voltage_button.setGeometry(QtCore.QRect(150,150,200,200))

        self.close_button = QtWidgets.QPushButton('close', self)
        self.close_button.setGeometry(450,0,50,50)


        self.do_button = QtWidgets.QPushButton('digital signal',self)
        self.do_button.setGeometry(150,360,200,100)

        self.show()
        self.voltage_button.clicked.connect(self.on_off)
        self.close_button.clicked.connect(self.close)
        self.do_button.clicked.connect(self.digital)

        self.channel1 = nidaqmx.Task()
        self.channel2 = nidaqmx.Task()
        self.task_read = nidaqmx.Task()
        self.dig_out = nidaqmx.Task()
        self.ctr_out = nidaqmx.Task()



        self.dig_out.di_channels.add_di_chan('Dev1/port0/line0')
        self.dig_out.timing.cfg_samp_clk_timing(100)
        self.dig_out.start()



        self.channel1.ao_channels.add_ao_voltage_chan('Dev1/ao0','my_channel',0,5)
        self.channel1.start()
        self.channel1.write(0)

        self.channel2.ao_channels.add_ao_voltage_chan('Dev1/ao1','secondary',0,5)
        self.channel2.start()
        self.channel2.write(0)

        self.task_read.ai_channels.add_ai_voltage_chan('Dev1/ai1')
        self.task_read.start()

    def digital(self):
        self.dig_out.write(3)



    def close(self):
        #shut off channel 1
        self.channel1.write(0)
        self.channel1.stop()
        self.channel1.close()

        #shut off channel 2
        self.channel2.write(0)
        self.channel2.stop()
        self.channel2.close()


        #shut off the reading
        self.task_read.stop()
        self.task_read.close()

        #turn off dig_out and close
        self.dig_out.write(False)
        self.dig_out.stop()
        self.dig_out.close()
        #close the UI
        self.close()





    def on_off(self):


        if self.voltage_button.text()[-3:] == ' on':


            self.channel1.write(5)
            self.channel2.write(2)
            print(self.task_read.read())
            self.voltage_button.setText('turn voltage off')

        elif self.voltage_button.text()[-3:] == 'off':


            self.channel2.write(0)
            self.channel1.write(0)
            self.voltage_button.setText('turn voltage on')




if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    win = ButtonWindow()

    sys.exit(app.exec_())

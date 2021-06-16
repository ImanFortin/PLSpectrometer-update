#THIS IS THE UI FILE IT FEEDS THE INPUTS TO THE SPECTROMETER
#IF YOU WISH TO CHANGE THE BEHAVIOUR OF THE SPECTROMETER EDIT 'spectrometer.py'
#IF YOU WISH TO CHANGE THE WAY DATA IS INPUTED THROUGH THE UI EDIT HERE OR USE
#'spectrometer.ui' WITH QTDESIGNER AND COMPILE THE UI TO 'qt_designer.py'

from qt_designer import Ui_MainWindow
from PyQt5 import QtWidgets as qtw
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtCore as qtc
from spectrometer import Spectrometer
from matplotlib_embedding import PlotWidget
import time
from graphing import Plots
from workers.move import moveWorker
from workers.scan import scanWorker
from PyQt5.QtCore import QObject, QThread, pyqtSignal




#the main windowclass that will be made it inherits from the widget MainWindow
class MainWindow(qtw.QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) #run the init mathod of the parent class (MainWindow)
        self.ui = Ui_MainWindow() #initiate an instance of the compiled qt designer class
        self.ui.setupUi(self) #run the setup method to create the window

        self.connect_buttons() #connect all the buttons
        self.make_plots() #add the plots to the UI
        self.double = Spectrometer('Dev2') #initialize the double spectrometer
        self.single = Spectrometer('Dev3') #initialize the single spectrometer
        self.ui.current_wavelength_lbl.setText('Position (nm): '+str(self.double.position))#display the current position
        self.autoscale_lbls() #autoscale the labels so they don't cut off
        print('done init')



    #method for adjusting the labels so they are consistent between machines
    def autoscale_lbls(self):
        self.ui.position_lbl.adjustSize()
        self.ui.current_wavelength_lbl.adjustSize()
        self.ui.actual_value_lbl.adjustSize()
        self.ui.recalibrate_lbl.adjustSize()
        self.ui.move_spectrometer_lbl.adjustSize()
        self.ui.go_to_lbl.adjustSize()
        self.ui.scan_start_lbl.adjustSize()
        self.ui.scan_end_lbl.adjustSize()
        self.ui.perform_scan_lbl.adjustSize()
        self.ui.scan_step_lbl.adjustSize()
        self.ui.file_name_lbl.adjustSize()
        self.ui.sample_id_lbl.adjustSize()
        self.ui.count_time_lbl.adjustSize()
        self.ui.spect_select_lbl.adjustSize()

    # connect all the buttons to their functions
    def connect_buttons(self):
        self.ui.recalibrate_button.clicked.connect(self.recalibrate)
        self.ui.scan_button.clicked.connect(self.scan)
        self.ui.move_button.clicked.connect(self.move)
        self.ui.radioButton.setChecked(True)#default to the double spectrometer
        self.ui.abort_button.clicked.connect(self.abort)
        self.ui.shutter_btn.clicked.connect(self.shutter)
        self.ui.radioButton.toggled.connect(self.switch_spectrometer)

    def make_plots(self):
        self.plot_frame = qtw.QFrame(self.ui.centralwidget)
        layout = qtw.QVBoxLayout()

        self.wavelength_plot = Plots('Wavelength')
        layout.addWidget(self.wavelength_plot)


        self.energy_plot = Plots('Energy')
        layout.addWidget(self.energy_plot)
        self.plot_frame.setLayout(layout)
        self.plot_frame.setGeometry(400,0,1000,1000)

    #update the plots with data
    def update_plots(self,data):
        self.wavelength_plot.refresh_stats(self.double.position,data)
        self.energy_plot.refresh_stats(self.double.position,data)

    def switch_spectrometer(self):
        if self.ui.radioButton.isChecked():
            self.ui.current_wavelength_lbl.setText('Position (nm): '+str(self.double.position))
            self.autoscale_lbls()
        else:
            self.ui.current_wavelength_lbl.setText('Position (nm): '+str(self.single.position))
            self.autoscale_lbls()



    #update the spectrometer position and display
    def update_position(self,position):
        position = round(position, 3)
        self.double.position = position
        if self.ui.radioButton.isChecked():#only update the display with double if double is selected
            current = self.ui.current_wavelength_lbl.text()
            keep = current[:current.find(':')+2]
            new_string = keep + str(position)
            self.ui.current_wavelength_lbl.setText(new_string)
            self.ui.current_wavelength_lbl.adjustSize()

    def change_status(self,status = ''):
        self.ui.status_lbl.setText('Status: ' + status)

    #function that sets the buttons to enabled, to be called after
    #a scan or a move (connected to the finished of the Thread)
    def enable_buttons(self):
        self.ui.recalibrate_button.setEnabled(True)
        self.ui.move_button.setEnabled(True)
        self.ui.scan_button.setEnabled(True)
        self.ui.optimize_btn.setEnabled(True)

    #disable buttons
    def disable_buttons(self):
        self.ui.recalibrate_button.setEnabled(False)
        self.ui.move_button.setEnabled(False)
        self.ui.scan_button.setEnabled(False)
        self.ui.optimize_btn.setEnabled(False)

    #shutter function
    def shutter(self):
        if self.ui.shutter_btn.isChecked():
            self.double.close_shutter()
            self.ui.shutter_btn.setText('Open Shutter')
        else:
            self.double.open_shutter()
            self.ui.shutter_btn.setText('Close Shutter')

    def scan(self):
        try:
            #read data from the input boxes
            start = float(self.ui.scan_start_input.text())
            end = float(self.ui.scan_end_input.text())
            step = float(self.ui.scan_step_input.text())
            time = float(self.ui.count_time_input.text())
            filename = self.ui.file_name_input.text()
            sample_id = self.ui.sample_ID_input.text()


        except:
            print('scan did not recieve valid inputs')
            return


        #disable the buttons to prevent crashing
        self.disable_buttons()
        self.change_status('Scanning')

        #clear the plots
        # self.wavelength_plot.clear()
        # self.energy_plot.clear()
        #set the range
        self.wavelength_plot.set_xlim(start,end)
        self.energy_plot.set_xlim(start,end)
        self.wavelength_plot.cla()
        self.energy_plot.cla()
        # Step 2: Create a QThread object
        self.scan_thread = QThread()
        # Step 3: Create a worker object
        self.worker = scanWorker(self.double,start,end,step,time,filename,sample_id)#input the double spectrometer


        # # Step 4: Move worker to the thread
        self.worker.moveToThread(self.scan_thread)#this makes the scan_thread methos be executed by the thread
        # # Step 5: Connect signals and slots
        self.scan_thread.started.connect(self.worker.scan)#connect to the scan method
        self.worker.finished.connect(self.scan_thread.quit)#quit when done
        self.worker.finished.connect(self.worker.deleteLater)#delete when done
        self.worker.finished.connect(self.enable_buttons)#enable buttons when done
        self.worker.finished.connect(self.change_status)
        self.scan_thread.finished.connect(self.scan_thread.deleteLater)#delete the thread when done
        self.worker.position.connect(self.update_position)#update the position as we go
        self.worker.data.connect(self.update_plots)#update the plots as we take data

        #start the thread
        self.scan_thread.start()



    def move(self):
        #try to load the data
        try:
            destination = float(self.ui.move_input.text())

        #print a message if it fails
        except:
            print('move recieved invalid input')
            return

        print('starting move to',destination)
        self.change_status('Moving')
        # Step 2: Create a QThread object
        self.thread = QThread()
        # Step 3: Create a worker object
        if self.ui.radioButton.isChecked():#if we have double selected
            if abs(destination - self.double.position) > 100:#safety measure
                intent = self.check_intent()
                if not intent:
                    return

            self.worker = moveWorker(self.double,destination)#input double

        else:#if single is selected
            if abs(destination - self.single.position) > 100:
                intent = self.check_intent()
                if not intent:
                    return

            self.worker = moveWorker(self.single,destination)#input single

        #disable the buttons to prevent crashing
        self.disable_buttons()

        # # Step 4: Move worker to the thread
        self.worker.moveToThread(self.thread)

        # # Step 5: Connect signals and slots see scan fordetailed documentation

        self.thread.started.connect(self.worker.move)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.worker.finished.connect(self.enable_buttons)
        self.worker.finished.connect(self.change_status)
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.position.connect(self.update_position)
        # # Step 6: Start the thread

        self.thread.start()



    def recalibrate(self):
        try:
            actual = float(self.ui.recalibrate_input.text())
        except:
            print('the recalibrate input was invalid')
            return

        if self.ui.radioButton.isChecked():
            self.double.recalibrate(actual)
        else:
            self.single.recalibrate(actual)

        self.update_position(actual)
        print('succesfully recalibrated', self.double.position)


    def check_intent(self):
        check = QMessageBox()
        check.setText("you have requested to move over 100nm is this correct")
        check.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        check.setIcon(QMessageBox.Warning)
        check = check.exec()

        if check == QMessageBox.Yes:
            return True
        else:
            return False

    #this overwrites the close button of the UI
    def closeEvent(self,event):


        close = QMessageBox()

        close.setText("Are you sure?")
        close.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)

        close = close.exec()

        if close == QMessageBox.Yes:
            self.double.save()
            self.double.close_channels()
            self.single.save()
            self.single.close_channels()
            event.accept()
        else:
            event.ignore()


    def abort(self):
        #changes the abort flag inside the worker to be true which will trigger
        #abort on next scan step, cannot currently abort a move
        self.worker.abort = True




#run the UI
if __name__ == '__main__':
    import sys
    app = qtw.QApplication(sys.argv) #makes the app
    win = MainWindow() #make our UI
    win.show() #display our UI

    sys.exit(app.exec_()) #executes the app

#THIS IS THE UI FILE IT FEEDS THE INPUTS TO THE SPECTROMETER
#IF YOU WISH TO CHANGE THE BEHAVIOUR OF THE SPECTROMETER EDIT 'spectrometer.py'
#IF YOU WISH TO CHANGE THE WAY DATA IS INPUTED THROUGH THE UI EDIT HERE OR USE
#'spectrometer.ui' WITH QTDESIGNER AND COMPILE THE UI TO 'qt_designer.py'

from qt_designer import Ui_MainWindow
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from spectrometer import Spectrometer
from matplotlib_embedding import PlotWidget
import time
from workers.move import moveWorker
from workers.scan import scanWorker
from PyQt5.QtCore import QObject, QThread, pyqtSignal




#the main windowclass that will be made it inherits from the widget MainWindow
class MainWindow(qtw.QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) #run the init mathod of the parent class (MainWindow)
        self.ui = Ui_MainWindow() #initiate an instance of the compiled qt designer class
        self.ui.setupUi(self) #run the setup method to create the window
        self.autoscale_lbls() #autoscdale the labels so they don't cut off
        self.connect_buttons() #connect all the buttons
        self.make_plots() #add the plots to the UI
        self.double = Spectrometer() #initialize the double spectrometer



    def make_plots(self):
        #make the wavelength plot
        self.wavelength_plot = PlotWidget(parent = self, width = 6, height = 4)
        self.wavelength_plot.move(500,0)

        #make the energy plot
        self.energy_plot = PlotWidget(parent = self, width = 6, height = 4, scale = 'log')
        self.energy_plot.move(500,470)

    #method for adjusting the labels so they are consistent between machines
    def autoscale_lbls(self):
        self.ui.position_lbl.adjustSize()
        self.ui.property_label.adjustSize()
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
        self.ui.common_variables_lbl.adjustSize()
        self.ui.spect_select_lbl.adjustSize()




    # connect all the buttons to their functions
    def connect_buttons(self):
        #connect the recalibrate function to the recalibrate function below
        self.ui.recalibrate_button.clicked.connect(self.recalibrate)
        #connect scan button to scan function below
        self.ui.scan_button.clicked.connect(self.scan)
        #connect move button to move function below
        self.ui.move_button.clicked.connect(self.move)
        #connect the close button to close function below
        self.ui.close_button.clicked.connect(self.exit)
        #default to the double spectrometer
        self.ui.radioButton.setChecked(True)

        self.ui.abort_button.clicked.connect(self.abort)


    #update the plots with data
    def update_plots(self,data):
        self.wavelength_plot.update(self.double.position,data)
        self.energy_plot.update(self.double.position,data)

    #update the spectrometer position
    def update_position(self,position):
        self.double.position = position

    #update the progress bar function arugment is a list that contains the current
    #step and the maximum amount of steps
    def update_progress(self,step_max):
        self.ui.progressBar_scan.setValue(step_max[0])
        self.ui.progressBar_scan.setMaximum(step_max[1])

    #function that sets the buttons to enabled, to be called after
    #a scan or a move (connected to the finished of the Thread)
    def enable_buttons(self):
        self.ui.recalibrate_button.setEnabled(True)
        self.ui.move_button.setEnabled(True)
        self.ui.scan_button.setEnabled(True)


    def scan(self):
        #try to read the entries
        try:
            start = float(self.ui.scan_start_input.text())
            end = float(self.ui.scan_end_input.text())
            step = float(self.ui.scan_step_input.text())
            time = float(self.ui.count_time_input.text())

        #raise exception if there is an issue
        except:
            print('scan did not recieve valid inputs')
            return #leave the function


        #disable the buttons to prevent crashing
        self.ui.recalibrate_button.setEnabled(False)
        self.ui.move_button.setEnabled(False)
        self.ui.scan_button.setEnabled(False)

        #clear the plots
        self.wavelength_plot.clear()
        self.energy_plot.clear()


        print('starting scan')
        # Step 2: Create a QThread object
        self.scan_thread = QThread()
        # Step 3: Create a worker object
        self.worker = scanWorker(self.double,start,end,step,time)
        # # Step 4: Move worker to the thread
        self.worker.moveToThread(self.scan_thread)
        #
        # # Step 5: Connect signals and slots
        #connect start to our scan function from the worker folder
        self.scan_thread.started.connect(self.worker.scan)
        #when done quit and delete the threads
        self.worker.finished.connect(self.scan_thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        #re-enable the buttons
        self.worker.finished.connect(self.enable_buttons)
        #when done delete thread
        self.scan_thread.finished.connect(self.scan_thread.deleteLater)
        #connect the progress to the progress bar
        self.worker.progress.connect(self.update_progress)
        #connect position to update position
        self.worker.position.connect(self.update_position)
        #connect the data to update plots
        self.worker.data.connect(self.update_plots)
        # Step 6: Start the thread

        self.scan_thread.start()



    def move(self):
        #try to load the data
        try:
            destination = float(self.ui.move_input.text())

        #print a message if it fails
        except:
            print('move recieved invalid input')
            return

        #disable the buttons to prevent crashing
        self.ui.recalibrate_button.setEnabled(False)
        self.ui.move_button.setEnabled(False)
        self.ui.scan_button.setEnabled(False)

        #if no issue run the move method of the spectrometer see spectrometer.py
        print('starting move to',destination)
        # Step 2: Create a QThread object
        self.thread = QThread()
        # Step 3: Create a worker object
        self.worker = moveWorker(self.double,destination)
        # # Step 4: Move worker to the thread
        self.worker.moveToThread(self.thread)

        # # Step 5: Connect signals and slots

        self.thread.started.connect(self.worker.move)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.worker.finished.connect(self.enable_buttons)
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.progress.connect(self.update_progress)
        self.worker.position.connect(self.update_position)
        # # Step 6: Start the thread
        self.thread.start()






    def recalibrate(self):
        #try to load in the data as a float
        try:
            actual = float(self.ui.recalibrate_input.text())
        #if we encounter an error print messagge
        except:
            print('the recalibrate input was invalid')
        #if no issue run the recalibrate method of the spectrometer see spectrometer.py
        else:
            self.double.recalibrate(actual)
            #print success message and the new postion
            print('succesfully recalibrated', self.double.position)

    def exit(self):
        #save the position of the spectrometer see spectrometer.py
        self.double.save()
        #close the application
        self.close()

    def abort(self):
        pass




#run the UI
if __name__ == '__main__':
    import sys
    app = qtw.QApplication(sys.argv) #just pyqt5 stuff
    win = MainWindow() #make our UI
    win.show() #display our UI

    sys.exit(app.exec_()) #more pyqt5 stuff

#THIS IS THE UI FILE IT FEEDS THE INPUTS TO THE SPECTROMETER
#IF YOU WISH TO CHANGE THE BEHAVIOUR OF THE SPECTROMETER EDIT 'spectrometer.py'
#IF YOU WISH TO CHANGE THE WAY DATA IS INPUTED THROUGH THE UI EDIT HERE OR USE
#'spectrometer.ui' WITH QTDESIGNER AND COMPILE THE UI TO 'qt_designer.py'



#importing the ui compiled python code class
from qt_designer import Ui_MainWindow
#import the widgets, required for inheritance
from PyQt5 import QtWidgets as qtw
#unused for now can be deleted without changing behaviour
from PyQt5 import QtCore as qtc
#custom class for the spectrometer see spectrometer.py
from spectrometer import Spectrometer

from matplotlib_embedding import Canvas


#the main windowclass that will be made it inherits from the widget MainWindow
class MainWindow(qtw.QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) #run the init mathod of the parent class (MainWindow)

        self.ui = Ui_MainWindow() #initiate an instance of the compiled qt designer class

        self.ui.setupUi(self) #run the setup method to create the window

        self.autoscale_lbls() #autoscdale the labels so they don't cut off

        self.connect_buttons() #connect all the buttons

        self.make_plots()#add the plots to the UI

        self.double = Spectrometer() #initialize the double spectrometer



    def make_plots(self):
        #make the wavelength plot
        self.wavelength_plot = Canvas(parent = self, width = 5, height = 4)
        self.wavelength_plot.move(500,35)

        #make the energy plot
        self.energy_plot = Canvas(parent = self, width = 5, height = 4)
        self.energy_plot.move(500,475)




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



    #connect all the buttons to their functions
    def connect_buttons(self):
        #connect the recalibrate function to the recalibrate function below
        self.ui.recalibrate_button.clicked.connect(self.recalibrate)
        #connect scan button to scan function below
        self.ui.scan_button.clicked.connect(self.scan)
        #connect move button to move function below
        self.ui.move_button.clicked.connect(self.move)
        #connect the abort button to abort function below
        self.ui.abort_button.clicked.connect(self.abort)
        #connect the close button to close function below
        self.ui.close_button.clicked.connect(self.exit)




    def scan(self):
        #try to read the entries
        try:
            start = float(self.ui.scan_start_input.text())
            end = float(self.ui.scan_end_input.text())
            step = float(self.ui.scan_step_input.text())

        #raise exception if there is an issue
        except:
            print('scan did not recieve valid inputs')

        #if there is no issue we run the scan method of spectrometer see spectrometer.py
        else:
            self.double.scan(start,end,step)




    def move(self):
        #try to load the data
        try:
            destination = float(self.ui.move_input.text())

        #print a message if it fails
        except:
            print('move recieved invalid input')

        #if no issue run the move method of the spectrometer see spectrometer.py
        else:
            self.double.move(destination)



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
        #call the abort function on the spectrometer see spectrometer.py
        self.double.abort()




#run the UI
if __name__ == '__main__':
    import sys
    app = qtw.QApplication(sys.argv) #just pyqt5 stuff
    win = MainWindow() #make our UI
    win.show() #display our UI
    sys.exit(app.exec_()) #more pyqt5 stuff

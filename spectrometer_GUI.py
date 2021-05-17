#THIS IS THE UI FILE IT FEEDS THE INPUTS TO THE SPECTROMETER 
#IF YOU WISH TO CHANGE THE BEHAVIOUR OF THE SPECTROMETER EDIT 'spectrometer.pu'
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


#the main windowclass that will be made it inherits from the widget MainWindow
class MainWindow(qtw.QMainWindow):

    def __init__(self, *args, **kwargs):
        
        #run the init mathod of the parent class (MainWindow)
        super().__init__(*args, **kwargs)
        #initiate an instance of the compiled qt designer class
        self.ui = Ui_MainWindow()
        #run the setup method to create the window
        self.ui.setupUi(self)
        #run the update function to reformat the labels
        self.update()
        self.connect_buttons()
        self.double = Spectrometer()
        

    #method for adjusting the labels so they are consistent between machines
    def update(self):
        self.ui.property_label.adjustSize()
        self.ui.actual_value_lbl.adjustSize()
        self.ui.move_to_lbl.adjustSize()
        self.ui.scan_start_lbl.adjustSize()
        self.ui.scan_end_lbl.adjustSize()
        self.ui.current_wavelength_lbl.adjustSize()
        
        
    
    #connect all the buttons to their functions
    def connect_buttons(self):
        self.ui.recalibrate_button.clicked.connect(self.recalibrate)
        self.ui.scan_button.clicked.connect(self.scan)
        self.ui.move_button.clicked.connect(self.move)
        self.ui.abort_button.clicked.connect(self.abort)
        self.ui.close_button.clicked.connect(self.exit)
        
        
        
    
    def scan(self):
        #try to load in the data
        try:
            start = float(self.ui.scan_start_input.text())
            end = float(self.ui.scan_end_input.text())
            step = float(self.ui.scan_step_input.text())
            
        #raise exception    
        except:
            print('scan did not recieve valid inputs')
            
        #if succesful we run the scan method of spectrometer
        else:
            self.double.scan(start,end,step)
            
            
            
        
    def move(self):
        #try to load the data
        try:
            destination = float(self.ui.move_input.text())
            
        #print if it fails
        except:
            print('move recieved invalid input')
            
        #if we succeed run the move method of the spectrometer
        else:
            self.double.move(destination)
            
        
        
    def recalibrate(self):
        try:
            actual = float(self.ui.recalibrate_input.text())
        
        except:
            print('the recalibrate input was invalid')
            
        else:
            self.double.recalibrate(actual)
            
            print('succesfully recalibrated', self.double.position)
            
            
        
    def exit(self):
        #save the position of the spectrometer
        self.double.save()
        #close the application
        self.close()
        
    
    def abort(self):
        #call the abort function on the spectrometer
        self.double.abort()
    
    
    
    def stop(self):
        pass

if __name__ == '__main__':
    import sys
    app = qtw.QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())

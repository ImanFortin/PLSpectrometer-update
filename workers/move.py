import time
from PyQt5.QtCore import QObject, QThread, pyqtSignal

#this is the move worker he does the moving
class moveWorker(QObject):

    #these are the signals that are connected to functions in GUI.py
    position = pyqtSignal(float)
    finished = pyqtSignal()

    #to initialize we need to take the spectrometer that is being moveToThread
    def __init__(self,spectrometer,end):
        super().__init__() #this just calls the parent init method always required if making a worker
        self.spectrometer = spectrometer #will be either single or double
        self.end = end #the desination
        self.abort = False

    def move(self):

        start = self.spectrometer.position#get the current position
        end = self.end#get the end position
        distance = round(abs(end - start),3)

        if end < start:
            direction = -1
        elif end > start:
            direction = 1
        else:
            self.finished.emit()
            return

        high = 1/(2*self.spectrometer.frequency)
        low = high
        #set the direction voltage
        self.spectrometer.set_direction(direction)#see spectrometer.py for the method

        if direction < 0:#if the direction is backwards
            self.spectrometer.move(distance + 20, high_time = high, low_time = low)#first move to twenty nm back
            direction = 1
            self.spectrometer.set_direction(direction) #change directions
            self.spectrometer.move(19.97, high_time = high, low_time = low) #move to within 0.03 nm of the positin
            self.spectrometer.move(0.03, high_time = high, low_time = 0.25) #do the last 0.03 nm with 1s in between each step (4 pulses a step)

        elif direction >= 0:#otherwise just move forwards within 0.03 and then slow down
            if distance < 0.03:
                self.spectrometer.move(distance, high_time = high, low_time = 0.25)
            else:
                self.spectrometer.move(distance - 0.03, high_time = high, low_time = low)
                self.spectrometer.move(0.03, high_time = high, low_time = 0.25)

        self.position.emit(end)
        self.finished.emit()#emit that we're done


    def check_abort(self):
        if self.abort:
            self.finished.emit()
            return

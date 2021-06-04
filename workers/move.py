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
        distance = abs(end  - start)#get the distance

        #try block to catch divide by zero error
        try:
            direction = int((end - start)/distance)#get the direction
        except:
            #if we divide by zero we are at the destination
            self.finished.emit() #emit done
            return #return

        high = 1/(self.spectrometer.frequency)
        low = high
        #set the direction voltage
        self.spectrometer.set_direction(direction)#see spectrometer.py for the method

        if direction < 0:#if the direction is backwards
            self.spectrometer.move(distance + 10, high_time = high, low_time = low)#first move to ten nm back
            direction = 1
            self.spectrometer.set_direction(direction) #change directions
            self.spectrometer.move(9.97, high_time = high, low_time = low) #move to with 0.03 nm of the positin
            self.spectrometer.move(0.03, high_time = high, low_time = 1) #do the last 0.03 nm with 1s in between each pulse

        elif direction > 0:#if the direction is forwards
            if distance < 10:#if distance is less than ten we need to go backwards
                self.spectrometer.set_direction(-1)#change direction
                self.spectrometer.move(abs(distance - 10), high_time = high, low_time = low)#move backwards the correct amount
                self.spectrometer.set_direction(1)#change direction
                self.spectrometer.move(9.97, high_time = high, low_time = low)#move forward with 0.03nm
                self.spectrometer.move(0.03, high_time = high, low_time = 1)#do the last 0.03 nm with 1s lows
            else:#otherwise just move forwards within 0.03 and then slow down
                self.spectrometer.move(distance - 0.03, high_time = high, low_time = low)
                self.spectrometer.move(0.03, high_time = high, low_time = 1)

        self.position.emit(end)
        self.finished.emit()#emit that we're done


    def check_abort(self):
        if self.abort:
            self.finished.emit()
            return

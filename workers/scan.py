import time
from PyQt5.QtCore import QObject, QThread, pyqtSignal
from datetime import datetime


#this is the scan worker he does the scanning
class scanWorker(QObject):

    #this is all the information we will be sending to UI while we run
    data = pyqtSignal(float)
    progress = pyqtSignal(list)
    position = pyqtSignal(float)
    finished = pyqtSignal()

    #needs to take a spectrometer, start, end, step, and time
    def __init__(self,spectrometer,start,end,step,time,filename):
        super().__init__()
        self.spectrometer = spectrometer
        self.start = start
        self.end = end
        self.step = step
        self.time = time
        self.abort = False
        #leaving these empty for now so i don't have to input them when testing
        self.filename = filename
        self.sample_id = ''




    def scan(self):

        #first copy the move function to get into position
        start = self.spectrometer.position
        end = self.start#we want to move to the start point
        distance = abs(end - start)

        try:
            direction = int((end - start)/distance)
        except:
            direction = 1 #this will need to be changed when we are actaully sending pulses

        #unfortunately we just have to copy in the move function here
        high = 1/(self.spectrometer.frequency)
        low = high
        #set the direction voltage
        self.spectrometer.set_direction(direction)#see spectrometer.py for the method

        if direction < 0:#if the direction is backwards
            self.spectrometer.move(distance + 10, high_time = high, low_time = low)#first move to ten nm back
            direction = 1
            self.check_abort()
            self.spectrometer.set_direction(direction) #change directions
            self.spectrometer.move(9.97, high_time = high, low_time = low) #move to 0.03 nm of the position
            self.check_abort()
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

        #prepare for the scan
        start = self.start
        end = self.end
        distance = abs(end - start)
        direction = 1
        f = open(self.filename, 'w')
        number_of_steps = int(distance/self.step)
        print(distance)
        print(number_of_steps)
        #start the scanning process
        for i in range(number_of_steps):
            self.check_abort()
            self.spectrometer.move(self.step, high_time = high, low_time = low)
            self.position.emit(self.spectrometer.position + self.step)
            self.progress.emit([i + 1,number_of_steps])
            counts = self.spectrometer.read(self.time)
            self.data.emit(counts + 1)
            print(counts)
            f.write(str(self.spectrometer.position) + '\t' + str(counts) + '\n')

        f.close()
        self.finished.emit()#emit that we're done

    def check_abort(self):
        if self.abort:
            self.finished.emit()
            return

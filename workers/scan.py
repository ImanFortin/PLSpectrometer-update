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
    def __init__(self,spectrometer,start,end,step,time):
        super().__init__()
        self.spectrometer = spectrometer
        self.start = start
        self.end = end
        self.step = step
        self.time = time
        self.abort = False
        #leaving these empty for now so i don't have to input them when testing
        self.filename = ''
        self.sample_id = ''




    def scan(self):

        #first copy the move function to get into position
        start = int(self.spectrometer.position)
        end = int(self.start)#we want to move to the start point
        distance = abs(end - start)

        try:
            direction = int((end - start)/distance)
        except:
            direction = 1 #this will need to be changed when we are actaully sending pulses

        print(start,end,direction)
        
        self.spectrometer.set_direction(direction)
        for i in range(start, end + direction, direction):
            if self.abort:#check the abort flag
                self.finished.emit()
                return
            print(i)
            self.position.emit(i) #emit the position
            time.sleep(1)#simulate the move collection


        #set the new start to be the current position
        start = int(self.spectrometer.position)
        end = int(self.end) #set end to the end position of the scan
        distance = abs(end - start)

        #check for divide by zero
        try:
            direction = int((end - start)/distance)
        except:
            self.finished.emit()#scan distance is zero
            return

        self.spectrometer.set_direction(direction)
        print(start,end,direction)
        for i in range(start, end + direction, direction):
            if self.abort:#check for the abort flag
                self.finished.emit()#if it is abort
                return
            print(i)
            self.position.emit(i) #emit the position
            self.data.emit(i/2)
            time.sleep(1) #simulate collecting data for one second
            self.progress.emit([abs(i-start),abs(start - end)])

        self.progress.emit([abs(start - end), abs(start - end)])
        self.finished.emit()#emit that we're done

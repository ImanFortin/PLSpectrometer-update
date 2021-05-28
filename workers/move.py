import time
from PyQt5.QtCore import QObject, QThread, pyqtSignal

#this is the move worker he does the moving
class moveWorker(QObject):

    #these are the signals that are connected to functions in GUI.py
    progress = pyqtSignal(list)#give the data type to be emitted
    position = pyqtSignal(float)
    finished = pyqtSignal()

    #to initialize we need to take the spectrometer that is being moveToThread
    def __init__(self,spectrometer,end):
        super().__init__() #this just calls the parent init method always required if making a worker
        self.spectrometer = spectrometer #will be either single or double
        self.end = end #the desination
        self.abort = False

    def move(self):

        start = int(self.spectrometer.position)#get the current position
        end = int(self.end)#get the end position
        distance = abs(end - start)#get the distance

        #try block to catch divide by zero error
        try:
            direction = int((end - start)/distance)#get the direction
        except:
            #if we divide by zero we are at the destination
            self.finished.emit() #emit done
            return #return

        #set the direction voltage
        self.spectrometer.set_direction(direction)#see spectrometer.py for the method
        self.progress.emit([0, abs(start - end)])#set progress to zero

        for i in range(start, end + direction, direction):
            if self.abort:#check the abort flag
                self.finished.emit()#signal done
                return

            print(i)
            time.sleep(1)#simulate the move
            self.progress.emit([abs(i-start),abs(start - end)]) #emit the progress
            self.position.emit(i) #emit the position


        self.progress.emit([abs(start - end), abs(start - end)])#emit that progress is done
        self.finished.emit()#emit that we're done

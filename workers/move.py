import time
from PyQt5.QtCore import QObject, QThread, pyqtSignal

#this is the move worker he does the moving
class moveWorker(QObject):

    progress = pyqtSignal(list)
    position = pyqtSignal(float)
    finished = pyqtSignal()


    def __init__(self,spectrometer,end):
        super().__init__()
        self.spectrometer = spectrometer
        self.end = end


    def move(self):
        
        start = int(self.spectrometer.position)#get the current position
        end = int(self.end)#get the end position
        distance = abs(end - start)#get the distance
        direction = int((end - start)/distance)#get the direction
        self.progress.emit([0, abs(start - end)])#set progress to zero

        print(start, end + direction, direction)
        for i in range(start, end, direction):
            time.sleep(1)#simulate the move
            self.progress.emit([abs(i-start),abs(start - end)]) #emit the progress
            self.position.emit(i) #emit the position


        self.progress.emit([abs(start - end), abs(start - end)])#emit that progress is done
        self.finished.emit()#emit that we're done

import time
from PyQt5.QtCore import QObject, QThread, pyqtSignal

class optimizeWorker(QObject):

    bar_update = pyqtSignal(int)
    finished = pyqtSignal()

    def __init__(self,spectrometer,player):
        super().__init__()
        self.abort = False
        self.player = None

    def optimize(self):
        counts[]
        maximum = 100
        
        while not self.abort:
            counts.append(spectrometer.read(0.1))
            if len(count) > 10:
                counts.pop(0)

            summed = sum(counts)
            while summed > maximum:
                maximum = 10*maximum
            bar_update.emit(summed)
            playbackSpeed = summed/self.max*4
            player.setPlaybackRate(playbackSpeed)
            player.play()

        finished.emit()

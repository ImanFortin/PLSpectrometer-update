import time
from PyQt5.QtCore import QObject, QThread, pyqtSignal

class optimizeWorker(QObject):

    count = pyqtSignal(int)

    def __init__(self,spectrometer):
        super().__init__()
        self.abort = False
        self.player = None
        
    def optimize(self):
        pass

import time
import random
from PyQt5 import QtMultimedia as qtmm
from PyQt5.QtCore import QObject, QThread, pyqtSignal
from PyQt5 import QtCore as qtc

class optimizeWorker(QObject):

    bar_update = pyqtSignal(int)
    finished = pyqtSignal()

    def __init__(self,spectrometer):
        super().__init__()
        self.abort = False
        self.player = qtmm.QMediaPlayer()
        url = qtc.QUrl(qtc.QDir.currentPath()+'/chirp.wav')
        self.set_source(url)

    def set_source(self, url):
        content = qtmm.QMediaContent(url)
        self.playlist = qtmm.QMediaPlaylist()
        self.playlist.addMedia(content)
        self.playlist.setCurrentIndex(1)
        self.player.setPlaylist(self.playlist)

    def optimize(self):
        counts = []
        maximum = 100
        changeScale = True
        number = 0
        while not self.abort:
            counts = spectrometer.read(0.1)

            while changeScale:
                if counts > maximum:
                    maximum *= 10

                elif counts < maximum/10:
                    maximum /= 10

                if (counts < maximum and counts > maximum/10) or counts == 0:
                    changeScale = False

            self.bar_update.emit(counts)
            playStart = int(60*1000*(counts/maximum))
            print(playStart)
            self.player.setPosition(playStart)
            print(self.player.isMuted())
            self.player.play()
            time.sleep(1)
            self.player.stop()
            number += 1
            if number >= 10:
                self.abort = True

        self.finished.emit()

class spectrometer():

    def read(self):
        return random.randint(100,1000)

if __name__ == '__main__':
    spec = spectrometer()
    opt = optimizeWorker(spec)
    opt.optimize()

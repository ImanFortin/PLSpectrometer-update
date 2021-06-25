import time
import random
from PyQt5 import QtMultimedia as qtmm
from PyQt5.QtCore import QObject, QThread, pyqtSignal
from PyQt5 import QtCore as qtc
from PyQt5 import QtWidgets as qtw
import sys

class optimizeWorker(QObject):

    bar_update = pyqtSignal(int)
    finished = pyqtSignal()

    def __init__(self,spectrometer):
        super().__init__()
        self.abort = False
        self.player = qtmm.QMediaPlayer()
        # Volume
        url = qtc.QUrl(qtc.QDir.currentPath()+'/workers/chirp.wav')
        print(url)
        self.player.setVolume(10)
        self.set_file(url)
        self.spectrometer = spectrometer

    def set_file(self, url):
        if url.scheme() == '':
            url.setScheme('file')
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

            counts = self.spectrometer.read()

            while changeScale:
                if counts >= maximum:
                    maximum *= 10

                elif counts < maximum/10:
                    maximum /= 10

                if (counts < maximum and counts >= maximum/10) or counts == 0:
                    changeScale = False

            self.bar_update.emit(counts)
            playStart = int(60*1000*(counts/maximum))
            print(playStart)
            # self.player.setPosition(playStart)
            self.player.play()
            time.sleep(0.2)
            self.player.stop()
            number += 1
            if number >= 10:
                self.abort = True

        self.finished.emit()

class spectrometer():

    def __init__(self):
        self.x = 5
        pass

    def read(self):
        return 999

if __name__ == '__main__':
    spec = spectrometer()
    ans = spec.read()
    print(ans)
    opt = optimizeWorker(spec)
    opt.optimize()

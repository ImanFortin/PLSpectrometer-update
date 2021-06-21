import sys
import os
from PyQt5.QtCore import QObject, QThread, pyqtSignal

class searchWorker(QObject):


    sample = pyqtSignal(str)
    finished = pyqtSignal()


    def __init__(self,name,year):
        super().__init__()
        self.name = name
        self.year = year

    def search(self):
        rootdir = 'Z:\data\ZnO\PL\Data'


        i = self.name
        j = self.year


        if i == '':
            self.finished.emit()
            return

        if j == '':
            print('Searching all...')
        else:
            print('Searching ' + j + '...')

        found = False

        for subdir, dirs, files in os.walk(rootdir):
            if j in subdir:
                for file in files:
                    f = open(os.path.join(subdir, file))
                    try:
                        line = f.readline()
                        f.close()
                        if i in line or i in os.path.join(subdir, file):
                            found = True
                            self.sample.emit(os.path.join(subdir, file) + '\n' + line)

                    except UnicodeDecodeError:
                        continue

        if not found:
            self.sample.emit('no match found')

        f.close()
        self.finished.emit()

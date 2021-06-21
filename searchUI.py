from PyQt5 import QtCore, QtGui
from PyQt5 import QtWidgets as qtw
from PyQt5.QtCore import QThread
from workers.search import searchWorker
from workers.plot import plotWorker

import sys
from PyQt5.QtWidgets import (
    QApplication,
    QCheckBox,
    QFormLayout,
    QLineEdit,
    QVBoxLayout,
    QWidget,
    QPushButton,
    QScrollArea,
    QHBoxLayout,
    QProgressBar
)

class SearchUI(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle('Plotting Spectra')
        self.resize(600,600)

        #the outer most widget that will contain the other widgets
        outerLayout = QVBoxLayout()

        #the top layout this contains the search related inputs and buttons
        self.searchLayout = QFormLayout()
        self.sampleNameInput = QLineEdit()
        self.sampleYearInput = QLineEdit()
        self.searchBtn = QPushButton('Search')
        self.searchLayout.addRow('Sample Name:', self.sampleNameInput)
        self.searchLayout.addRow('Sample Year:', self.sampleYearInput)
        self.searchLayout.addRow(self.searchBtn)

        # self.scroll = QScrollArea()
        self.fileDisplay = qtw.QPlainTextEdit()

        #the botton Layout
        self.plotLayout = QFormLayout()
        self.filePathInput = QLineEdit()
        self.plotBtn = QPushButton('Plot')
        self.plotLayout.addRow('Enter Path:',self.filePathInput)
        self.plotLayout.addRow(self.plotBtn)

        outerLayout.addLayout(self.searchLayout)
        outerLayout.addWidget(self.fileDisplay)
        outerLayout.addLayout(self.plotLayout)

        self.setLayout(outerLayout)
        self.connect_btns()


    def connect_btns(self):
        self.searchBtn.clicked.connect(self.search)
        self.plotBtn.clicked.connect(self.plot)

    def search(self):
        #get the sample name and year
        sampleName = self.sampleNameInput.text()
        year = self.sampleYearInput.text()
        self.fileDisplay.setPlainText('')
        #set up the thread
        self.thread = QThread()
        self.searchWorker = searchWorker(sampleName,year)
        self.searchWorker.moveToThread(self.thread)
        self.thread.started.connect(self.searchWorker.search)
        self.searchWorker.finished.connect(self.thread.quit)
        self.searchWorker.finished.connect(self.searchWorker.deleteLater)
        self.searchWorker.sample.connect(self.appendFilePath)
        self.thread.finished.connect(self.thread.deleteLater)
        self.thread.finished.connect(self.doneSearch)
        #start the thread
        self.searchBtn.setText('Searching...')
        self.thread.start()



    def appendFilePath(self,path):
        self.fileDisplay.appendPlainText(path + '\n')

    def doneSearch(self):
        self.searchBtn.setText('Search')

    def donePlot(self):
        self.plotBtn.setText('Plot')


    def plot(self):
        filepath = self.filePathInput.text()
        self.thread = QThread()
        self.plotWorker = plotWorker(filepath)
        self.plotWorker.moveToThread(self.thread)
        self.thread.started.connect(self.plotWorker.plot)
        self.plotWorker.finished.connect(self.thread.quit)
        self.plotWorker.finished.connect(self.plotWorker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.thread.finished.connect(self.donePlot)
        self.plotBtn.setText('Plotting...')
        self.thread.start()



if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    window = SearchUI()
    window.show()
    sys.exit(app.exec())

import sys
import numpy as np
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as gtg
from PyQt5 import QtCore as qtc
from plotWidget import Canvas
from Blit import BlitManager
import random
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
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


class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        outerLayout = QVBoxLayout()
        self.wavelength_plot = Canvas(parent = self)
        toolbar = NavigationToolbar(self.wavelength_plot, self)
        outerLayout.addWidget(toolbar)
        outerLayout.addWidget(self.wavelength_plot)
        self.setLayout(outerLayout)
        self.show()
        x = np.linspace(0, 2 * np.pi, 500)

        for j in range(500):
            # update the artists
            self.wavelength_plot.add_data(x[j],2*np.sin(x[j]  * np.pi))


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec())

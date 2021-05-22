from PyQt5.QtWidgets import *
import sys
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import numpy as np
import mplcursors
from PyQt5 import QtCore


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        title = "Matplotlib Embeding In PyQt5"
        top = 400
        left = 400
        width = 900
        height = 500

        self.setWindowTitle(title)
        self.setGeometry(top, left, width, height)

        self.MyUI()


    def MyUI(self):


        # frame = QFrame(self)
        # frame.setGeometry(QtCore.QRect(100, 40, 500, 500))
        # frame.setFrameShape(QFrame.Box)
        # frame.setFrameShadow(QFrame.Plain)
        # frame.setLineWidth(3)


        canvas = PlotWidget(self)
        canvas.move(20,20)

        button = QPushButton("Click Me", self)
        button.move(100, 450)

        button2 = QPushButton("Click Me Two", self)
        button2.move(250, 450)


class Canvas(FigureCanvas):
    def __init__(self, parent = None, width = 5, height = 5, dpi = 100, scale = 'linear'):

        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        self.axes.grid()
        self.axes.set_yscale(scale)
        super().__init__(fig)
        self.setParent(parent)





class PlotWidget(QWidget):

    def __init__(self, parent = None, scale = 'linear', *args, **kwargs):
        super().__init__(*args, **kwargs) #run the init function of the parent (QWidget)
        self.setParent(parent) # set our parent to the given argument to that is shows up
        layout = QVBoxLayout() #make a vertical layout

        self.ydata = []
        self.xdata = []


        self.sc = Canvas(self, width=5, height=4, dpi=100, scale = scale) #make our canvas

        self.lines = self.sc.axes.scatter(self.xdata, self.ydata, s = 3) #plot the dots
        self.sc.axes.plot(self.xdata, self.ydata) #plot line to connect the dots

        mplcursors.cursor(self.lines, hover = True)
        # Create toolbar, passing canvas as first parament, parent (self, the MainWindow) as second.
        toolbar = NavigationToolbar(self.sc, self)

        #add our toolbar and plot to the widget
        layout.addWidget(toolbar)
        layout.addWidget(self.sc)
        self.setLayout(layout)

    def update(self,xdata,ydata):

        self.ydata.append(ydata)
        self.xdata.append(xdata)
        self.sc.axes.cla()
        self.lines = self.sc.axes.scatter(self.xdata,self.ydata)
        self.sc.axes.plot(self.xdata,self.ydata)
        mplcursors.cursor(self.lines, hover = True)
        self.sc.draw()

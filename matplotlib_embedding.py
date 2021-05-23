from PyQt5.QtWidgets import *
import sys
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import numpy as np
import mplcursors
from PyQt5 import QtCore



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
        self.sc.axes.grid()
        mplcursors.cursor(self.lines, hover = True)
        # Create toolbar, passing canvas as first parament, parent (self, the MainWindow) as second.
        toolbar = NavigationToolbar(self.sc, self)

        #add our toolbar and plot to the widget
        layout.addWidget(toolbar)
        layout.addWidget(self.sc)
        self.setLayout(layout)

    def update(self,xdata,ydata):

        self.ydata.append(ydata)#append the y data
        self.xdata.append(xdata)#append the x data
        self.sc.axes.cla()#clear the canvas
        self.lines = self.sc.axes.scatter(self.xdata,self.ydata, s = 3)#add new data
        self.sc.axes.plot(self.xdata,self.ydata)#reconnect the lines
        mplcursors.cursor(self.lines, hover = True)#add the cursor
        self.sc.axes.grid()#make the grid
        self.sc.draw()#show the plot

    def clear(self):
        self.ydata.clear()
        self.xdata.clear()
        self.sc.axes.cla()

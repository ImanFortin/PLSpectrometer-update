from PyQt5.QtWidgets import *
import sys
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import mplcursors
from Blit import BlitManager
from PyQt5 import QtCore



class Canvas(FigureCanvas):
    def __init__(self, parent = None, dpi = 100):

        self.fig = Figure(dpi=dpi, linewidth = 2, edgecolor = (0,0,0));
        self.ax = self.fig.add_subplot(111)
        super().__init__(self.fig)

        self.fig.set_facecolor((170/255,170/255,170/255,170/255))
        self.ax.set_facecolor((0,0,0,1))
        self.ax.set_xlim(0,2*np.pi)
        self.ax.set_ylim(-1,1)
        self.xdata = []
        self.ydata = []
        self.plot_ref = self.ax.plot(self.xdata,self.ydata)[0]
        plt.close()
        # make sure our window is on the screen and drawn
        self.show()


    def update_plot(self,xdata,ydata):
        # update the artists
        self.ydata.append(ydata)
        self.xdata.append(xdata)
        self.plot_ref.set_ydata(self.ydata)
        self.plot_ref.set_xdata(self.xdata)

        self.draw()
        # tell the blitting manager to do its thing
        # self.bm.update()

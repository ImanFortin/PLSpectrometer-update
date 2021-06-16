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
import random


class Canvas(FigureCanvas):
    def __init__(self, parent = None, dpi = 100):

        self.fig,self.ax = plt.subplots(dpi=dpi, linewidth = 2, edgecolor = (0,0,0));

        self.fig.set_facecolor((170/255,170/255,170/255,170/255))
        self.ax.set_facecolor((0,0,0,1))
        self.ax.set_xlim(0,2*np.pi)
        self.ax.set_ylim(-2.1,2.2)
        super().__init__(self.fig)
        (self.ln,) = self.ax.plot([], [], animated=True)
        self.bm = BlitManager(self.fig.canvas, [self.ln])
        plt.tight_layout()
        plt.pause(.1)
        plt.close()
        self.max = 0

        # make sure our window is on the screen and drawn
        self.show()


    def add_data(self,xdata,ydata):
        # update the artists
        

        current_x,current_y = self.ln.get_data()
        self.ln.set_ydata(np.append(current_y,ydata))
        self.ln.set_xdata(np.append(current_x,xdata))


        # tell the blitting manager to do its thing
        self.bm.update()

import numpy as np
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc
from PyQt5 import QtChart as qtch

class Plots(qtch.QChartView):

    max = 100

    def __init__(self, name):
        super().__init__()
        # self.setParent(parent)
        self.chart = qtch.QChart(title = name)
        self.setChart(self.chart)

        self.series = qtch.QLineSeries(name = 'Counts')
        self.chart.addSeries(self.series)

        self.ydata = []
        self.xdata = []
        self.series.append([
        qtc.QPointF(x,self.ydata[index])
        for index, x in enumerate(self.xdata)
        ])

        x_axis = qtch.QValueAxis()
        x_axis.setRange(0, 10)
        y_axis = qtch.QValueAxis()
        y_axis.setRange(0,self.max)

        self.chart.setAxisX(x_axis,self.series)
        self.chart.setAxisY(y_axis,self.series)
        self.chart.setTheme(qtch.QChart.ChartThemeDark)
        self.setRenderHint(qtg.QPainter.Antialiasing)

    def set_xlim(self,min,max):
        x_axis = qtch.QValueAxis()
        x_axis.setRange(min, max)
        self.chart.setAxisX(x_axis,self.series)


    def refresh_stats(self,xdata,ydata):

        self.xdata.append(xdata)
        self.ydata.append(ydata)
        if ydata > 0.9*self.max:
            self.max = 1.2*ydata
            y_axis = qtch.QValueAxis()
            y_axis.setRange(0,self.max)
            self.chart.setAxisY(y_axis,self.series)

        new_data = [
        qtc.QPointF(x,self.ydata[index])
        for index, x in enumerate(self.xdata)]
        self.series.replace(new_data)

    def cla(self):

        self.ydata = []
        self.xdata = []

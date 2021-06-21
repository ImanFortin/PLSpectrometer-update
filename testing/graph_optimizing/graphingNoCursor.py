import numpy as np
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc
from PyQt5 import QtChart as qtch

#the linear plots
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
        #autoscaling
        if ydata > 0.9*self.max:
            self.max = 1.2*ydata
            y_axis = qtch.QValueAxis()
            y_axis.setRange(0,self.max)
            self.chart.setAxisY(y_axis,self.series)

        #to add data follow this procedure
        new_data = [
        qtc.QPointF(x,self.ydata[index])
        for index, x in enumerate(self.xdata)]
        self.series.replace(new_data)

    def cla(self):

        self.ydata = []
        self.xdata = []
        self.max = 100
        y_axis = qtch.QValueAxis()
        y_axis.setRange(0,self.max)
        self.chart.setAxisY(y_axis,self.series)

#the log plots
class LogPlots(qtch.QChartView):

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
        y_axis = qtch.QLogValueAxis()
        y_axis.setBase(10)
        y_axis.setRange(1,self.max)

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
            y_axis = qtch.QLogValueAxis()
            y_axis.setBase(10)
            y_axis.setRange(1,self.max)
            self.chart.setAxisY(y_axis,self.series)

        new_data = [
        qtc.QPointF(x,self.ydata[index])
        for index, x in enumerate(self.xdata)]
        self.series.replace(new_data)

    def cla(self):

        self.ydata = []
        self.xdata = []



class BarChartView(qtch.QChartView):

    max = 100
    min = 0
    def __init__(self,parent):
        super().__init__()
        self.chart = qtch.QChart()
        self.setChart(self.chart)
        self.series = qtch.QBarSeries()
        self.series.setBarWidth(1)
        self.chart.addSeries(self.series)
        self.chart.legend().setVisible(False)
        self.chart.setContentsMargins(-10, -10, -10, -10)
        self.bar_set = qtch.QBarSet('')
        self.series.append(self.bar_set)

        self.bar_set.append(20)

        self.x_axis = qtch.QBarCategoryAxis()

        self.x_axis.setVisible(False)
        self.chart.setAxisX(self.x_axis)
        self.series.attachAxis(self.x_axis)

        self.y_axis = qtch.QValueAxis()

        self.y_axis.setRange(0,100)
        self.y_axis.setTickCount(5)
        self.y_axis.setVisible(False)
        self.chart.setAxisY(self.y_axis)
        self.series.attachAxis(self.y_axis)

        self.series.setLabelsVisible(True)
        self.chart.layout().setContentsMargins(0,0,0,0)
        self.chart.setTheme(qtch.QChart.ChartThemeDark)
        self.setMinimumSize(10,50)

        self.setParent(parent)

    def refresh_stats(self,ydata):
        while ydata > self.max:
            self.min = self.max
            self.max *= 10

            self.y_axis.setRange(0,self.max)


        while ydata < self.min:
            self.max /= 10
            if self.min == 100:
                self.min = 0
            else:
                self.min /= 10

            self.y_axis.setRange(self.min,self.max)


        self.bar_set.replace(0,ydata)
        self.series.append(self.bar_set)

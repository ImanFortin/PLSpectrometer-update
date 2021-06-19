import sys
import numpy as np
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc
from PyQt5 import QtChart as qtch
from collections import deque
import random
import time
import psutil
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


class MainWindow(qtw.QMainWindow):
    def __init__(self):
        super().__init__()
        tabs = qtw.QTabWidget()
        self.setCentralWidget(tabs)
        disk_usage_view = DiskUsageChartView()
        tabs.addTab(disk_usage_view, "Disk Usage")
        cpu_view = CPUUsageView()
        tabs.addTab(cpu_view, 'CPU Usage')
        plot = Plots('wavelength', Xrange = (0,200))
        tabs.addTab(plot, 'test plot')
        self.show()




class DiskUsageChartView(qtch.QChartView):
    chart_title = 'Disk Usage by Partition'

    def __init__(self):
        super().__init__()
        chart = qtch.QChart(title = self.chart_title)
        self.setChart(chart)
        series = qtch.QBarSeries()
        chart.addSeries(series)
        bar_set = qtch.QBarSet('Percent Used')
        series.append(bar_set)

        partitions = []

        bar_set.append(20)

        x_axis = qtch.QBarCategoryAxis()
        x_axis.append(partitions)
        chart.setAxisX(x_axis)
        series.attachAxis(x_axis)

        y_axis = qtch.QValueAxis()
        y_axis.setRange(0,100)
        chart.setAxisY(y_axis)
        series.attachAxis(y_axis)

        series.setLabelsVisible(True)


class Plots(qtch.QChartView):

    max = 100

    def __init__(self, name, Xrange = (0,10)):
        super().__init__()
        self.chart = qtch.QChart(title = name)
        self.setChart(self.chart)

        self.series = qtch.QSplineSeries(name = 'Counts')
        self.chart.addSeries(self.series)

        self.ydata = []
        self.xdata = []
        self.series.append([
        qtc.QPoint(x,y)
        for x,y in enumerate(self.xdata)
        ])

        x_axis = qtch.QValueAxis()
        x_axis.setRange(Xrange[0], Xrange[1])
        y_axis = qtch.QValueAxis()
        y_axis.setRange(0,self.max)

        self.chart.setAxisX(x_axis,self.series)
        self.chart.setAxisY(y_axis,self.series)
        self.chart.setTheme(qtch.QChart.ChartThemeBlueCerulean)
        self.setRenderHint(qtg.QPainter.Antialiasing)
        self.timer = qtc.QTimer(interval = 200, timeout = self.refresh_stats)
        self.timer.start()




    def refresh_stats(self):

        xdata = 1
        ydata = random.randint(0,150)
        self.xdata.append(xdata)
        self.ydata.append(ydata)

        if ydata > 0.9*self.max:
            self.max = 1.2*ydata
            y_axis = qtch.QValueAxis()
            y_axis.setRange(0,self.max)
            self.chart.setAxisY(y_axis,self.series)

        new_data = [
        qtc.QPoint(x,y)
        for x,y in enumerate(self.ydata)]
        self.series.replace(new_data)

class CPUUsageView(qtch.QChartView):

    num_data_points = 500
    chart_title = 'Cpu Utilization'

    def __init__(self):
        super().__init__()
        chart = qtch.QChart(title = self.chart_title)
        self.setChart(chart)

        self.series = qtch.QSplineSeries(name = 'Percentage')
        chart.addSeries(self.series)

        self.data = deque(
        [0] * self.num_data_points, maxlen = self.num_data_points
        )
        self.series.append([
        qtc.QPoint(x,y)
        for x, y in enumerate(self.data)]
        )

        x_axis = qtch.QValueAxis()
        x_axis.setRange(0,self.num_data_points)
        x_axis.setLabelsVisible(False)
        y_axis = qtch.QValueAxis()
        y_axis.setRange(0,100)
        chart.setAxisX(x_axis, self.series)
        chart.setAxisY(y_axis, self.series)

        self.setRenderHint(qtg.QPainter.Antialiasing)
        self.timer = qtc.QTimer(interval = 200, timeout = self.refresh_stats)
        self.timer.start()

    def keyPressEvent(self,event):
        keymap = {
        qtc.Qt.Key_Up: lambda: self.chart().scroll(0, -10),
        qtc.Qt.Key_Down: lambda: self.chart().scroll(0, 10),
        qtc.Qt.Key_Right: lambda: self.chart().scroll(-10, 0),
        qtc.Qt.Key_Left: lambda: self.chart().scroll(10, 0),
        qtc.Qt.Key_Greater: lambda: self.chart().zoomIN,
        qtc.Qt.Key_Less: lambda: self.chart().zoomOut,
        }
        callback = keymap.get(event.key())
        if callback:
            callback()

    def refresh_stats(self):
        usage = psutil.cpu_percent()
        self.data.append(usage)

        new_data = [
        qtc.QPoint(x,y)
        for x,y in enumerate(self.data)]
        self.series.replace(new_data)




if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec())

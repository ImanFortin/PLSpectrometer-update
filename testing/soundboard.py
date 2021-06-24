import sys
import time
import random
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc
from PyQt5 import QtMultimedia as qtmm
from PyQt5 import QtChart as qtch


class PlayButton(qtw.QPushButton):
    play_stylesheet = 'background-color: lightgreen; color: black;'
    stop_stylesheet = 'background-color: darkred; color: white;'

    def __init__(self):
        super().__init__('Play')
        self.setFont(qtg.QFont('Sans', 32, qtg.QFont.Bold))
        self.setSizePolicy(
            qtw.QSizePolicy.Expanding,
            qtw.QSizePolicy.Expanding
        )
        self.setStyleSheet(self.play_stylesheet)

    def on_state_changed(self, state):
        if state == qtmm.QMediaPlayer.PlayingState:
            self.setStyleSheet(self.stop_stylesheet)
            self.setText('Stop')
        else:
            self.setStyleSheet(self.play_stylesheet)
            self.setText('Play')


class BarChartView(qtch.QChartView):

    max = 100
    min = 0
    def __init__(self):
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
        self.y_axis.setLabelFormat("%.1e")
        self.chart.setAxisY(self.y_axis)
        self.series.attachAxis(self.y_axis)

        self.series.setLabelsVisible(True)
        self.chart.layout().setContentsMargins(0,0,0,0)
        self.chart.setTheme(qtch.QChart.ChartThemeDark)
        self.chart.setMinimumSize(150,100)


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

class SoundWidget(qtw.QWidget):

    def __init__(self):
        super().__init__()
        self.setLayout(qtw.QGridLayout())

        # Playback
        self.label = qtw.QLabel("No file loaded")
        self.layout().addWidget(self.label, 0, 0, 1, 2)

        self.play_button = PlayButton()
        self.layout().addWidget(self.play_button, 3, 0, 1, 2)

        self.player = qtmm.QMediaPlayer()
        self.play_button.clicked.connect(self.on_playbutton)
        self.player.stateChanged.connect(self.play_button.on_state_changed)

        
        # Slider
        self.position = qtw.QSlider(
            minimum=0, orientation=qtc.Qt.Horizontal)
        self.layout().addWidget(self.position, 1, 0, 1, 2)

        self.player.positionChanged.connect(self.position.setSliderPosition)
        self.player.durationChanged.connect(self.position.setMaximum)
        self.position.sliderMoved.connect(self.player.setPosition)

        # Volume
        self.volume = qtw.QSlider(
            minimum=0,
            maximum=100,
            sliderPosition=75,
            orientation=qtc.Qt.Horizontal,
            sliderMoved=self.player.setVolume
        )
        self.layout().addWidget(self.volume, 2, 0)
        url = qtc.QUrl(qtc.QDir.currentPath()+'/testing/beep.mp3')
        self.set_file(url)


    def on_playbutton(self):
        if self.player.state() == qtmm.QMediaPlayer.PlayingState:
            self.player.stop()
        else:
            self.player.setPlaybackRate(1)
            self.player.play()


    def set_file(self, url):
        self.label.setText(url.fileName())
        if url.scheme() == '':
            url.setScheme('file')
        content = qtmm.QMediaContent(url)

        self.playlist = qtmm.QMediaPlaylist()
        self.playlist.addMedia(content)
        self.playlist.setCurrentIndex(1)
        self.player.setPlaylist(self.playlist)



class MainWindow(qtw.QMainWindow):

    def __init__(self):
        """MainWindow constructor.

        Code in this method should define window properties,
        create backend resources, etc.
        """
        super().__init__()
        rows = 3
        columns = 3
        soundboard = qtw.QWidget()
        soundboard.setLayout(qtw.QGridLayout())
        self.setCentralWidget(soundboard)

        verticalSpacer = qtw.QSpacerItem(200, 40, qtw.QSizePolicy.Minimum, qtw.QSizePolicy.Expanding)
        soundboard.layout().addItem(verticalSpacer,0,2)

        self.bar = BarChartView()
        soundboard.layout().addWidget(self.bar,0,4,0,4)

        sw = SoundWidget()
        soundboard.layout().addWidget(sw)

        # Code ends here
        self.bar.refresh_stats(1000000)
        # self.bar.refresh_stats(25)
        self.show()


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    # it's required to save a reference to MainWindow.
    # if it goes out of scope, it will be destroyed.
    mw = MainWindow()
    mw.resize(300,200)
    sys.exit(app.exec())

from qt_designer_GUI import Ui_MainWindow
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from spectrometer import Spectrometer

class MainWindow(qtw.QMainWindow):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.spectrometer = Spectrometer()




    def move(self):
        pass


    def close():
        pass

if __name__ == '__main__':
    import sys
    app = qtw.QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'spectrometer.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1022, 748)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.abort_button = QtWidgets.QPushButton(self.centralwidget)
        self.abort_button.setGeometry(QtCore.QRect(10, 610, 141, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.abort_button.setFont(font)
        self.abort_button.setStyleSheet("QPushButton{\n"
"    background-color: rgb(255, 0, 0)\n"
"}")
        self.abort_button.setAutoDefault(False)
        self.abort_button.setDefault(False)
        self.abort_button.setFlat(False)
        self.abort_button.setObjectName("abort_button")
        self.close_button = QtWidgets.QPushButton(self.centralwidget)
        self.close_button.setGeometry(QtCore.QRect(170, 610, 141, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.close_button.setFont(font)
        self.close_button.setStyleSheet("QPushButton{\n"
"    background-color: rgb(255, 0, 0)\n"
"}")
        self.close_button.setAutoDefault(False)
        self.close_button.setDefault(False)
        self.close_button.setFlat(False)
        self.close_button.setObjectName("close_button")
        self.property_label = QtWidgets.QLabel(self.centralwidget)
        self.property_label.setGeometry(QtCore.QRect(20, 20, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.property_label.setFont(font)
        self.property_label.setObjectName("property_label")
        self.current_wavelength_lbl = QtWidgets.QLabel(self.centralwidget)
        self.current_wavelength_lbl.setGeometry(QtCore.QRect(20, 40, 101, 21))
        self.current_wavelength_lbl.setObjectName("current_wavelength_lbl")
        self.dial = QtWidgets.QDial(self.centralwidget)
        self.dial.setGeometry(QtCore.QRect(350, 10, 50, 64))
        self.dial.setSingleStep(1)
        self.dial.setOrientation(QtCore.Qt.Horizontal)
        self.dial.setInvertedAppearance(False)
        self.dial.setWrapping(False)
        self.dial.setNotchesVisible(False)
        self.dial.setObjectName("dial")
        self.frame1 = QtWidgets.QFrame(self.centralwidget)
        self.frame1.setGeometry(QtCore.QRect(10, 10, 321, 121))
        self.frame1.setFrameShape(QtWidgets.QFrame.Box)
        self.frame1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame1.setLineWidth(3)
        self.frame1.setObjectName("frame1")
        self.frame2 = QtWidgets.QFrame(self.centralwidget)
        self.frame2.setGeometry(QtCore.QRect(10, 140, 241, 131))
        self.frame2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame2.setLineWidth(3)
        self.frame2.setObjectName("frame2")
        self.actual_value_lbl = QtWidgets.QLabel(self.frame2)
        self.actual_value_lbl.setGeometry(QtCore.QRect(10, 0, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.actual_value_lbl.setFont(font)
        self.actual_value_lbl.setObjectName("actual_value_lbl")
        self.recalibrate_input = QtWidgets.QLineEdit(self.frame2)
        self.recalibrate_input.setGeometry(QtCore.QRect(10, 30, 113, 20))
        self.recalibrate_input.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.recalibrate_input.setObjectName("recalibrate_input")
        self.recalibrate_button = QtWidgets.QPushButton(self.frame2)
        self.recalibrate_button.setGeometry(QtCore.QRect(10, 60, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.recalibrate_button.setFont(font)
        self.recalibrate_button.setMouseTracking(False)
        self.recalibrate_button.setStyleSheet("QPushButton{\n"
"    background-color: rgb(64, 137, 255);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 20px;\n"
"    min-width: 2em;\n"
"    padding: 6px;\n"
"    \n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"    background-color: green;\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-width: 5em;\n"
"    padding: 6px;\n"
"    \n"
"}")
        self.recalibrate_button.setCheckable(False)
        self.recalibrate_button.setAutoDefault(False)
        self.recalibrate_button.setDefault(False)
        self.recalibrate_button.setFlat(False)
        self.recalibrate_button.setObjectName("recalibrate_button")
        self.frame3 = QtWidgets.QFrame(self.centralwidget)
        self.frame3.setGeometry(QtCore.QRect(10, 280, 241, 131))
        self.frame3.setFrameShape(QtWidgets.QFrame.Box)
        self.frame3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame3.setLineWidth(3)
        self.frame3.setObjectName("frame3")
        self.move_input = QtWidgets.QLineEdit(self.frame3)
        self.move_input.setGeometry(QtCore.QRect(10, 30, 113, 20))
        self.move_input.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.move_input.setObjectName("move_input")
        self.move_to_lbl = QtWidgets.QLabel(self.frame3)
        self.move_to_lbl.setGeometry(QtCore.QRect(10, 0, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.move_to_lbl.setFont(font)
        self.move_to_lbl.setObjectName("move_to_lbl")
        self.move_button = QtWidgets.QPushButton(self.frame3)
        self.move_button.setGeometry(QtCore.QRect(10, 60, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.move_button.setFont(font)
        self.move_button.setMouseTracking(False)
        self.move_button.setStyleSheet("QPushButton{\n"
"    background-color: rgb(64, 137, 255);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 20px;\n"
"    min-width: 2em;\n"
"    padding: 6px;\n"
"    \n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"    background-color: green;\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-width: 5em;\n"
"    padding: 6px;\n"
"    \n"
"}")
        self.move_button.setCheckable(False)
        self.move_button.setAutoDefault(False)
        self.move_button.setDefault(False)
        self.move_button.setFlat(False)
        self.move_button.setObjectName("move_button")
        self.frame4 = QtWidgets.QFrame(self.centralwidget)
        self.frame4.setGeometry(QtCore.QRect(10, 420, 351, 151))
        self.frame4.setFrameShape(QtWidgets.QFrame.Box)
        self.frame4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame4.setLineWidth(3)
        self.frame4.setObjectName("frame4")
        self.scan_start_input = QtWidgets.QLineEdit(self.frame4)
        self.scan_start_input.setGeometry(QtCore.QRect(10, 30, 71, 20))
        self.scan_start_input.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.scan_start_input.setObjectName("scan_start_input")
        self.scan_start_lbl = QtWidgets.QLabel(self.frame4)
        self.scan_start_lbl.setGeometry(QtCore.QRect(10, 0, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.scan_start_lbl.setFont(font)
        self.scan_start_lbl.setObjectName("scan_start_lbl")
        self.scan_end_lbl = QtWidgets.QLabel(self.frame4)
        self.scan_end_lbl.setGeometry(QtCore.QRect(100, 0, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.scan_end_lbl.setFont(font)
        self.scan_end_lbl.setObjectName("scan_end_lbl")
        self.scan_end_input = QtWidgets.QLineEdit(self.frame4)
        self.scan_end_input.setGeometry(QtCore.QRect(100, 30, 71, 20))
        self.scan_end_input.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.scan_end_input.setObjectName("scan_end_input")
        self.scan_button = QtWidgets.QPushButton(self.frame4)
        self.scan_button.setGeometry(QtCore.QRect(10, 80, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.scan_button.setFont(font)
        self.scan_button.setMouseTracking(False)
        self.scan_button.setStyleSheet("QPushButton{\n"
"    background-color: rgb(69, 87, 255);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 20px;\n"
"    min-width: 2em;\n"
"    padding: 6px;\n"
"    \n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"    background-color: rgb(11, 15, 255);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 18px;\n"
"    min-width: 5em;\n"
"    padding: 6px;\n"
"    \n"
"}")
        self.scan_button.setCheckable(False)
        self.scan_button.setAutoDefault(False)
        self.scan_button.setDefault(False)
        self.scan_button.setFlat(False)
        self.scan_button.setObjectName("scan_button")
        self.progressBar_scan = QtWidgets.QProgressBar(self.frame4)
        self.progressBar_scan.setGeometry(QtCore.QRect(130, 100, 101, 23))
        self.progressBar_scan.setProperty("value", 24)
        self.progressBar_scan.setObjectName("progressBar_scan")
        self.scan_step_lbl = QtWidgets.QLabel(self.frame4)
        self.scan_step_lbl.setGeometry(QtCore.QRect(200, 0, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.scan_step_lbl.setFont(font)
        self.scan_step_lbl.setObjectName("scan_step_lbl")
        self.scan_step_input = QtWidgets.QLineEdit(self.frame4)
        self.scan_step_input.setGeometry(QtCore.QRect(200, 30, 71, 20))
        self.scan_step_input.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.scan_step_input.setObjectName("scan_step_input")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1022, 31))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionnew = QtWidgets.QAction(MainWindow)
        self.actionnew.setObjectName("actionnew")
        self.actionsave = QtWidgets.QAction(MainWindow)
        self.actionsave.setObjectName("actionsave")
        self.actionsave_as = QtWidgets.QAction(MainWindow)
        self.actionsave_as.setObjectName("actionsave_as")
        self.actioncopy = QtWidgets.QAction(MainWindow)
        self.actioncopy.setObjectName("actioncopy")
        self.menuFile.addAction(self.actionnew)
        self.menuFile.addAction(self.actionsave)
        self.menuFile.addAction(self.actionsave_as)
        self.menuFile.addAction(self.actioncopy)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.abort_button.setText(_translate("MainWindow", "Abort"))
        self.close_button.setText(_translate("MainWindow", "Close"))
        self.property_label.setText(_translate("MainWindow", "Properties"))
        self.current_wavelength_lbl.setText(_translate("MainWindow", "Current Wavelength:"))
        self.actual_value_lbl.setText(_translate("MainWindow", "actual value"))
        self.recalibrate_button.setText(_translate("MainWindow", "Recalibrate"))
        self.move_to_lbl.setText(_translate("MainWindow", "move to"))
        self.move_button.setText(_translate("MainWindow", "GO"))
        self.scan_start_lbl.setText(_translate("MainWindow", "start "))
        self.scan_end_lbl.setText(_translate("MainWindow", "End"))
        self.scan_button.setText(_translate("MainWindow", "GO"))
        self.scan_step_lbl.setText(_translate("MainWindow", "step"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.actionnew.setText(_translate("MainWindow", "new"))
        self.actionsave.setText(_translate("MainWindow", "save"))
        self.actionsave_as.setText(_translate("MainWindow", "save as"))
        self.actioncopy.setText(_translate("MainWindow", "copy"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


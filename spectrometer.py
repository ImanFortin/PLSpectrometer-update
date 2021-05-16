# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'spectrometer.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1022, 748)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.box_scan = QtWidgets.QLabel(self.centralwidget)
        self.box_scan.setGeometry(QtCore.QRect(10, 420, 241, 161))
        self.box_scan.setFrameShape(QtWidgets.QFrame.Box)
        self.box_scan.setLineWidth(3)
        self.box_scan.setText("")
        self.box_scan.setObjectName("box_scan")
        self.scan_start_lbl = QtWidgets.QLabel(self.centralwidget)
        self.scan_start_lbl.setGeometry(QtCore.QRect(30, 430, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.scan_start_lbl.setFont(font)
        self.scan_start_lbl.setObjectName("scan_start_lbl")
        self.scan_end_lbl = QtWidgets.QLabel(self.centralwidget)
        self.scan_end_lbl.setGeometry(QtCore.QRect(160, 430, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.scan_end_lbl.setFont(font)
        self.scan_end_lbl.setObjectName("scan_end_lbl")
        self.start_input = QtWidgets.QLabel(self.centralwidget)
        self.start_input.setGeometry(QtCore.QRect(30, 450, 71, 21))
        self.start_input.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.start_input.setFrameShape(QtWidgets.QFrame.Panel)
        self.start_input.setFrameShadow(QtWidgets.QFrame.Plain)
        self.start_input.setObjectName("start_input")
        self.end_input = QtWidgets.QLabel(self.centralwidget)
        self.end_input.setGeometry(QtCore.QRect(160, 450, 71, 21))
        self.end_input.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.end_input.setFrameShape(QtWidgets.QFrame.Panel)
        self.end_input.setObjectName("end_input")
        self.progressBar_scan = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_scan.setGeometry(QtCore.QRect(140, 530, 101, 23))
        self.progressBar_scan.setProperty("value", 24)
        self.progressBar_scan.setObjectName("progressBar_scan")
        self.box_scan_2 = QtWidgets.QLabel(self.centralwidget)
        self.box_scan_2.setGeometry(QtCore.QRect(10, 280, 241, 131))
        self.box_scan_2.setFrameShape(QtWidgets.QFrame.Box)
        self.box_scan_2.setLineWidth(3)
        self.box_scan_2.setText("")
        self.box_scan_2.setObjectName("box_scan_2")
        self.move_to_lbl = QtWidgets.QLabel(self.centralwidget)
        self.move_to_lbl.setGeometry(QtCore.QRect(20, 280, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.move_to_lbl.setFont(font)
        self.move_to_lbl.setObjectName("move_to_lbl")
        self.start_input_2 = QtWidgets.QLabel(self.centralwidget)
        self.start_input_2.setGeometry(QtCore.QRect(20, 310, 71, 21))
        self.start_input_2.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.start_input_2.setFrameShape(QtWidgets.QFrame.Panel)
        self.start_input_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.start_input_2.setObjectName("start_input_2")
        self.box_scan_3 = QtWidgets.QLabel(self.centralwidget)
        self.box_scan_3.setGeometry(QtCore.QRect(10, 140, 241, 131))
        self.box_scan_3.setFrameShape(QtWidgets.QFrame.Box)
        self.box_scan_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.box_scan_3.setLineWidth(3)
        self.box_scan_3.setText("")
        self.box_scan_3.setObjectName("box_scan_3")
        self.start_input_3 = QtWidgets.QLabel(self.centralwidget)
        self.start_input_3.setGeometry(QtCore.QRect(20, 170, 71, 21))
        self.start_input_3.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.start_input_3.setFrameShape(QtWidgets.QFrame.Panel)
        self.start_input_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.start_input_3.setObjectName("start_input_3")
        self.actual_value_lbl = QtWidgets.QLabel(self.centralwidget)
        self.actual_value_lbl.setGeometry(QtCore.QRect(20, 140, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.actual_value_lbl.setFont(font)
        self.actual_value_lbl.setObjectName("actual_value_lbl")
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
        self.scan_button = QtWidgets.QPushButton(self.centralwidget)
        self.scan_button.setGeometry(QtCore.QRect(20, 510, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.scan_button.setFont(font)
        self.scan_button.setMouseTracking(False)
        self.scan_button.setStyleSheet("QPushButton{\n"
"    background-color: rgb(0, 255, 0);\n"
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
        self.scan_button.setCheckable(False)
        self.scan_button.setAutoDefault(False)
        self.scan_button.setDefault(False)
        self.scan_button.setFlat(False)
        self.scan_button.setObjectName("scan_button")
        self.move_button = QtWidgets.QPushButton(self.centralwidget)
        self.move_button.setGeometry(QtCore.QRect(20, 350, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.move_button.setFont(font)
        self.move_button.setMouseTracking(False)
        self.move_button.setStyleSheet("QPushButton{\n"
"    background-color: rgb(0, 255, 0);\n"
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
        self.recalibrate_button = QtWidgets.QPushButton(self.centralwidget)
        self.recalibrate_button.setGeometry(QtCore.QRect(20, 210, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.recalibrate_button.setFont(font)
        self.recalibrate_button.setMouseTracking(False)
        self.recalibrate_button.setStyleSheet("QPushButton{\n"
"    background-color: rgb(0, 255, 0);\n"
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
        self.box_scan_4 = QtWidgets.QLabel(self.centralwidget)
        self.box_scan_4.setGeometry(QtCore.QRect(10, 10, 321, 121))
        self.box_scan_4.setFrameShape(QtWidgets.QFrame.Box)
        self.box_scan_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.box_scan_4.setLineWidth(3)
        self.box_scan_4.setText("")
        self.box_scan_4.setObjectName("box_scan_4")
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
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1022, 21))
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
        self.scan_start_lbl.setText(_translate("MainWindow", "start "))
        self.scan_end_lbl.setText(_translate("MainWindow", "End"))
        self.start_input.setText(_translate("MainWindow", "TextLabel"))
        self.end_input.setText(_translate("MainWindow", "TextLabel"))
        self.move_to_lbl.setText(_translate("MainWindow", "move to"))
        self.start_input_2.setText(_translate("MainWindow", "TextLabel"))
        self.start_input_3.setText(_translate("MainWindow", "TextLabel"))
        self.actual_value_lbl.setText(_translate("MainWindow", "actual value"))
        self.abort_button.setText(_translate("MainWindow", "Abort"))
        self.close_button.setText(_translate("MainWindow", "Close"))
        self.scan_button.setText(_translate("MainWindow", "GO"))
        self.move_button.setText(_translate("MainWindow", "GO"))
        self.recalibrate_button.setText(_translate("MainWindow", "Recalibrate"))
        self.property_label.setText(_translate("MainWindow", "Properties"))
        self.current_wavelength_lbl.setText(_translate("MainWindow", "Current Wavelength:"))
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

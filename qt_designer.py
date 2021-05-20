# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qtdesigner_files/spectrometer.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1221, 932)
        MainWindow.setStyleSheet("background-color: rgb(135, 135, 135);\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.abort_button = QtWidgets.QPushButton(self.centralwidget)
        self.abort_button.setGeometry(QtCore.QRect(10, 770, 141, 71))
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
        self.close_button.setGeometry(QtCore.QRect(180, 770, 141, 71))
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
        self.frame1 = QtWidgets.QFrame(self.centralwidget)
        self.frame1.setGeometry(QtCore.QRect(10, 30, 401, 101))
        self.frame1.setFrameShape(QtWidgets.QFrame.Box)
        self.frame1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame1.setLineWidth(3)
        self.frame1.setObjectName("frame1")
        self.dial = QtWidgets.QDial(self.frame1)
        self.dial.setGeometry(QtCore.QRect(330, 10, 50, 64))
        self.dial.setSingleStep(1)
        self.dial.setSliderPosition(0)
        self.dial.setOrientation(QtCore.Qt.Horizontal)
        self.dial.setInvertedAppearance(False)
        self.dial.setWrapping(False)
        self.dial.setNotchesVisible(True)
        self.dial.setObjectName("dial")
        self.property_label = QtWidgets.QLabel(self.frame1)
        self.property_label.setGeometry(QtCore.QRect(20, 10, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.property_label.setFont(font)
        self.property_label.setObjectName("property_label")
        self.current_wavelength_lbl = QtWidgets.QLabel(self.frame1)
        self.current_wavelength_lbl.setGeometry(QtCore.QRect(20, 30, 131, 21))
        self.current_wavelength_lbl.setObjectName("current_wavelength_lbl")
        self.frame2 = QtWidgets.QFrame(self.centralwidget)
        self.frame2.setGeometry(QtCore.QRect(10, 280, 401, 91))
        self.frame2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame2.setLineWidth(3)
        self.frame2.setObjectName("frame2")
        self.actual_value_lbl = QtWidgets.QLabel(self.frame2)
        self.actual_value_lbl.setGeometry(QtCore.QRect(10, 10, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.actual_value_lbl.setFont(font)
        self.actual_value_lbl.setObjectName("actual_value_lbl")
        self.recalibrate_input = QtWidgets.QLineEdit(self.frame2)
        self.recalibrate_input.setGeometry(QtCore.QRect(10, 40, 113, 20))
        self.recalibrate_input.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.recalibrate_input.setObjectName("recalibrate_input")
        self.recalibrate_button = QtWidgets.QPushButton(self.frame2)
        self.recalibrate_button.setGeometry(QtCore.QRect(220, 20, 151, 51))
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
"    border-color: black;\n"
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
        self.recalibrate_button.setCheckable(False)
        self.recalibrate_button.setAutoDefault(False)
        self.recalibrate_button.setDefault(False)
        self.recalibrate_button.setFlat(False)
        self.recalibrate_button.setObjectName("recalibrate_button")
        self.frame3 = QtWidgets.QFrame(self.centralwidget)
        self.frame3.setGeometry(QtCore.QRect(10, 410, 401, 91))
        self.frame3.setFrameShape(QtWidgets.QFrame.Box)
        self.frame3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame3.setLineWidth(3)
        self.frame3.setObjectName("frame3")
        self.move_input = QtWidgets.QLineEdit(self.frame3)
        self.move_input.setGeometry(QtCore.QRect(10, 40, 113, 20))
        self.move_input.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.move_input.setObjectName("move_input")
        self.go_to_lbl = QtWidgets.QLabel(self.frame3)
        self.go_to_lbl.setGeometry(QtCore.QRect(10, 10, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.go_to_lbl.setFont(font)
        self.go_to_lbl.setObjectName("go_to_lbl")
        self.move_button = QtWidgets.QPushButton(self.frame3)
        self.move_button.setGeometry(QtCore.QRect(250, 20, 121, 51))
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
"    border-color: black;\n"
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
        self.move_button.setCheckable(False)
        self.move_button.setAutoDefault(False)
        self.move_button.setDefault(False)
        self.move_button.setFlat(False)
        self.move_button.setObjectName("move_button")
        self.frame4 = QtWidgets.QFrame(self.centralwidget)
        self.frame4.setGeometry(QtCore.QRect(10, 540, 401, 221))
        self.frame4.setFrameShape(QtWidgets.QFrame.Box)
        self.frame4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame4.setLineWidth(3)
        self.frame4.setObjectName("frame4")
        self.scan_start_input = QtWidgets.QLineEdit(self.frame4)
        self.scan_start_input.setGeometry(QtCore.QRect(10, 30, 71, 20))
        self.scan_start_input.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.scan_start_input.setObjectName("scan_start_input")
        self.scan_start_lbl = QtWidgets.QLabel(self.frame4)
        self.scan_start_lbl.setGeometry(QtCore.QRect(10, 10, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.scan_start_lbl.setFont(font)
        self.scan_start_lbl.setObjectName("scan_start_lbl")
        self.scan_end_lbl = QtWidgets.QLabel(self.frame4)
        self.scan_end_lbl.setGeometry(QtCore.QRect(10, 60, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.scan_end_lbl.setFont(font)
        self.scan_end_lbl.setObjectName("scan_end_lbl")
        self.scan_end_input = QtWidgets.QLineEdit(self.frame4)
        self.scan_end_input.setGeometry(QtCore.QRect(10, 80, 71, 20))
        self.scan_end_input.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.scan_end_input.setObjectName("scan_end_input")
        self.scan_button = QtWidgets.QPushButton(self.frame4)
        self.scan_button.setGeometry(QtCore.QRect(250, 30, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.scan_button.setFont(font)
        self.scan_button.setMouseTracking(False)
        self.scan_button.setStyleSheet("QPushButton{\n"
"    background-color: rgb(64, 137, 255);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
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
        self.progressBar_scan.setGeometry(QtCore.QRect(10, 180, 381, 23))
        self.progressBar_scan.setProperty("value", 24)
        self.progressBar_scan.setObjectName("progressBar_scan")
        self.scan_step_lbl = QtWidgets.QLabel(self.frame4)
        self.scan_step_lbl.setGeometry(QtCore.QRect(120, 10, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.scan_step_lbl.setFont(font)
        self.scan_step_lbl.setObjectName("scan_step_lbl")
        self.scan_step_input = QtWidgets.QLineEdit(self.frame4)
        self.scan_step_input.setGeometry(QtCore.QRect(120, 30, 71, 20))
        self.scan_step_input.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.scan_step_input.setObjectName("scan_step_input")
        self.file_name_lbl = QtWidgets.QLabel(self.frame4)
        self.file_name_lbl.setGeometry(QtCore.QRect(10, 110, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.file_name_lbl.setFont(font)
        self.file_name_lbl.setObjectName("file_name_lbl")
        self.file_name_input = QtWidgets.QLineEdit(self.frame4)
        self.file_name_input.setGeometry(QtCore.QRect(10, 140, 181, 20))
        self.file_name_input.setObjectName("file_name_input")
        self.sample_id_lbl = QtWidgets.QLabel(self.frame4)
        self.sample_id_lbl.setGeometry(QtCore.QRect(210, 110, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.sample_id_lbl.setFont(font)
        self.sample_id_lbl.setObjectName("sample_id_lbl")
        self.sample_ID_input = QtWidgets.QLineEdit(self.frame4)
        self.sample_ID_input.setGeometry(QtCore.QRect(210, 140, 181, 20))
        self.sample_ID_input.setObjectName("sample_ID_input")
        self.count_time_lbl = QtWidgets.QLabel(self.frame4)
        self.count_time_lbl.setGeometry(QtCore.QRect(120, 60, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.count_time_lbl.setFont(font)
        self.count_time_lbl.setObjectName("count_time_lbl")
        self.count_time_input = QtWidgets.QLineEdit(self.frame4)
        self.count_time_input.setGeometry(QtCore.QRect(120, 80, 71, 20))
        self.count_time_input.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.count_time_input.setObjectName("count_time_input")
        self.perform_scan_lbl = QtWidgets.QLabel(self.centralwidget)
        self.perform_scan_lbl.setGeometry(QtCore.QRect(10, 510, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.perform_scan_lbl.setFont(font)
        self.perform_scan_lbl.setObjectName("perform_scan_lbl")
        self.move_spectrometer_lbl = QtWidgets.QLabel(self.centralwidget)
        self.move_spectrometer_lbl.setGeometry(QtCore.QRect(10, 380, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.move_spectrometer_lbl.setFont(font)
        self.move_spectrometer_lbl.setObjectName("move_spectrometer_lbl")
        self.recalibrate_lbl = QtWidgets.QLabel(self.centralwidget)
        self.recalibrate_lbl.setGeometry(QtCore.QRect(10, 250, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.recalibrate_lbl.setFont(font)
        self.recalibrate_lbl.setObjectName("recalibrate_lbl")
        self.position_lbl = QtWidgets.QLabel(self.centralwidget)
        self.position_lbl.setGeometry(QtCore.QRect(10, 0, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.position_lbl.setFont(font)
        self.position_lbl.setObjectName("position_lbl")
        self.common_variables_lbl = QtWidgets.QLabel(self.centralwidget)
        self.common_variables_lbl.setGeometry(QtCore.QRect(10, 140, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.common_variables_lbl.setFont(font)
        self.common_variables_lbl.setObjectName("common_variables_lbl")
        self.frame2_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame2_2.setGeometry(QtCore.QRect(10, 160, 401, 91))
        self.frame2_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame2_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame2_2.setLineWidth(3)
        self.frame2_2.setObjectName("frame2_2")
        self.radioButton = QtWidgets.QRadioButton(self.frame2_2)
        self.radioButton.setGeometry(QtCore.QRect(20, 50, 51, 17))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.frame2_2)
        self.radioButton_2.setGeometry(QtCore.QRect(90, 50, 51, 17))
        self.radioButton_2.setObjectName("radioButton_2")
        self.spect_select_lbl = QtWidgets.QLabel(self.frame2_2)
        self.spect_select_lbl.setGeometry(QtCore.QRect(20, 20, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.spect_select_lbl.setFont(font)
        self.spect_select_lbl.setObjectName("spect_select_lbl")
        self.spect_select_lbl_2 = QtWidgets.QLabel(self.frame2_2)
        self.spect_select_lbl_2.setGeometry(QtCore.QRect(250, 20, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.spect_select_lbl_2.setFont(font)
        self.spect_select_lbl_2.setObjectName("spect_select_lbl_2")
        self.lineEdit = QtWidgets.QLineEdit(self.frame2_2)
        self.lineEdit.setGeometry(QtCore.QRect(250, 50, 131, 20))
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1221, 21))
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
        self.actual_value_lbl.setText(_translate("MainWindow", "actual value (nm)"))
        self.recalibrate_button.setText(_translate("MainWindow", "Recalibrate"))
        self.go_to_lbl.setText(_translate("MainWindow", "go to value (nm)"))
        self.move_button.setText(_translate("MainWindow", "Move"))
        self.scan_start_lbl.setText(_translate("MainWindow", "Start (nm)"))
        self.scan_end_lbl.setText(_translate("MainWindow", "End (nm)"))
        self.scan_button.setText(_translate("MainWindow", "Scan"))
        self.scan_step_lbl.setText(_translate("MainWindow", "Step size (nm)"))
        self.file_name_lbl.setText(_translate("MainWindow", "File Name"))
        self.sample_id_lbl.setText(_translate("MainWindow", "Sample ID"))
        self.count_time_lbl.setText(_translate("MainWindow", "Count Time (s)"))
        self.perform_scan_lbl.setText(_translate("MainWindow", "Perform Scan"))
        self.move_spectrometer_lbl.setText(_translate("MainWindow", "Move Spectrometer"))
        self.recalibrate_lbl.setText(_translate("MainWindow", "Recalibrate Spectrometer"))
        self.position_lbl.setText(_translate("MainWindow", "Position and movement"))
        self.common_variables_lbl.setText(_translate("MainWindow", "Common Variables"))
        self.radioButton.setText(_translate("MainWindow", "double"))
        self.radioButton_2.setText(_translate("MainWindow", "single"))
        self.spect_select_lbl.setText(_translate("MainWindow", "spectrometer"))
        self.spect_select_lbl_2.setText(_translate("MainWindow", "Pulse Frequency"))
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


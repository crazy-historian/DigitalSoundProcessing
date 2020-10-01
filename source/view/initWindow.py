# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'initWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

from PyQt5 import QtCore, QtGui, QtWidgets


class InitWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(637, 366)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.rateLabel = QtWidgets.QLabel(self.centralwidget)
        self.rateLabel.setGeometry(QtCore.QRect(30, 20, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rateLabel.setFont(font)
        self.rateLabel.setObjectName("rateLabel")
        self.radioButtonRate1 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButtonRate1.setGeometry(QtCore.QRect(80, 70, 51, 17))
        self.radioButtonRate1.setObjectName("radioButtonRate1")
        self.radioButtonRate2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButtonRate2.setGeometry(QtCore.QRect(80, 100, 51, 17))
        self.radioButtonRate2.setObjectName("radioButtonRate2")
        self.radioButtonRate3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButtonRate3.setGeometry(QtCore.QRect(80, 130, 51, 17))
        self.radioButtonRate3.setObjectName("radioButtonRate3")
        self.channelLabel = QtWidgets.QLabel(self.centralwidget)
        self.channelLabel.setGeometry(QtCore.QRect(440, 20, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.channelLabel.setFont(font)
        self.channelLabel.setObjectName("channelLabel")
        self.radioButtonChannel1 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButtonChannel1.setGeometry(QtCore.QRect(470, 70, 82, 17))
        self.radioButtonChannel1.setObjectName("radioButtonChannel1")
        self.radioButtonChannel2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButtonChannel2.setGeometry(QtCore.QRect(470, 110, 91, 17))
        self.radioButtonChannel2.setChecked(False)
        self.radioButtonChannel2.setAutoExclusive(True)
        self.radioButtonChannel2.setObjectName("radioButtonChannel2")
        self.radioButtonChunk2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButtonChunk2.setGeometry(QtCore.QRect(290, 100, 51, 17))
        self.radioButtonChunk2.setObjectName("radioButtonChunk2")
        self.radioButtonChunk1 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButtonChunk1.setGeometry(QtCore.QRect(290, 70, 41, 17))
        self.radioButtonChunk1.setObjectName("radioButtonChunk1")
        self.chunkLabel = QtWidgets.QLabel(self.centralwidget)
        self.chunkLabel.setGeometry(QtCore.QRect(260, 20, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.chunkLabel.setFont(font)
        self.chunkLabel.setObjectName("chunkLabel")
        self.radioButtonChunk3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButtonChunk3.setGeometry(QtCore.QRect(290, 130, 51, 17))
        self.radioButtonChunk3.setObjectName("radioButtonChunk3")
        self.pushButtonStartRecord = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonStartRecord.setGeometry(QtCore.QRect(80, 180, 471, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButtonStartRecord.setFont(font)
        self.pushButtonStartRecord.setObjectName("pushButtonStartRecord")
        self.pushButtonStopRecord = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonStopRecord.setGeometry(QtCore.QRect(80, 250, 471, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButtonStopRecord.setFont(font)
        self.pushButtonStopRecord.setObjectName("pushButtonStopRecord")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 637, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.rateLabel.setText(_translate("MainWindow", "Частота дискретизации"))
        self.radioButtonRate1.setText(_translate("MainWindow", "12000"))
        self.radioButtonRate2.setText(_translate("MainWindow", "24000"))
        self.radioButtonRate3.setText(_translate("MainWindow", "48000"))
        self.channelLabel.setText(_translate("MainWindow", "Число каналов записи"))
        self.radioButtonChannel1.setText(_translate("MainWindow", "Один (Моно)"))
        self.radioButtonChannel2.setText(_translate("MainWindow", "Два (Стерео)"))
        self.radioButtonChunk2.setText(_translate("MainWindow", "512"))
        self.radioButtonChunk1.setText(_translate("MainWindow", "256"))
        self.chunkLabel.setText(_translate("MainWindow", "Размер буфера"))
        self.radioButtonChunk3.setText(_translate("MainWindow", "1024"))
        self.pushButtonStartRecord.setText(_translate("MainWindow", "Начать запись"))
        self.pushButtonStopRecord.setText(_translate("MainWindow", "Остановить запись"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = InitWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

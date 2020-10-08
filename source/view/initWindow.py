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

    def setupUI(self):
        #self.setGeometry(637, 366)
        self.resize(637, 366)
        self.setWindowTitle("Init audio recording")
        self.setObjectName("InitWindow")
        self.font = QtGui.QFont()
        self.font.setPointSize(12)
        self.setupWidgets()
        self.relateUI()
        self.show()

    def setupWidgets(self):
        # rate column
        self.rateLabel = QtWidgets.QLabel(self)
        self.rateLabel.setGeometry(QtCore.QRect(30, 20, 171, 41))
        self.rateLabel.setFont(self.font)
        self.rateLabel.setObjectName("rateLabel")

        self.radioButtonRate1 = QtWidgets.QRadioButton(self)
        self.radioButtonRate1.setGeometry(QtCore.QRect(80, 70, 51, 17))
        self.radioButtonRate1.setObjectName("radioButtonRate1")

        self.radioButtonRate2 = QtWidgets.QRadioButton(self)
        self.radioButtonRate2.setGeometry(QtCore.QRect(80, 100, 51, 17))
        self.radioButtonRate2.setObjectName("radioButtonRate2")

        self.radioButtonRate3 = QtWidgets.QRadioButton(self)
        self.radioButtonRate3.setGeometry(QtCore.QRect(80, 130, 51, 17))
        self.radioButtonRate3.setObjectName("radioButtonRate3")

        # chunk-size column
        self.chunkLabel = QtWidgets.QLabel(self)
        self.chunkLabel.setGeometry(QtCore.QRect(260, 20, 111, 41))
        self.chunkLabel.setFont(self.font)
        self.chunkLabel.setObjectName("chunkLabel")

        self.radioButtonChunk1 = QtWidgets.QRadioButton(self)
        self.radioButtonChunk1.setGeometry(QtCore.QRect(290, 70, 41, 17))
        self.radioButtonChunk1.setObjectName("radioButtonChunk1")

        self.radioButtonChunk2 = QtWidgets.QRadioButton(self)
        self.radioButtonChunk2.setGeometry(QtCore.QRect(290, 100, 51, 17))
        self.radioButtonChunk2.setObjectName("radioButtonChunk2")

        self.radioButtonChunk3 = QtWidgets.QRadioButton(self)
        self.radioButtonChunk3.setGeometry(QtCore.QRect(290, 130, 51, 17))
        self.radioButtonChunk3.setObjectName("radioButtonChunk3")

        # number-of-channels column
        self.channelLabel = QtWidgets.QLabel(self)
        self.channelLabel.setGeometry(QtCore.QRect(440, 20, 171, 41))
        self.channelLabel.setFont(self.font)
        self.channelLabel.setObjectName("channelLabel")

        self.radioButtonChannel1 = QtWidgets.QRadioButton(self)
        self.radioButtonChannel1.setGeometry(QtCore.QRect(470, 70, 82, 17))
        self.radioButtonChannel1.setObjectName("radioButtonChannel1")

        self.radioButtonChannel2 = QtWidgets.QRadioButton(self)
        self.radioButtonChannel2.setGeometry(QtCore.QRect(470, 110, 91, 17))
        self.radioButtonChannel2.setObjectName("radioButtonChannel2")

        # push-button columns
        self.pushButtonStartRecord = QtWidgets.QPushButton(self)
        self.pushButtonStartRecord.setFont(self.font)
        self.pushButtonStartRecord.setGeometry(QtCore.QRect(80, 180, 471, 61))
        self.pushButtonStartRecord.setObjectName("pushButtonStartRecord")

        self.pushButtonStopRecord = QtWidgets.QPushButton(self)
        self.pushButtonStopRecord.setFont(self.font)
        self.pushButtonStopRecord.setGeometry(QtCore.QRect(80, 250, 471, 61))
        self.pushButtonStopRecord.setObjectName("pushButtonStopRecord")

    def relateUI(self):
        self._translate = QtCore.QCoreApplication.translate
        # MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        # rate column
        self.rateLabel.setText(self._translate("MainWindow", "Частота дискретизации"))
        self.radioButtonRate1.setText(self._translate("MainWindow", "12000"))
        self.radioButtonRate2.setText(self._translate("MainWindow", "24000"))
        self.radioButtonRate3.setText(self._translate("MainWindow", "48000"))
        # chunk-size
        self.chunkLabel.setText(self._translate("MainWindow", "Размер буфера"))
        self.radioButtonChunk1.setText(self._translate("MainWindow", "256"))
        self.radioButtonChunk2.setText(self._translate("MainWindow", "512"))
        self.radioButtonChunk3.setText(self._translate("MainWindow", "1024"))
        # number-of-channels column
        self.channelLabel.setText(self._translate("MainWindow", "Число каналов записи"))
        self.radioButtonChannel1.setText(self._translate("MainWindow", "Один (Моно)"))
        self.radioButtonChannel2.setText(self._translate("MainWindow", "Два (Стерео)"))

        # push-buttons column
        self.pushButtonStartRecord.setText(self._translate("MainWindow", "Начать запись"))
        self.pushButtonStopRecord.setText(self._translate("MainWindow", "Остановить запись"))


    #
    # def setupUi(self, MainWindow):
    #     MainWindow.setObjectName("MainWindow")
    #     MainWindow.resize(637, 366)
    #     self.centralwidget = QtWidgets.QWidget(MainWindow)
    #     self.centralwidget.setObjectName("centralwidget")
    #
    #
    #
    #     MainWindow.setCentralWidget(self.centralwidget)
    #     self.menubar = QtWidgets.QMenuBar(MainWindow)
    #     self.menubar.setGeometry(QtCore.QRect(0, 0, 637, 21))
    #     self.menubar.setObjectName("menubar")
    #     MainWindow.setMenuBar(self.menubar)
    #     self.statusbar = QtWidgets.QStatusBar(MainWindow)
    #     self.statusbar.setObjectName("statusbar")
    #     MainWindow.setStatusBar(self.statusbar)
    #
    #     self.retranslateUi(MainWindow)
    #     QtCore.QMetaObject.connectSlotsByName(MainWindow)

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = InitWindow()
    ui.setupUI()
    sys.exit(app.exec_())

# from source.presenter import Presenter
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

import sys


class View(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle("Qt Window example")
        self.initUI()
        self.show()

    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Label")
        self.label.move(50, 50)

        self.button = QtWidgets.QPushButton(self)
        self.button.setText("Start Presenter")
        self.button.clicked.connect(self.clickSignal)

    def clickSignal(self):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = View()
    app.exec_()

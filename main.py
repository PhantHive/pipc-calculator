from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtGui import QFont, QFontDatabase
from PyQt5.QtWidgets import QPushButton, QApplication, QMainWindow, QLabel, QStackedWidget, QHBoxLayout, QVBoxLayout, \
    QWidget, QListWidget, QStackedLayout
import sys

from src.pages.ivPage import IVWindow
from src.pages.ipPage import IPWindow
from src.pages.home import Main


class Pjmat(QMainWindow):
    def __init__(self, parent=None):
        super(Pjmat, self).__init__(parent)

        self.icon = QtGui.QIcon()
        self.icon.addPixmap(QtGui.QPixmap('src/image/bg.jpg'), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.setWindowIcon(self.icon)

        QtGui.QFontDatabase.addApplicationFont('./src/font/simplicity.ttf')

        self.uiMainWindow = Main()
        self.uiIP = IPWindow()
        self.uiIV = IVWindow()
        self.startMainWindow()

    def startMainWindow(self):
        self.uiMainWindow.setupUI(self)
        # Connect buttons to the page (ivPage, ipPage ...)
        self.uiMainWindow.ipBt.clicked.connect(self.startIterPow)
        self.uiMainWindow.ivBt.clicked.connect(self.startInvPow)
        self.show()

    def startIterPow(self):
        self.uiIP.setupUI(self)
        self.uiIP.homeBt.clicked.connect(self.startMainWindow)
        self.show()

    def startInvPow(self):
        self.uiIV.setupUI(self)
        self.uiIV.homeBt.clicked.connect(self.startMainWindow)
        self.show()


if __name__ == '__main__':
    font = QFont('aero')
    app = QApplication(sys.argv)
    app.setStyle('Window')
    app.setStyleSheet(open('src/css/main.qss').read())
    window = Pjmat()
    sys.exit(app.exec_())

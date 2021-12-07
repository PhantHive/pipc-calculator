from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtGui import QFont, QFontDatabase
from PyQt5.QtWidgets import QPushButton, QApplication, QMainWindow, QLabel, QStackedWidget, QHBoxLayout, QVBoxLayout, \
    QWidget, QListWidget, QStackedLayout
import sys


class Main(object):
    def setupUI(self, Main):
        Main.setGeometry(500, 100, 750, 750)
        Main.setFixedSize(750, 750)
        Main.setWindowTitle("MATH PROJECT - IPSA 2021")

        self.mainWidget = QWidget(Main)

        self.label = QLabel(self.mainWidget)
        self.label.setText("MATH PROJECT")
        self.label.move(220, 50)
        self.label.resize(400, 70)

        # Button Iter Power Page
        self.ipBt = QPushButton(self.mainWidget)
        self.ipBt.setText(" ♦   Iterative Power")
        self.ipBt.move(320, 150)
        self.ipBt.resize(120, 55)

        Main.setCentralWidget(self.mainWidget)

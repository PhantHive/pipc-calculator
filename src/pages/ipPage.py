from PyQt5 import QtGui, QtWidgets, QtCore, Qt
from PyQt5.QtGui import QFont, QFontDatabase, QIntValidator
from PyQt5.QtWidgets import QPushButton, QApplication, QMainWindow, QLabel, QStackedWidget, QHBoxLayout, QVBoxLayout, \
    QWidget, QListWidget, QStackedLayout, QLineEdit, QFormLayout
from src.maths.iterPower import IterPower
from src.maths.createMatrix import Matrix
import sys


class IPWindow(object):

    def __init__(self):
        self.onlyInt = QIntValidator()
        self.startCalc = []

    def setupUI(self, IPWindow):
        IPWindow.setGeometry(500, 100, 750, 750)
        IPWindow.setFixedSize(750, 750)
        IPWindow.setWindowTitle("MATH PROJECT - IPSA 2021 \ Iter Power")

        self.IpWidgets = QWidget(IPWindow)

        self.labelIp = QLabel(self.IpWidgets)
        self.labelIp.setText("Iterative Power")
        self.labelIp.move(50, 50)
        self.labelIp.resize(700, 70)

        # Button Home page
        self.homeBt = QPushButton(self.IpWidgets)
        self.homeBt.setText("HOME")
        self.homeBt.move(620, 690)
        self.homeBt.resize(120, 55)

        self.gui()

        IPWindow.setCentralWidget(self.IpWidgets)

    def gui(self):

        # Nitermax
        self.niterMax = QLabel(self.IpWidgets)
        self.niterMax.setText('Nitermax >')
        self.nmaxInput = QLineEdit(self.IpWidgets)

        # Matrix size
        self.msizeInput = QLineEdit(self.IpWidgets)
        self.matrixSize = QLabel(self.IpWidgets)
        self.matrixSize.setText("Matrix size >")

        # Tolerance value
        self.epsInput = QLineEdit(self.IpWidgets)
        self.epsilon = QLabel(self.IpWidgets)
        self.epsilon.setText("Tolerance >")

        self.msizeInput.setValidator(self.onlyInt)
        self.nmaxInput.setValidator(self.onlyInt)
        self.epsInput.setValidator(self.onlyInt)
        self.niterMax.setProperty("type", 1)
        self.matrixSize.setProperty("type", 1)
        self.epsilon.setProperty("type", 1)

        # calculate button
        self.calcul = QPushButton(self.IpWidgets)
        self.calcul.setText("Calculate =>")
        self.calcul.setProperty("type", 1)

        self.inputs = [self.epsInput, self.nmaxInput, self.msizeInput]

        self.move_widgets()
        self.calcul.clicked.connect(self.calculate)

    def move_widgets(self):

        self.nmaxInput.move(155, 200)
        self.nmaxInput.resize(150, 25)
        self.niterMax.move(30, 200)

        self.msizeInput.move(155, 270)
        self.msizeInput.resize(150, 25)
        self.matrixSize.move(30, 270)

        self.epsInput.move(155, 340)
        self.epsInput.resize(150, 25)
        self.epsilon.move(30, 340)

        self.calcul.move(340, 260)
        self.calcul.resize(85, 45)

    def calculate(self):

        for entry in self.inputs:

            if entry.text() == "":
                entry.setPlaceholderText("Insert an integer")
                self.startCalc.append(False)

        if False in self.startCalc:
            self.startCalc.clear()
            return
        else:
            # Calculate with iterPower.py in maths package
            msize = int(self.msizeInput.text())
            nmax = int(self.nmaxInput.text())
            eps = 10**(-int(self.epsInput.text()))

            cMatrix = Matrix(msize, True)
            matA = cMatrix.getMatrix()

            iP = IterPower(matA, eps, nmax)
            last_diff, nbIter = iP.iter()
            print(last_diff, nbIter)




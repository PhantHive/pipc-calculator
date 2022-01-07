from decimal import Decimal

import numpy as np
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QPushButton, QLabel, QWidget, QLineEdit, QComboBox
from src.maths.invPower import InvPower
from src.maths.createMatrix import Matrix
from src.maths.src.iterative import Iter

from src.maths.src.norm import Norm
from src.canvas.Canvas import Canvas


class IVWindow(object):

    def __init__(self):

        self.onlyInt = QIntValidator()
        self.startCalc = []
        self.inputs = []
        self.choice = "Random"
        self.method = "Directe"

    def setupUI(self, IVWindow):
        IVWindow.setGeometry(500, 100, 1200, 780)
        IVWindow.setFixedSize(1200, 780)
        IVWindow.setWindowTitle("MATH PROJECT - IPSA 2021 \ Puissance Itérée Inverse")

        self.IVWidgets = QWidget(IVWindow)

        self.labelIV = QLabel(self.IVWidgets)
        self.labelIV.setText("Puissance Itérée Inverse")
        self.labelIV.move(50, 50)
        self.labelIV.resize(700, 70)

        self.canvas = Canvas(self.IVWidgets)
        self.canvas.resize(475, 275)
        self.canvas.move(370, 500)

        # Button Home page
        self.homeBt = QPushButton(self.IVWidgets)
        self.homeBt.setText("MENU")
        self.homeBt.move(1060, 720)
        self.homeBt.resize(130, 55)
        self.homeBt.setProperty("type", 1)

        self.entry_widgets()
        self.result_widgets()
        self.move_widgets()

        IVWindow.setCentralWidget(self.IVWidgets)

    def hide_mat(self, n):

        if n == 1:
            for mat in self.matrix:
                mat.hide()
                mat.clear()
            self.msizeInput.show()
            self.matrixSize.show()
        else:
            self.msizeInput.hide()
            self.matrixSize.hide()
            self.msizeInput.clear()
            for mat in self.matrix:
                mat.show()

    def new_ui(self, text):
        if text == "Random":
            self.hide_mat(1)
            self.choice = "Random"
        else:
            self.hide_mat(0)
            self.choice = "Custom"

    def setMethod(self, text):
        self.method = text

    def entry_widgets(self):

        self.matChoice = QComboBox(self.IVWidgets)
        self.matChoice.addItem("Random")
        self.matChoice.addItem("Custom")
        self.matChoice.activated[str].connect(self.new_ui)

        # Method choice
        self.methode = QComboBox(self.IVWidgets)
        self.methode.addItem("Directe")
        self.methode.addItem("QR")
        self.methode.addItem("LU")
        self.methode.activated[str].connect(self.setMethod)

        # Nitermax
        self.niterMax = QLabel(self.IVWidgets)
        self.niterMax.setText('Nitermax>')
        self.nmaxInput = QLineEdit(self.IVWidgets)

        # Tolerance value
        self.epsInput = QLineEdit(self.IVWidgets)
        self.epsilon = QLabel(self.IVWidgets)
        self.epsilon.setText("Tolerance>")

        self.nmaxInput.setValidator(self.onlyInt)
        self.epsInput.setValidator(self.onlyInt)
        self.niterMax.setProperty("type", 1)
        self.epsilon.setProperty("type", 1)

        self.inputs.append(self.nmaxInput)
        self.inputs.append(self.epsInput)

        # custom matrix
        self.custMatrix = QLabel(self.IVWidgets)
        self.custMatrix.setText("Matrice> ")
        self.custMatrix.setProperty("type", 1)

        # method label
        self.custMethod = QLabel(self.IVWidgets)
        self.custMethod.setText("Méthode> ")
        self.custMethod.setProperty("type", 1)

        # Matrix size
        self.msizeInput = QLineEdit(self.IVWidgets)
        self.matrixSize = QLabel(self.IVWidgets)
        self.matrixSize.setText("Taille (n, n)>")
        self.msizeInput.setValidator(self.onlyInt)
        self.matrixSize.setProperty("type", 1)

        self.matA = QLineEdit(self.IVWidgets)
        self.matB = QLineEdit(self.IVWidgets)
        self.matC = QLineEdit(self.IVWidgets)
        self.matD = QLineEdit(self.IVWidgets)
        self.matE = QLineEdit(self.IVWidgets)
        self.matF = QLineEdit(self.IVWidgets)
        self.matG = QLineEdit(self.IVWidgets)
        self.matH = QLineEdit(self.IVWidgets)
        self.matI = QLineEdit(self.IVWidgets)

        self.matrix = [self.matA, self.matB, self.matC, self.matD, self.matE,
                       self.matF, self.matG, self.matH, self.matI]

        for mat in self.matrix:
            mat.setValidator(self.onlyInt)

        # calculate button
        self.calcul = QPushButton(self.IVWidgets)
        self.calcul.setText("Calculer =>")
        self.calcul.setProperty("type", 1)

        self.calcul.clicked.connect(self.calculate)

    def result_widgets(self):
        # Result
        self.nbiter = QLabel(self.IVWidgets)
        self.nbiter.setText('*Nombre d\'itération*')
        self.nbiter.setProperty("type", 2)

        self.lastdiff = QLabel(self.IVWidgets)
        self.lastdiff.setText('*Dernier écart*')
        self.lastdiff.setProperty("type", 2)

        self.eigvals = QLabel(self.IVWidgets)
        self.eigvals.setText('*Valeur Propre Min*')
        self.eigvals.setProperty("type", 2)

        self.valnorm = QLabel(self.IVWidgets)
        self.valnorm.setText('*Norme*')
        self.valnorm.setProperty("type", 2)

        self.cond = QLabel(self.IVWidgets)
        self.cond.setText('*Conditionnement*')
        self.cond.setProperty("type", 2)

        self.eigvec = QLabel(self.IVWidgets)
        self.eigvec.setText('*Approximation de Vecteur Propre*')
        self.eigvec.setProperty("type", 2)

    def move_widgets(self):

        self.nmaxInput.move(155, 200)
        self.nmaxInput.resize(150, 25)
        self.niterMax.move(30, 200)

        self.custMatrix.move(30, 270)
        self.matChoice.move(155, 270)
        self.matChoice.resize(150, 25)

        self.methode.move(155, 340)
        self.methode.resize(150, 25)
        self.custMethod.move(30, 340)

        self.epsInput.move(155, 410)
        self.epsInput.resize(150, 25)
        self.epsilon.move(30, 410)

        self.calcul.move(360, 260)
        self.calcul.resize(85, 45)

        self.valnorm.move(485, 150)
        self.valnorm.resize(250, 50)

        # result widgets
        self.nbiter.move(485, 220)
        self.nbiter.resize(250, 50)
        self.lastdiff.move(485, 290)
        self.lastdiff.resize(250, 50)

        self.eigvals.move(485, 360)
        self.eigvals.resize(250, 50)

        self.cond.move(485, 430)
        self.cond.resize(250, 50)

        self.eigvec.move(800, 180)
        self.eigvec.resize(350, 100)

        self.matA.move(180, 470)
        self.matB.move(215, 470)
        self.matC.move(250, 470)

        self.matD.move(180, 505)
        self.matE.move(215, 505)
        self.matF.move(250, 505)

        self.matG.move(180, 540)
        self.matH.move(215, 540)
        self.matI.move(250, 540)

        self.msizeInput.move(155, 480)
        self.msizeInput.resize(150, 25)
        self.matrixSize.move(30, 480)



        for mat in self.matrix:
            mat.resize(30, 30)

        self.hide_mat(1)

    def calculate(self):

        if self.nmaxInput.text() != "":

            if int(self.nmaxInput.text()) < 5:
                self.nmaxInput.clear()
                self.nmaxInput.setPlaceholderText("> 5")
                self.startCalc.append(False)

        else:
            for entry in self.inputs:
                if entry.text() == "":
                    entry.setPlaceholderText("Insert an integer")
                    self.nbiter.setText('*Nombre d\'itération*')
                    self.lastdiff.setText('*Dernier écart*')
                    self.startCalc.append(False)

        if self.choice == "Random":
            if self.msizeInput.text() == "":
                self.msizeInput.setPlaceholderText("Insert an integer")
                self.startCalc.append(False)
            elif int(self.msizeInput.text()) > 1000:
                self.msizeInput.clear()
                self.msizeInput.setPlaceholderText("< 1001")
                self.startCalc.append(False)
        else:
            for mat in self.matrix:
                if mat.text() == "":
                    mat.setPlaceholderText("X")
                    self.startCalc.append(False)

        if False in self.startCalc:
            self.startCalc.clear()
            return
        else:
            # Calculate with iterPower.py in maths package
            nmax = int(self.nmaxInput.text())
            eps = 10 ** (-int(self.epsInput.text()))

            if self.msizeInput.text() != "":
                msize = int(self.msizeInput.text())
                cMatrix = Matrix(msize, True)
                matA = cMatrix.getMatrix()
            else:
                self.mat_inputs = [[int(self.matA.text()), int(self.matB.text()), int(self.matC.text())],
                                   [int(self.matD.text()), int(self.matE.text()), int(self.matF.text())],
                                   [int(self.matG.text()), int(self.matH.text()), int(self.matI.text())]]
                matA = np.array(self.mat_inputs)

            print(matA)
            IV = Iter(matA, eps, nmax, "inverse", self.method)
            last_diff, nbIter = IV.iter()

            # Conditionement
            IP = Iter(matA, eps, nmax, "iterative", self.method)
            IP.iter()

            last_diff = "{:.5e}".format(Decimal(last_diff)).replace(".", ",")

            self.eigvals.resize(250, 100)
            self.eigvec.resize(450, 300)
            vals, vecs = IV.eigvals()
            v_min = vals

            val = "{:.2f}".format(Decimal(vals)).replace(".", ",")
            eigvals_txt = f"Valeur Propre Min: \n {val} \n"

            vals_max, vec_max = IP.eigvals()
            v_max = vals_max

            if len(vecs) > 7:
                vec_txt = "Approximation de Vecteur Propre: \n\n Trop grand pour être affiché"
            else:
                vecs = vecs.tolist()
                vec_txt = f"Approximation de Vecteur Propre:\n"
                for i in range(len(vecs)):
                    vec_txt += "\n"
                    vecs[i] = "{:.5f}".format(Decimal(vecs[i])).replace(".", ",")
                    vec_txt += f"{vecs[i]}   "

            # Calculate the matrix norm:
            calc_norm = Norm(matA)
            norm = calc_norm.mat_norm()
            norm = "{:.5f}".format(Decimal(norm)).replace(".", ",")

            self.valnorm.setText(f"Norme = {norm}")
            self.eigvec.setText(vec_txt)
            self.nbiter.setText(f"Nb iter = {nbIter}")
            self.lastdiff.setText(f"Ecart = {last_diff}")
            self.eigvals.setText(eigvals_txt)

            # Calculate cond
            cond, cond_np = IV.get_cond(v_max, v_min)
            print("Cond = ", cond, cond_np)
            cond = "{:.2f}".format(Decimal(cond)).replace(".", ",")
            self.cond.setText(f"Cond = {cond}")

            iter_list, proc_list = IV.get_datas()
            self.canvas.plot(iter_list, proc_list)
            self.canvas.draw()

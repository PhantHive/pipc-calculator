import numpy as np


class Matrix:

    def __init__(self, n, positif):
        self.n = n
        self.positif = positif
        self.matA = None

        self.matA = self.setMatrix()
        while np.linalg.det(self.matA) == 0:
            self.setMatrix()

    def setMatrix(self):
        self.matA = np.random.random_integers(0, 1000, size=(self.n, self.n))
        A = None
        if self.positif:
            A = (self.matA + self.matA.T) / 2
        self.matA = A
        return self.matA

    def getMatrix(self):
        print(self.matA)
        return self.matA

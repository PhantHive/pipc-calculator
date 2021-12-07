import numpy as np


class Matrix:

    def __init__(self, n, positif):
        self.n = n
        self.positif = positif
        self.matA = np.random.randint(0, 1000, size=(n, n))
        print(self.matA)
        if self.positif:
            A = (self.matA + self.matA.T) / 2
            self.matA = A

    def getMatrix(self):
        print(self.matA)
        return self.matA

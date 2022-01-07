import numpy as np
import scipy.linalg


class Decomp:

    def __init__(self, matA):
        self.matA = matA
        self.matX = None
        self.matY = None

    def decomp_qr(self):
        self.X, self.Y = np.linalg.qr(self.matA)
        return self.X, self.Y

    def decomp_lu(self):
        P, self.matX, self.matY = scipy.linalg.lu(self.matA)
        return self.matX, self.matY



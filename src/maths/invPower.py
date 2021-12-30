import time
import numpy as np
from src.maths.src.decomp import Decomp


class InvPower(object):

    def __init__(self, A, eps, nmax, method):
        self.A = A
        self.eps = eps
        self.nmax = nmax
        self.method = method

        self.w = None
        self.c = None
        self.old_w = None
        # generate x vector
        self.x = np.random.random(len(self.A))
        self.diff = None
        self.verif = False
        self.vp = None
        self.proc_time = []
        self.iter_list = []

        print(self.method)

    def w_sequence(self, k):
        w = (np.linalg.inv(np.linalg.matrix_power(self.A, k)) @ self.x) / (
            np.linalg.norm(np.linalg.inv((np.linalg.matrix_power(self.A, k))) @ self.x))
        return w

    def c_sequence(self, w):
        mat_X, mat_Y = None, None

        if self.method == "Directe":
            c = np.linalg.inv(self.A) @ w
        else:
            met = Decomp(self.A)

            if self.method == "QR":
                mat_X, mat_Y = met.decomp_qr()
            elif self.method == "LU":
                mat_X, mat_Y = met.decomp_lu()

            y_int = np.linalg.solve(mat_X, w)
            c = np.linalg.solve(mat_Y, y_int)

        return c

    def eigvals(self):
        '''vals, vec = np.linalg.eig(self.A)
        print(vals, vec)'''
        return self.vp, self.c

    def get_datas(self):
        return self.iter_list, self.proc_time

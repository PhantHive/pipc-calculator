import time
import numpy as np
import numpy.linalg

from src.maths.src.decomp import Decomp


class InvPower(object):
    '''
    This method use a c_sequence, a w_sequence and a choosen decomposition method.
    Used to get an approximation of the min eigen value and eigen vector.
    '''

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

    def w_sequence(self, k):

        try:
            w = ((np.linalg.matrix_power(np.linalg.inv(self.A), k)) @ self.x) / (
                np.linalg.norm((np.linalg.matrix_power(np.linalg.inv(self.A), k)) @ self.x))
        except numpy.linalg.LinAlgError:
            w = ((np.linalg.matrix_power(np.linalg.pinv(self.A), k)) @ self.x) / (
                np.linalg.norm((np.linalg.matrix_power(np.linalg.pinv(self.A), k)) @ self.x))

        return w

    def c_sequence(self, w):
        mat_X, mat_Y = None, None

        if self.method == "Directe":
            try:
                c = np.linalg.inv(self.A) @ w
            except numpy.linalg.LinAlgError:
                print("erreur!")
                c = np.linalg.pinv(self.A) @ w
        else:
            met = Decomp(self.A)

            if self.method == "QR":
                mat_X, mat_Y = met.decomp_qr()
            elif self.method == "LU":
                mat_X, mat_Y = met.decomp_lu()

            try:
                y_int = np.linalg.solve(mat_X, w)
                c = np.linalg.solve(mat_Y, y_int)
            except numpy.linalg.LinAlgError:
                pass

        return c

    def eigvals(self):
        vals, vec = np.linalg.eig(self.A)
        print(vec)
        # print(vals, vec)
        return self.vp, self.w

    def get_datas(self):
        return self.iter_list, self.proc_time

    def get_cond(self, vp_max, vp_min):
        cond = vp_max / vp_min
        cond_np = numpy.linalg.cond(self.A)
        return cond, cond_np




import numpy as np


class InvPower:

    def __init__(self, A, eps, nmax):
        self.A = A
        self.eps = eps
        self.nmax = nmax

        self.w = None
        self.c = None
        self.old_w = None
        # generate x vector
        self.x = np.random.random(len(self.A))
        self.diff = None
        self.verif = False
        self.vp = None

    def w_sequence(self, k):
        w = (np.linalg.matrix_power(self.A, k) @ self.x) / (
            np.linalg.norm((np.linalg.matrix_power(self.A, k)) @ self.x))
        return w

    def c_sequence(self, w):
        c = np.linalg.inv(self.A) @ w
        return c

    def iter(self):

        for k in range(1, self.nmax):
            print("k=", k)
            self.w = self.w_sequence(k)
            print(self.w, self.old_w)
            if self.old_w is not None:

                self.diff = np.linalg.norm(self.w - self.old_w)
                print(self.diff)
                if self.diff <= self.eps:
                    self.verif = True
                else:
                    self.verif = False
            else:
                self.verif = False

            if self.verif:

                return self.diff, k

            else:
                self.old_w = self.w
                self.c = self.c_sequence(self.w)
                self.vp = np.linalg.norm(self.c)

        self.verif = False
        return self.diff, (self.nmax - 1)

    def eigvals(self):
        vals, vec = np.linalg.eig(self.A)
        print(vals, vec)
        return self.vp, self.c

import numpy as np


class IterPower:

    def __init__(self, A, eps, nmax):
        self.A = A
        self.eps = eps
        self.nmax = nmax
        self.w = None
        self.old_w = None
        # generate x vector
        self.x = np.random.random(len(self.A))
        self.diff = None
        self.verif = False

    def w_sequence(self, k):
        w = (self.A ** k) * self.x / (np.linalg.norm((self.A ** k) * self.x))
        return w

    def c_sequence(self, w):
        c = self.A * w
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
                c = self.c_sequence(self.w)

        self.verif = False
        return self.diff, self.nmax

    def eigvals(self):
        vals, vec = np.linalg.eig(self.A)
        return vals, vec

'''if __name__ == '__main__':
    n = 3
    a = np.random.randint(0, 1000, size=(n, n))
    matA = (a + a.T) / 2
    print(matA)
    iP = IterPower(matA, 10, 100)
    last_diff, nbIter = iP.iter()
    print(last_diff, nbIter)'''

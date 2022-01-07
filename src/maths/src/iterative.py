import time
import numpy as np
from src.maths.invPower import InvPower
from src.maths.iterPower import IterPower


class Iter(InvPower, IterPower):
    '''
    Global iterative class for both Inverse and "classic" iterative Power
    '''

    def __init__(self, A, eps, nmax, choice, method=None):
        '''
        :param w: w^(k+1)
        :param old_w: w^k
        :param A:
        :param eps:
        :param nmax:
        :param choice:
        :param method:
        '''
        super(Iter, self).__init__(A, eps, nmax, method)
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
        self.choice = choice

    def iter(self):

        start = time.time()
        for k in range(1, self.nmax):
            # print("k=", k)
            self.iter_list.append(k)
            if self.choice == "inverse":
                self.w = InvPower.w_sequence(self, k)
            else:
                self.w = IterPower.w_sequence(self, k)

            # print(self.w, self.old_w)
            if self.old_w is not None:

                self.diff = np.linalg.norm(self.w - self.old_w)
                # print(self.diff)
                if self.diff <= self.eps:
                    self.verif = True
                else:
                    self.verif = False
            else:
                self.verif = False

            if self.verif:
                stop = time.time()
                self.proc_time.append(stop - start)
                return self.diff, k

            else:
                self.old_w = self.w
                if self.choice == "inverse":
                    self.c = InvPower.c_sequence(self, self.w)
                    self.vp = 1 / np.linalg.norm(self.c)  # eigen value

                else:
                    self.c = IterPower.c_sequence(self, self.w)
                    self.vp = np.linalg.norm(self.c)

                stop = time.time()
                self.proc_time.append(stop - start)

        self.verif = False
        return self.diff, (self.nmax - 1)

import math

import numpy as np
from sympy import limit, oo
from src.maths.src.iterative import Iter


class Conv:
    '''
    Check if a squence is convergent using limit and
    the maximum eigen value returned by the iterative Power function.
    '''

    def __init__(self, A, w, k, vp):
        self.A = A
        self.w = w
        self.k = k
        self.vp = vp
        self.conv = False
        self.lim = None

    def convergent(self, choice):
        '''
        w^k et testé avec -1^k * w^k
        '''
        if choice == 1:
            t = ((-1) ** self.k)
            result = "La suite (-1)^k * wk est convergente"
            result_2 = "La suite (-1)^k * wk n'est pas convergente"
        else:
            t = 1
            result = "La suite wk est convergente"
            result_2 = "La suite wk n'est pas convergente"

        f = (self.A @ (t * self.w)) / self.w
        self.lim = limit(f, self.k + 1, oo)

        if (max(self.lim) - math.ceil(self.vp)) < 0.3:
            print(result)
            self.conv = True
        else:
            print(result_2)

    def diff_numpy(self):
        vals, vec = np.linalg.eig(self.A)
        return max(vals) - self.vp

    def get_result(self):
        return self.conv, max(self.lim), self.vp


if __name__ == '__main__':
    A = np.array([[0, 1], [1, 0]])
    IP = Iter(A, 10, 10, "iterative")
    last_diff, nbIter = IP.iter()
    val, vec = IP.eigvals()
    print(A)
    conv = Conv(A, vec, nbIter, np.abs(val))
    conv.convergent(2)

    diff = conv.diff_numpy()
    print("Ecart entre la valeur propre de numpy et celle de l'algo:", diff)

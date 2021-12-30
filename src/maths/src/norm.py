import math

import numpy as np


class Norm:

    def __init__(self, A):
        self.A = A
        self.Tr_A = []
        self.trace = 0
        self.norm = None
        self.calc_norm()

    def transpose(self):
        new_row = []
        for i in range(self.A.shape[1]):
            for j in range(self.A.shape[0]):
                new_row.append(self.A[j, i])

            self.Tr_A.append(new_row)
            new_row = []

        self.Tr_A = np.array(self.Tr_A)
        return self.Tr_A

    def mat_trace(self, mat):
        i = 0
        for row in mat:
            self.trace += row[i]
            i += 1

        return self.trace

    def calc_norm(self):

        self.Tr_A = self.transpose()
        mat_temp = self.Tr_A @ self.A

        self.trace = self.mat_trace(mat_temp)
        self.norm = math.sqrt(self.trace)
        return self.norm

    def mat_norm(self):
        return self.norm

'''
if __name__ == '__main__':
    A = np.array([[1, 1, 3], [1, 3, 1], [1, 1, 3]])
    norm = Norm(A)
'''


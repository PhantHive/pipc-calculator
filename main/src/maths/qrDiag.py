import numpy as np
from src.maths.src.decomp import Decomp


class QRDIAG:
    def __init__(self, A, nmax, eps):
        self.A = A
        self.Q = None
        self.R = None
        self.P = None

        self.Ak = None
        self.Akp = None
        self.Mk = None
        self.nbIter = 0
        self.eps = eps
        self.nmax = nmax
        self.verif = True
        self.decomp = Decomp(self.A)

    def diag(self):
        k = 0
        n, p = np.shape(self.A)
        eigvals = []

        while (self.nbIter < self.nmax) & self.verif:
            self.nbIter += 1
            if k == 0:
                self.Ak = self.A
            else:
                self.Ak = self.Akp

            self.Q, self.R = self.decomp.decomp_qr()
            self.Akp = self.R @ self.Q
            self.P = ((np.transpose(self.Q) @ self.Ak) @ self.Q)

            mk_list = []
            for i in range(n):
                for j in range(n):
                    if j < i:
                        mk_list.append(np.abs(self.Ak[i, j]))
                        if np.abs(self.Ak[i, j]) <= self.eps:
                            self.verif = False

            self.Mk = max(mk_list)

            k += 1

        for i in range(n):
            eigvals.append(self.Ak[i, i])

        return self.Ak, self.P, k, self.Mk, eigvals

    def eigvals_numpy(self):
        return np.linalg.eig(self.A)



if __name__ == '__main__':

    A = np.array([[3, 1, 1], [1, 3, 1], [1, 1, 3]])
    qrdiag = QRDIAG(A, nmax=100, eps=10 ** (-10))
    print("A =", A)

    Ak, P, nbnbIter, Mk, eigvals = qrdiag.diag()
    vals_numpy = qrdiag.eigvals_numpy()

    print(f"Résultat obtenue pour la matrice: \n{A}\n\n"
          f"Dernière matrice A^k: \n{Ak}\n\n"
          f"Nombre d'itérations: {nbnbIter}\n\n"
          f"Matrice de passage P: \n{P}\n\n"
          f"Valeur maximale Mk: {Mk}\n\n"
          f"Approximation des valeurs propres: \n{eigvals}\n\n"
          f"Valeurs propres avec Numpy: \n{list(vals_numpy[0])}\n\n")


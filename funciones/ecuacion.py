import numpy as np

class Ecuacion():
    def resolver(self, primer_termino, segundo_termino):
        self.primer_termino = np.array(primer_termino)
        self.segundo_termino = np.array(segundo_termino)

        solucion = np.linalg.solve(self.primer_termino, self.segundo_termino)


        return solucion
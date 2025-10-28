import numpy as np
from cifrado import *
from crear_array import *


class App():
    def abrir_document(self, matriz, archivo, condicional):
        self.archivo = archivo
        self.matriz = matriz
        self.condicional = condicional
        
        array = []
        array_valores_x = []
        array_valores_y = []

        resultado = []

        matriz_original = np.array(self.matriz)

        with open(self.archivo, "r") as f:
            for line in f:
        
                valores_Array = [float(x) for x in line.strip().split()]

                array = np.array(valores_Array).reshape(-1, 1)

                cir = Cifrado()
                create = crear_array()

                if self.condicional == "cifrar":
                    resultado = cir.cifrar(array, matriz_original)

                elif self.condicional == "decifrar":
                    resultado = cir.decifrar(matriz_original, array)
        
                valores_x = create.valores_x(resultado)
                valores_y = create.valores_y(resultado)

                array_valores_x.append(valores_x)
                array_valores_y.append(valores_y)

        return array_valores_x, array_valores_y
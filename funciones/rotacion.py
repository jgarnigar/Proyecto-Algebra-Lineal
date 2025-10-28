import numpy as np

class Rotacion():
    def rotar_matriz(self, valores_x, valores_y):
        self.valores_x = valores_x
        self.valores_y = valores_y
        angulo = 135
        angulo_rad = np.deg2rad(angulo)

        rotacion_x = []
        rotacion_y = []

        matriz_rotacion = np.array([
            [np.cos(angulo_rad), -np.sin(angulo_rad)],
            [np.sin(angulo_rad), np.cos(angulo_rad)]
        ])

        for x, y in zip(self.valores_x, self.valores_y):
            new_array = np.array([x, y]).reshape(2,1)
            array_rotado = matriz_rotacion @ new_array
            rotacion_x.append(array_rotado[0,0])
            rotacion_y.append(array_rotado[1,0])

        return rotacion_x, rotacion_y
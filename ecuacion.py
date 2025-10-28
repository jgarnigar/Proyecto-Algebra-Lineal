from clases import *

primer_termino = np.array([
    [6, 7, -1, -12, 14, 5, -12, -3, 9, -5],
    [2, -15, 8, 6, -7, 9, -9, 5, -8, -6],
    [-25, 10, 0, -9, -12, 14, -6, 8, -13, 4],
    [6, -3, 5, -16, 1, 9, -7, 3, -4, 5],
    [8, -9, 6, -1, -1, -5, 7, 0, 3, 2,],
    [-5, 6, 9, -2, 10, -14, 3, 5, -12, 6],
    [-4, 5, 8, -2, 9, -8, 4, 1, 0, -2],
    [1, 1, 2, -3, 4, -1, -4, -7, 2, -4],
    [10, 5, -9, 6, 1, 1, 7, -8, 3, 11],
    [-2, 4, 3, 5, -10, -1, 3, -1, -7, 1]
], dtype=int)

segundo_termino = np.array([48, 64, -132, -75, -16, -408, -203, 59, 126, 2], dtype=int)

ecuacion = Ecuacion()

matriz = ecuacion.resolver(primer_termino, segundo_termino)

print(matriz)


# la matriz da los resultados tales que.
# (2,−2,−3,5,−9,4,−7,−10,11,0)

matriz_codificacion = np.array([
    [ 2,  3, -2,  5, -3,  8],
    [ 6,  5,  0, -9,  7,  4],
    [-7,  8,-10,  1, 11,  7],
    [11,  0,  8,  8, 12, -6],
    [10, -1,  4, -5, -12,  3],
    [ 4,  6,  2, -4,  9, -1]
], dtype=int)


#valores utilizados para la comprobación de las funciones
matriz = np.array([
    [1, 7, 1, 6, 0, 2],
    [2, 8, 2, 0, -1, 9],
    [3, 9, 4, 2, 5, 1],
    [4, 1, 8, 6, 5, -3],
    [5, 2, 5, 7, 4, 2],
    [6, 3, 6, 7, 4, 1]
])


valores = [
    [2],
    [2],
    [2.5],
    [2],
    [3],
    [2]
]
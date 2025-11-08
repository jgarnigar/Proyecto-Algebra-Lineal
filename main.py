import numpy as np
from clases import *
from funciones import *

matriz_codificacion = np.array([
    [ 2,  3, -2,  5, -3,  8],
    [ 6,  5,  0, -9,  7,  4],
    [-7,  8,-10,  1, 11,  7],
    [11,  0,  8,  8, 12, -6],
    [10, -1,  4, -5, -12,  3],
    [ 4,  6,  2, -4,  9, -1]
], dtype=int)


aplicacion = App()
rotar = Rotacion()
desempaquetador = Desempaquetar_Array()
graficar = Graficar()
traslacion = Traslacion()
guardar_datos = GuardarDatos()
cir = Cifrado()
create = crear_array()

inversa = cir.inversa(matriz_codificacion)

def main():
    try: 
        valores_x, valores_y = aplicacion.abrir_document(matriz_codificacion, "datos/datos encriptados.txt", "descifrar")
        desempaquetar_x, desempaquetar_y = desempaquetador.desempaquetar(valores_x, valores_y)

        valores_rotados_x, valores_rotados_y = rotar.rotar_matriz(desempaquetar_x, desempaquetar_y)

        valores_trasladados_x, valores_trasladados_y = traslacion.trasladar_matriz(valores_rotados_x, valores_rotados_y, 20, 30)

        graficar.graficadora(desempaquetar_x, desempaquetar_y)
        graficar.graficadora(valores_rotados_x, valores_rotados_y)
        graficar.graficadora(valores_trasladados_x, valores_trasladados_y)


        guardar_datos.save(desempaquetar_x, desempaquetar_y, "datos/valores desencriptados.txt")
        guardar_datos.save(valores_rotados_x, valores_rotados_y, "datos/valores rotados.txt")
        guardar_datos.save(valores_trasladados_x,valores_trasladados_y,"datos/valores trasladados.txt")

        return True
    except Exception as e:
        print(f"Error encontrado: {e}")


if __name__ == "__main__":
    main()
    
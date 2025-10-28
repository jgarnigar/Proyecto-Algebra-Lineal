import numpy as np
import matplotlib.pyplot as plt


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

class Cifrado():

    def inversa(self, matriz_codificar):
        self.matriz_codificar = matriz_codificar

        matriz_inversa = np.linalg.inv(self.matriz_codificar)

        return matriz_inversa
    
    def cifrar(self, matriz, matriz_codificar):
        self.matriz = matriz
        self.matriz_codificar = matriz_codificar
        matriz_cifrada = self.matriz_codificar @ self.matriz

        return matriz_cifrada
    
    def decifrar(self, matriz_codificacion, matriz_resolver):
        self.matriz_codificacion = matriz_codificacion
        self.matriz_resolver = matriz_resolver

        matriz_inversa = np.linalg.inv(self.matriz_codificacion)

        matriz_decifrada = matriz_inversa @ self.matriz_resolver

        return matriz_decifrada


class crear_array():

    def valores_x(self, array):
        self.array = array
        puntos_x = []
        contador = 1
        for x in self.array:
            if contador % 2 != 0:
                puntos_x.append(x)

            contador += 1

        return puntos_x
    
    def valores_y(self, array):
        self.array = array
        puntos_y = []
        contador = 1

        for y in self.array:
            if contador % 2 == 0:
                puntos_y.append(y)

            contador +=1
        
        return puntos_y


class Ecuacion():
    def resolver(self, primer_termino, segundo_termino):
        self.primer_termino = np.array(primer_termino)
        self.segundo_termino = np.array(segundo_termino)

        solucion = np.linalg.solve(self.primer_termino, self.segundo_termino)


        return solucion

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
    
class Desempaquetar_Array():
    def desempaquetar(self, valores_x, valores_y):
        self.valores_x = valores_x
        self.valores_y = valores_y

        new_values_x = []
        new_values_y = []

        for nueva_lista in self.valores_x:
            for x in np.ravel(nueva_lista):
                new_values_x.append(x)

        for nueva_lista in self.valores_y:
            for y in np.ravel(nueva_lista):
                new_values_y.append(y)

        return new_values_x, new_values_y
    
class Graficar():
    def graficadora(self, x, y):
        self.x = x
        self.y = y

        plt.scatter(self.x, self.y, color='blue', marker='o', label='Puntos (x, y)')
        # Personalizar el gráfico
        plt.title("Gráfico de puntos")
        plt.xlabel("Eje X")
        plt.ylabel("Eje Y")
        plt.legend()
        plt.grid(True)

        # Mostrar el gráfico
        plt.show()

class Traslacion():
    def trasladar_matriz(self, x, y, a, b):
        self.x = x
        self.y = y
        # a = movimiento en x
        self.a = a
        # b = mobimiento en y
        self.b = b

        valores_x = []
        valores_y = []

        matriz_traslacion = np.array([
            [1, 0, self.a],
            [0, 1, self.b],
            [0, 0, 1]
        ])

        for punto_x, punto_y in zip(self.x, self.y):
            punto = np.array([punto_x, punto_y, 1]).reshape(3,1)

            resultado = matriz_traslacion @ punto

            valores_x.append(resultado[0,0])
            valores_y.append(resultado[1,0])

        return valores_x, valores_y
    

class GuardarDatos():
    def save(self, valores_x, valores_y, nombre_archivo):
        self.valores_x = valores_x
        self.valores_y = valores_y
        self.nombre_archivo = nombre_archivo

        with open(self.nombre_archivo, "w") as f:
            for x, y in zip(valores_x, valores_y):
                f.write(f"({x}, {y})\n")
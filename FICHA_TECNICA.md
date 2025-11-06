<h1 align="center">📊 FICHA TÉCNICA - Proyecto Álgebra Lineal.</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python Badge"/>
  <img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy Badge"/>
  <img src="https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge&logo=plotly&logoColor=white" alt="Matplotlib Badge"/>
</p>

<p align="center">
  <img src="https://img.icons8.com/color/96/000000/python.png" alt="Python Icon" height="70"/>
  <img src="https://img.icons8.com/color/96/000000/numpy.png" alt="NumPy Icon" height="70"/>
  <img src="https://upload.wikimedia.org/wikipedia/commons/8/84/Matplotlib_icon.svg" alt="Matplotlib Icon" height="70"/>
</p>

<p align="center">
  <a href="https://github.com/jgarnigar/Proyecto-Algebra-Lineal/tree/master">
    <img src="https://img.shields.io/badge/GitHub-jgarnigar-181717?style=for-the-badge&logo=github" alt="GitHub Badge">
  </a>
</p>

## 🔍**Descripción**
- Los datos fueron encriptados multiplicando una matriz 6x6 por una matriz 6x1. El resultado es una matriz 6x1 con los datos encriptados. Estos datos nuevos ocultan una imagen. La nueva matriz 6x1 nos da los valores (x,y).

- Para desencriptar estos datos, obtendremos la matriz inversa de la matriz 6x6 y multiplicaremos por la 6x1 con los datos encriptados.

- Finalmente usaremos matplotlib con el fin de visualizar los datos desencriptados.

## ⚙️ **Instalación y requisitos.**
Utilizaremos **Python** 3.10 o superior, **Numpy** y **Matplotlib**. Para asegurarnos que todo funcione, por favor cree un entorno virtual.

***Instalar Python 3.10 o superior***

[Descargar Python](https://www.python.org/downloads/)

🖥️ ***Clone el repositorio:***

    git clone https://github.com/jgarnigar/Proyecto-Algebra-Lineal.git


⌨️ ***Crear el entorno virtual***
```bash
python -m venv venv
source venv/bin/activate     # Para Linux/Mac
venv\Scripts\activate        # Para Windows
```

💻 ***Instale los requerimientos***

    pip install -r requirements.txt

    
🚀 ***Ejecución del programa***

Una vez tengamos el repositorio clonado y todos los requisitos instalados, ejecute este código desde la carpeta principal:

    `python main.py`

> ⚠️ **Nota:** asegúrese de ejecutar este comando desde la carpeta raíz del proyecto!


## 🎯 **Objetivo**

- El objetivo es crear un algoritmo a través de Python y Numpy para poder desencriptar estos datos de forma automatizada y por último mostrar estos datos con Matplotlib.

## 🗂️ **Estructura**

📂 Proyecto Álgebra Lineal

 ┣ 📁 datos/          → Datos encriptados y desencriptados

 ┣ 📁 funciones/       → Funciones lógicas

 ┣ 📄 main.py        → Archivo principal de ejecución

 ┣ 📄 requirements.txt

 ┗ 📄 README.md



## 🧠 **Operaciones matemáticas**
Estos son los temas utilizados para resolver el proyecto.

🔹 Multiplicación de matrices.

🔹 Matrices inversas.

🔹 Determinantes.

🔹 Sistema de ecuaciones.

🔹 Producto escalar.

🔹 Producto vectorial.

## 🧠 **Métodos de Numpy.**
Explicaremos brevemente los métodos utilizados en Numpy para poder trabajar con nuestas clases.


🔹 ***np.linalg.inv()*** => Inversa de una matriz.

🔹 ***matriz_a @ matriz_b*** => Multiplicación de matrices.

🔹 ***np.array()*** => Creación de arrays.

🔹 ***np.linalg.solve***(primer_termino, segundo_termino) => Resolución de sistema de ecuaciones.

🔹 ***np.ravel()***  => convierte un array multidimensional en uno unidimensional

🔹 ***np.deg2rad()*** => Convierte un ángulo en grados a radianes.

🔹 ***np.cos()*** => Función Coseno.

🔹 ***np.sen()*** => Función Seno.

🔹 ***np.reshape()*** => Función para transformar la dimensión de arrays. Ejemplo, pasar de 1x6 a 6x1.

- Si el array es un 1x6, usamos np.reshape(-1, 1): -1 significa que toma el máximo valor que en este caso es 6 que serán las filas, y : 1, que será el número total de columnas. Ahora el array es de 6x1.


## 💾 **Datos**
*Todos los datos fueron almacenados dentro de la carpeta datos*.

📦 Proyecto-algebra-linea

┣ 📂 datos > datos encriptados.txt 

┃ ┣ valores desencriptados.txt 

┃ ┣ valores rotados.txt

┃ ┣ valores trasladados.txt


## 🧮 **Ecuaciones**

Antes de empezar a desencriptar los datos, tenemos que tener todos los datos de nuestra matriz 6x6 la cual usaremos para resolver el proyecto. 

Tenemos la siguiente matriz la cual tiene incógnitas que hay que encontrar: 

```bash
            a    3   b   5   c   8

            6    d   0   e   7   f

            g    8   h   1   i   7
A =        
            11   j   8   k   12  m

            n   -1   p  -5   r   3 

            4    t   2   w   9   z

```

### 1️⃣ **Primera Ecuación**

```bash

Resolvemos nuestra ecuación de 10x10

6𝑎 + 7𝑏 − 𝑐 − 12𝑑 + 14𝑒 + 5𝑓 − 12𝑔 − 3ℎ + 9𝑖 − 5𝑗 = 48

2𝑎 − 15𝑏 + 8𝑐 + 6𝑑 − 7𝑒 + 9𝑓 − 9𝑔 + 5ℎ − 8𝑖 − 6𝑗 = 64

−25𝑎 + 10𝑏 − 9𝑑 − 12𝑒 + 14𝑓 − 6𝑔 + 8ℎ − 13𝑖 + 4𝑗 = −132

6𝑎 − 3𝑏 + 5𝑐 − 16𝑑 + 𝑒 + 9𝑓 − 7𝑔 + 3ℎ − 4𝑖 + 5𝑗 = −75

8𝑎 − 9𝑏 + 6𝑐 − 𝑑 − 𝑒 − 5𝑓 + 7𝑔 + 3𝑖 + 2𝑗 = −16

−5𝑎 + 6𝑏 + 9𝑐 − 2𝑑 + 10𝑒 − 14𝑓 + 3𝑔 + 5ℎ − 12𝑖 + 6𝑗 = −408

−4𝑎 + 5𝑏 + 8𝑐 − 2𝑑 + 9𝑒 − 8𝑓 + 4𝑔 + ℎ − 2𝑗 = −203

𝑎 + 𝑏 + 2𝑐 − 3𝑑 + 4𝑒 − 𝑓 − 4𝑔 − 7ℎ + 2𝑖 − 4𝑗 = 59

10𝑎 + 5𝑏 − 9𝑐 + 6𝑑 + 𝑒 + 𝑓 + 7𝑔 − 8ℎ + 3𝑖 + 11𝑗 = 126

−2𝑎 + 4𝑏 + 3𝑐 + 5𝑑 − 10𝑒 − 𝑓 + 3𝑔 − ℎ − 7𝑖 + 𝑗 = 2


# Pasamos todos los datos del primer término a un array.
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

#Ahora pasamos los datos del segundo término a otro array.

segundo_termino = np.array([48, 64, -132, -75, -16, -408, -203, 59, 126, 2], dtype=int)

#Tenemos una clase Ecuacion() la cual hace uso de np.linalg.solve para resolver el sistema.
ecuacion = Ecuacion()

matriz = ecuacion.resolver(primer_termino, segundo_termino)

# la matriz da los resultados tales que.
# (2,−2,−3,5,−9,4,−7,−10,11,0)
```

- ⚠️ Para ver la clase Ecuacion(), por favor presione [Aquí](###Ecuacion())


💡 Para las incógnitas 𝑘, 𝑚, 𝑛, 𝑝, 𝑟,𝑡, 𝑤, 𝑧 debe resolver las siguientes operaciones entre vectores:

### 2️⃣ **Segunda Ecuación**

*Se tienen los vectores 𝑈⃗ = (3, 6, 7) y 𝑉⃗ = (𝑘, 𝑚, 𝑛). El resultado de operar 2𝑈⃗ × 3𝑉⃗ es igual a 612𝑖̂+ 156𝑗̂− 396𝑘̂ y el producto 𝑈⃗ ∙ 𝑉⃗ = 58*

Segunda Ecuación ecuación para encontrar k, m, n.

$$
2U X 3V = (612, 156, -396)
$$


$$
\frac{2U X 3V}{6} = (102, 26, -66)
$$

Despejamos k y m para poder dejar n como una variables independiente.

$$
6n - 7m = 102
$$

$$
7k -3n = 26     -->  m = \frac{6n - 102}{7}
$$

$$
3m - 6k = -66    -->  k = \frac{3n + 26}{7}
$$

Ahora que (n) es una variable independiente, cambiamos a la ecuación de producto escalar despejando n, para esto reemplazamos k y m.

$$
U * V = 58
$$

Multiplicamos toda la expresión por 7, así removemos las divisiones.

$$
3 (\frac{3n + 26}{7}) + 6(\frac{6n - 102}{7}) + 7n = 58
$$


$$
9n + 78 + 36n - 612 + 49n = 406
$$

Despejamos

$$
94n = 490
$$

$$
n = 10
$$

Conociendo el valor de n, podemos encontrar k y m con las ecuaciones anteriores:

$$
m = \frac{6n - 102}{7}
$$

$$
k = \frac{3n + 26}{7}
$$

Empecemos con (m) sustituyendo n por 10:

$$
m = \frac{6(10) -102}{7} -- > m = -6
$$

Ahora encontramos (k) sustituyendo n por 10:

$$
k = \frac{3(10) +26}{7}  -- > k = 8
$$

Para finalizar tenemos los valores:

$$
k = 8, m = -6, n = 10
$$


----------------------------------------------------------------------------

### 3️⃣ **Tercera Ecuación**

Se tienen los vectores 𝑈⃗ = (6, 𝑝, 𝑟) y 𝑉⃗ = (𝑡, 8, 9). El resultado de operar 3𝑈⃗ − 10𝑉⃗ es igual a −42𝑖̂− 68𝑗̂− 126𝑘̂

$$
U = (6, p, r) \quad V = (t, 8, 9)
$$

$$
3U - 10V = (-42, -68, -126)
$$

$$
3U = (18, 3p, 3r) \quad  10V = (10t, 80, 90)
$$

$$
(t) \quad  18 -10t = -42
$$

$$
-10t = -60 \quad (t) = 6
$$

$$
(p) \quad  3p - 80 = -68
$$

$$
3p = 12 \quad (p) = 4
$$


$$
(r) \quad  3r - 90 = -126
$$

$$
  3r = -36 \quad (r) = -12
$$

$$
(t) = 6, \quad (p) = 4, \quad (r) = -12
$$

-----------------------------------------


### 4️⃣ **Cuarta Ecuación**

Se tienen los vectores: 

$$
U = (\frac{-1}{2}, \frac{\sqrt{38}}{2}, \frac{5}{2})
$$

$$
V = (11, \sqrt{342}, -21)
$$

La magnitud de |𝑈⃗ | es igual a −𝑤. Además, el producto escalar 𝑈⃗ ∙ 𝑉⃗ es igual a 𝑧.

***Buscamos solamente la variable w primero:***

$$
U = (\frac{-1}{2}, \frac{\sqrt{38}}{2}, \frac{5}{2})
$$

$$
|u| = -w
$$

$$
|U| = \sqrt{(\frac{1}{2})^2 + (\frac{\sqrt{32}}{2})^2 + (\frac{5}{2})^2}
$$

$$
|U| = \sqrt{\frac{1}{4} + \frac{38}{4} + \frac{25}{4}}
$$

$$
|U| = \sqrt{\frac{64}{4}}
$$

$$
|U| = 4
$$

$$
(W) = -4
$$

-----------------------------------------

***Ahora buscamos la variable z:***

El producto escalar 𝑈⃗ ∙ 𝑉⃗ es igual a 𝑧.

$$
U * V = z
$$

$$
U = (\frac{-1}{2}, \frac{\sqrt{38}}{2}, \frac{5}{2})
$$

$$
V = (11, \sqrt{342}, -21)
$$

$$
(U * V) = (\frac{-1}{2} * \frac{11}{1}) + (\frac{\sqrt{38}}{2} * \frac{3\sqrt{38}}{1}) + (\frac{5}{2} * \frac{-21}{1})
$$

$$
(U * V) = (\frac{-11}{2}) + (\frac{3\sqrt{38}^2}{2}) + (\frac{-105}{2})
$$

$$
(U * V) = (\frac{-11}{2} - \frac{-105}{2}) + (\frac{57}{1})
$$

$$
(U * V) = -58 + 57
$$

$$
(U * V) = -1
$$

$$
(Z) = -1
$$



------------------------------------------------------------------
### ✅ **Resultado de las ecuaciones.**

En total tenemos las siguientes variables encontradas con la ecuación también realizada anteriormente en la clase Ecuación.

$$
a = 2, \quad b = -2, \quad c = -3, \quad d = 5, \quad e = -9, \quad f = 4, \quad g = -7, \quad h = -10, \quad i = 11, \quad j = 0, \quad k = 8, \quad m = -6, \quad n = 10, \quad w = -4, \quad z = -1, \quad p = 4, \quad t = 6, \quad r = -12
$$

Al final la matriz para codificar los vectores es:

    [ 2,  3, -2,  5, -3,  8]
    [ 6,  5,  0, -9,  7,  4]
    [-7,  8,-10,  1, 11,  7]
    [11,  0,  8,  8, 12, -6]
    [10, -1,  4, -5, -12, 3]
    [ 4,  6,  2, -4,  9, -1]


## ⚙️ **Clases**

*Ahora que ya resolvimos nuestras ecauciones y obtuvimos nuestra matriz completa, ya podemos comenzar a programar para poder desencriptar nuestros datos*

### 💾 **Librerías**

*Primero importamos las librerías que usaremos a lo largo de nuestro proyecto*

```bash

import numpy as np
import matplotlib.pyplot as plt

```

### **Cifrado()**

*Creamos nuestra clase Cifrado la cual Cifra, descifra datos y podemos obtener una matriz inversa para depurar.*

### **Funcionamiento de la clase Cifrado()**


- ⚡ Primero tenemos la función ***`inversa()`*** la cual nos devuelve la inversa de la matriz ingresada.

- ⚡ Tenemos la función ***`cifrar()`*** la cual obtiene 2 matrices y las multiplica y nos devuelve la matriz multiplicada (cifrada).

- ⚡ Por último tenemos la función ***`descifrar()`*** la cual obtiene 2 matrices. La primer matriz es la matriz usada para descifrar y la segunda es la que tiene los datos cifrados. La funcióin crear la matriz inversa y la multiplica por la matriz con los datos cifrados y por último devuelve una matriz con los datos descifrados.

⚠️ Nota: La función ***`inversa()`*** es utilizada para depurar, por eso la función ***`descifrar()`*** también resuelve la matriz inversa por sí sola.

```bash

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

    def descifrar(self, matriz_codificacion, matriz_resolver):
        self.matriz_codificacion = matriz_codificacion
        self.matriz_resolver = matriz_resolver

        matriz_inversa = np.linalg.inv(self.matriz_codificacion)

        matriz_decifrada = matriz_inversa @ self.matriz_resolver

        return matriz_decifrada


```

### **Crear_Array()**

*La clase `crear_array()` fue creada con el objetivo de obtener un arreglo con valores alternados de `(x,y)` en un formato (x1, y1, x2, y2...) y los separará en dos arreglos independientes con las cordenadas `(x)` y `(y)`*.

### **Funcionamiento de la clase Crear_Array()**

**Método valores_x()**

- Recorre el arreglo original y toma los valores impares (1, 3, 5...). Cada uno de estos valores corresponde a `(x)`.

- Finalmente nos devuelve un arreglo con los valores de `(x)`.

**Método valores_y()**

- Recorre el arreglo original también, pero ahora solo toma los valores pares (2, 4, 6...) y cada uno de estos valores corresponderá a `(y)`.

- Agregamos todos esos valores en un nuevo arreglo y lo devolvemos.


```bash

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

```

### **Ecuacion()**

*Creamos una clase llamada ecuación con la finalidad de resolver la ecuación $10x10$ brindada en las instrucciones del proyecto.*

### **Funcionamiento de la clase Ecuacion()**


- La clase nos pide los valores separados del primero término y segundo término de la ecuación.

- Hacemos uso de *`np.linalg.solve()`* para poder obtener los valores de las incógnitas.

- Por último nos devuelve un arreglo con las incógnitas descubiertas.

```bash

class Ecuacion():
    def resolver(self, primer_termino, segundo_termino):
        self.primer_termino = np.array(primer_termino)
        self.segundo_termino = np.array(segundo_termino)

        solucion = np.linalg.solve(self.primer_termino, self.segundo_termino)


        return solucion

```

### **Desempaquetar()**

*Esta clase se encarga de transformar los arreglos de coordenadas (x, y) en listas unidimensionales. Debido a que la clase `App()` devuelve los datos en un formato anidado como:*

```bash
[[array([x1, x2, x3])], [array([y1, y2, y3])]]
```

*Sin embargo, para aplicar operaciones como Traslación, Rotación o para graficar los puntos usando `zip(x, y)`, es necesario trabajar con estructuras unidimensionales como:*

```bash
[x1, x2, x3]   y  [y1, y2, y3]
```

### **Funcionamiento de la clase Desempaquetar()**


1️⃣ Pedimos los arreglos separados de `(x, y)`.

2️⃣ Creamos un for para cada valor de `(x, y)`.

3️⃣ Aplanamos los arreglos para dejarlos unidimensionales.

4️⃣ Agregamos los datos a un nuevo arreglo.

5️⃣ Devolvemos los arreglos ya aplanados.


```bash

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

```

### **Rotacion()**

*La clase Rotacion aplica una transformación geométrica de rotación a un conjunto de puntos en el plano cartesiano.*


*Recibe dos listas de coordenadas `(x, y)`, y devuelve las nuevas coordenadas resultantes después de ser rotadas un ángulo determinado.*

La matriz de rotación en 2D está definida como:

$$
R(\theta) =
\begin{bmatrix}
\cos(\theta) & -\sin(\theta) \\
\sin(\theta) & \cos(\theta)
\end{bmatrix}
$$

Y la transformación de un punto $(x, y)$ se obtiene mediante:

$$
\begin{bmatrix}
x' \\
y'
\end{bmatrix}
=
R(\theta)
\cdot
\begin{bmatrix}
x \\
y
\end{bmatrix}
$$

### **Funcionamiento de la clase Rotacion()**


1️⃣ Pedimos los valores de `(x, y)` es arreglos separados.

2️⃣ El ángulo (135 grados para nuestro ejemplo) es convertido a radianes.

3️⃣ Iteramos los valores de `(x, y)` y los agregamos a una matriz de 2x1

4️⃣ Multiplicamos la matriz de rotación por la matriz 2x1

5️⃣ Obtenemos los nuevos valores de `(x, y)` ya rotados y los agregamos a un nuevo arreglo.

6️⃣ Por último la función nos regresa dos arreglos con los datos `(x, y)` ya rotados.


```bash

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

```

### **Traslacion()**

La clase Traslacion aplica una transformación geométrica de traslación a un conjunto de puntos en el plano cartesiano.


Recibe coordenadas `(x, y)` y las desplaza una distancia *a* en el eje x y *b* en el eje y.

La matriz de traslación en coordenadas homogéneas se define como:

$$
T(a, b) =
\begin{bmatrix}
1 & 0 & a \\
0 & 1 & b \\
0 & 0 & 1
\end{bmatrix}
$$

Aplicada a un punto $(x, y)$, la transformación se realiza mediante el producto matricial:

$$
\begin{bmatrix}
x' \\
y' \\
1
\end{bmatrix}
=
T(a, b)
\cdot
\begin{bmatrix}
x \\
y \\
1
\end{bmatrix}
$$

### **Funcionamiento de la clase Traslacion()**


1️⃣ Pedimos los valores de `(x, y)` y `(a, b)` es arreglos separados.

2️⃣ Iteramos los valores de `(x, y)` y los agregamos a una matriz de 2x1.

3️⃣ Multiplicamos la matriz de traslación por la matriz 2x1.

4️⃣ Obtenemos los nuevos valores de `(x, y)` ya trasladados y los agregamos a un nuevo arreglo.

5️⃣ Por último la función nos regresa dos arreglos con los datos `(x, y)` ya trasladados.


```bash

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

```

### **GuardarDatos()**

*Esta clase permite almacenar las coordenadas generadas durante el proceso (rotación, traslación, etc.) en un archivo de texto externo.*

*Los valores se guardan en formato de pares ordenados:*

```bash
(x1, y1)
(x2, y2)
(x3, y3)
```

### **Funcionamiento de la clase GuardarDatos()**


1️⃣ Recibe los arreglos `(x, y)` y el nombre del archivo.

2️⃣ Creamos o reemplazamos los datos del nombre del archivo .txt

3️⃣ Recorremos los arreglos usando `zip(x, y)`.

4️⃣ Guardamos los pares `(x, y)` como una línea en nuestro archivo.

5️⃣ Cerramos el documento con with open().

```bash

class GuardarDatos():
    def save(self, valores_x, valores_y, nombre_archivo):
        self.valores_x = valores_x
        self.valores_y = valores_y
        self.nombre_archivo = nombre_archivo

        with open(self.nombre_archivo, "w") as f:
            for x, y in zip(valores_x, valores_y):
                f.write(f"({x}, {y})\n")

```

### **App()**

*La clase **`App`** se encarga de abrir un archivo que contiene datos encriptados o sin encriptar, procesarlos y ejecutar la lógica correspondiente para **cifrar** o **descifrar** los valores.*


*Los datos leídos se convierten en una matriz y posteriormente se desempaquetan para obtener los valores en los ejes `(x,y)`*

### **Funcionamiento de la clase App()**


1️⃣ Lee un archivo línea por línea.

2️⃣ Transforma los datos numéricos en una matriz columna.

3️⃣ Aplica el método de cifrado o descifrado según el parámetro `condicional`.

4️⃣ Finalmente, separa los valores resultantes en arreglos independientes para `(x, y)`.

```bash

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

                elif self.condicional == "descifrar":
                    resultado = cir.descifrar(matriz_original, array)

                valores_x = create.valores_x(resultado)
                valores_y = create.valores_y(resultado)

                array_valores_x.append(valores_x)
                array_valores_y.append(valores_y)

        return array_valores_x, array_valores_y

```

### **Graficar()**

*Esta clase nos permite graficar todos los puntos `(x, y)` con los datos Desencriptados, Rotados y Trasladados*

### **Funcionamiento de la clase Graficar()**

1️⃣ Obtiene dos arreglos con los valores `(x, y)`.

2️⃣ Utilizamos `Matplotlib` para graficar cada uno de estos datos.

3️⃣ Con el método `plt.show()` mostramos el gráfico.


```bash

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

```

## **Instancias**

*Inicializamos nuestras instancias de clases:*

```bash

    aplicacion = App()
    rotar = Rotacion()
    desempaquetador = Desempaquetar_Array()
    graficar = Graficar()
    traslacion = Traslacion()
    guardar_datos = GuardarDatos()
    cir = Cifrado()
    create = crear_array()

```

## **Comprobación de Datos**

### **Matriz Inversa**

*Buscamos comprobar que la clase Cifrado con el método inversa funciona para poder obtener la inversa de nuestra matriz*

`Input:`

```bash

inversa = cir.inversa(matriz_codificacion)
print(f"La matriz inversa es: \n{inversa}")
```

`Output: `

```bash

La matriz inversa es: 
[[-0.13562749 -0.03955583  0.16534674  0.097423    0.19435366 -0.08729311]
 [ 0.02119736 -0.18428661  0.04575739 -0.04399749  0.08185104  0.26227216]
 [ 0.28413995  0.12090928 -0.33697884 -0.11187932 -0.30448355  0.15573015]
 [ 0.03036874 -0.074251    0.03071444  0.03456945  0.01842657  0.00880997]
 [ 0.01988791  0.10211607 -0.03490467  0.02074167 -0.08727739 -0.06304735]
 [ 0.21047035  0.19392416 -0.17502619 -0.04965431 -0.19964907 -0.06674523]]

```

### **Desencriptar datos**

Multiplicaremos nuestra matriz inversa por la matriz con los datos codificados y de esta manera poder descifrarlos. Así podemos corroborarque los datos son correctos y que nuestra función sí nos brinda los resultados correctos.

La matriz con los datos encriptados es:

```bash
[230.3]
[263.5]
[238.8]
[814.8]
[-100]
[432.7]
```

`Input:`

```bash
#nuestra matriz de 6x1 y nuestra matriz de 6x6, usamos reshape para cambiar su dimensión a 6x1
dato_encriptado = np.array([230.3, 263.5, 238.8, 814.8, -100, 432.7]).reshape(-1, 1)
#guardamos los datos usando la clase decifrar.
datos_desencriptados = cir.descifrar(matriz_codificacion, dato_encriptado)
#mostramos los datos por pantalla
print(datos_desencriptados)
```

`Output: `

```bash
[[20. ]
 [36.7]
 [23.5]
 [24.9]
 [21.5]
 [ 8.4]]

```


### **Rotación de datos**

Ya comprobamos que los datos son desencriptados correctamente usando nuestras clases y métodos. Ahora comprobaremos que los datos pueden ser rotados.

Teniendo nuestra variable datos_desencriptados, usaremos la clase Rotacion para rotar los datos brindados y darnos los nuevos resultados.

La clase Rotacion() nos pide datos_x, datos_y. Esto fue realizado para poder realizar nuestra gráfica con matplotlib. Tenemos la clase crear_array() la cual nos ayuda a obtener los valores x, y para utilizar este método.

`Input: `

```bash

#Primero obtenemos los resultados (x, y), así se los podemos pasar a nuestra clase.
valor_prueba_x = create.valores_x(datos_desencriptados)
#mostramos los datos
print(f"Los valores de x son : {valor_prueba_x}")
#obtenemos los resultados para y
valor_prueba_y = create.valores_y(datos_desencriptados)
#mostramos los datos de y
print(f"Los valores de y son: {valor_prueba_y}")

#estos datos aún no están rotados, la rotación será ahora con la clase Rotacion()

```

`Output: `

```bash

Los valores de x son : [array([20.]), array([23.5]), array([21.5])]
Los valores de y son: [array([36.7]), array([24.9]), array([8.4])]


```


⚠️ Podemos notar que los valores de (x,y) están en arrays anidados, por lo cual será necesario desempaquetarlos a través de la clase Desempaquetar_Array(), así de esta manera por fin podremos rotar los datos.

`Input: `

```bash

valor_prueba_desempaquetar_x, valor_prueba_desempaquetar_y = desempaquetador.desempaquetar(valor_prueba_x, valor_prueba_y)
#mostramos los valores
print(f"Los valores de x son: {valor_prueba_desempaquetar_x}")
print(f"Los valores de y son: {valor_prueba_desempaquetar_y}")

#Ahora ya podemos usar la clase Rotacion()

valor_prueba_rotados_x, valor_prueba_rotados_y = rotar.rotar_matriz(valor_prueba_desempaquetar_x, valor_prueba_desempaquetar_y)
#Mostramos los valores

print(f"Los valores x rotados son: {valor_prueba_rotados_x}")
print(f"Los valores y rotados son: {valor_prueba_rotados_y}")

```

`Output: `

```bash

Los valores de x son: [np.float64(20.000000000000007), np.float64(23.499999999999986), np.float64(21.50000000000001)]

Los valores de y son: [np.float64(36.69999999999996), np.float64(24.900000000000002), np.float64(8.400000000000023)]

Los valores x rotados son: [np.float64(-40.09295449327722), np.float64(-34.22396820942889), np.float64(-21.142492757477793)]

Los valores y rotados son: [np.float64(-11.808683245815308), np.float64(-0.9899494936611762), np.float64(9.263098833543765)]

```

Como pudimos comprobar, los valores fueron rotados exitosamente por lo que podemos comprobar que la clase Rotacion() funciona sin ningún problema, ahora pasaremos a trasaladar los datos.

### **Traslación**

Ahora buscaremos comprobar que la clase `Traslacion()` funciona pasándole los datos anteriomente brindados.

La clase `Traslacion()` recibe los datos de `(x,y)` y `(a,b)`. Donde `(a,b)` son las distancias de traslación para los ejes `(x,y)`.

`Input: `

```bash

#usaremos los datos anteriomente rotados para obtener los datos finales.
valor_prueba_transladado_x, valor_prueba_trasladado_y = traslacion.trasladar_matriz(valor_prueba_rotados_x, valor_prueba_rotados_y, 20, 30)

#pasamos los valores (a,b) como (20,30)
#mostramos los datos.

print(f"Los valores trasladados para x son: {valor_prueba_transladado_x}")
print(f"Los valores trasladados para y son: {valor_prueba_trasladado_y}")

```

`Output: `

```bash

Los valores trasladados para x son: [np.float64(-20.09295449327722), np.float64(-14.22396820942889), np.float64(-1.1424927574777932)]

Los valores trasladados para y son: [np.float64(18.19131675418469), np.float64(29.010050506338825), np.float64(39.263098833543765)]

```

Con estas comprobaciones logramos obtener todos los datos y asegurarnos que las clases y métodos funcionan para ahora poder pasar un archivo.txt con todos los datos y así poder desencriptar los datos de forma automatizada.

Mostraremos los datos para corroborar las gráficas


## **Gráficas de Comprobación**

### > **Datos Desencriptados**

`Input: `

```bash

#Grafica para los puntos desencriptados únicamente.
graficar.graficadora(valor_prueba_x, valor_prueba_y)

```

`Output: `


<p align="center">
    <img src="imagenes\datos_desencriptados_test.png">
</p>

### > **Datos Rotados**

`Input: `

```bash

#Grafica para los datos rotados
graficar.graficadora(valor_prueba_rotados_x, valor_prueba_rotados_y)

```

`Output: `

<p align="center">
    <img src="imagenes\datos_rotados_test.png">
</p>


### > **Datos Trasladados**

`Input: `

```bash

#Gráfica para los datos rotados y trasladados
graficar.graficadora(valor_prueba_transladado_x, valor_prueba_trasladado_y)

```

`Output: `

<p align="center">
    <img src="imagenes\datos_trasladados_test.png">
</p>



## > **Desencriptar**

*Como ya comprobamos que las clases y métodos funcionan, ahora les pasaremos un archivo "datos encriptados.txt" el cual tiene todos los datos encriptados. Cada línea tiene 6 datos los cuales corresponderán a nuestras matrices 6x1 y resolveremos línea por línea de nuestro documento.*

*Obtenemos cada valor para nuestros datos:*

```bash

#Desencriptamos todos los valores para (x, y)
valores_x, valores_y = aplicacion.abrir_document(matriz_codificacion, "/content/drive/MyDrive/Colab Notebooks/datos encriptados.txt", "decifrar")

#Los datos están anidados, así que los aplanamos con la clase Desempaquetar_Array()
desempaquetar_x, desempaquetar_y = desempaquetador.desempaquetar(valores_x, valores_y)

#Rotamos los datos ahora que están desempaquetados
valores_rotados_x, valores_rotados_y = rotar.rotar_matriz(desempaquetar_x, desempaquetar_y)

#Trasladamos los datos ya rotados para obtener la última gráfica.
valores_trasladados_x, valores_trasladados_y = traslacion.trasladar_matriz(valores_rotados_x, valores_rotados_y, 20, 30)

```

*Como ya tenemos todos nuestros valores `Desencriptados`, `Rotados` y `Trasladados` ahora hace uso de nuestra clase `Graficar()` para visualizar los datos.*


## > *Graficas - Datos Resueltos!*

### > *Gráfico desencriptado*

`Input: `

```bash

graficar.graficadora(desempaquetar_x, desempaquetar_y)

```

`Output: `

<p align="center">
    <img src="imagenes\datos_desencriptados.png">
</p>

### > *Gráfico Matriz Rotación*

`Input: `

```bash

graficar.graficadora(valores_rotados_x, valores_rotados_y)


```

`Output: `

<p align="center">
    <img src="imagenes\datos_rotados.png">
</p>


### > *Gráfico Matriz Rotación y Traslado*

`Input: `

```bash

graficar.graficadora(valores_trasladados_x, valores_trasladados_y)

```

`Output: `

<p align="center">
    <img src="imagenes\datos_trasladados.png">
</p>


## > *Guardar Datos*

*Guardamos los datos ya desencriptaods, rotados y trasladados en nuevos archivos.*

```bash

guardar_datos.save(desempaquetar_x, desempaquetar_y, "datos\valores desencriptados.txt")

guardar_datos.save(valores_rotados_x, valores_rotados_y, "datos\valores rotados.txt")

guardar_datos.save(valores_trasladados_x,valores_trasladados_y,"datos\valores trasladados.txt")

```


## 👨‍💻 Autor

<p align="center">
    Hecho con ☕ (quizá demasiado)!
    <br>
    <i><b>Junior Eduardo Garniga Rojas</b></i></a>  👾

</p>


<p align="center">
    <a href="https://github.com/jgarnigar">
        <img src= "https://img.shields.io/badge/GitHub-jgarnigar-181717?style=for-the-badge&logo=github">
    </a>
</p>

import numpy as np

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

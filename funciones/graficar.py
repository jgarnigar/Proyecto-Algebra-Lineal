import matplotlib.pyplot as plt


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
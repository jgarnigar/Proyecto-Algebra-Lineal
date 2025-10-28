

class GuardarDatos():
    def save(self, valores_x, valores_y, nombre_archivo):
        self.valores_x = valores_x
        self.valores_y = valores_y
        self.nombre_archivo = nombre_archivo

        with open(self.nombre_archivo, "w") as f:
            for x, y in zip(valores_x, valores_y):
                f.write(f"({x}, {y})\n")
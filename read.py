from pathlib import Path

carpeta = Path("funciones")

for archivos in carpeta.glob("*"):
    with open("todos los archivos.txt", "a")as f:
        f.write(str(archivos))


print(carpeta.exists())
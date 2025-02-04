#
from pathlib import Path

# Creamos una variable de path apartir e la clase path i indicamos un directorio
path = Path("directorio")

#

# Si este existe
path.exists()
# Crear la carpeta o diirectorio
path.mkdir()
# eliminar la carpeta o directorio (con la condicion que tiene que estar vacio)
path.rmdir()
# para cambiarle el nombre al directorio
path.rename("Nuevo-nombre")
#

for p in path.iterdir():
    print(p)


archvios = [p for p in path.iterdir() if not p.is_dir()]  #
archvios = [p for p in path.glob("01-*.py")]  #
archvios = [p for p in path.glob("**/*.py")]  #

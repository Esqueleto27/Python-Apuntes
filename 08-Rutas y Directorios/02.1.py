# Trabajando con directorios y archivos en Python con pathlib
from pathlib import Path

# Crear una variable 'path' a partir de la clase Path, indicando un directorio (puede existir o no)
path = Path("directorio")

# Verificar si el directorio existe
print(path.exists())

# Crear un nuevo directorio (si no existe)
path.mkdir()

# Eliminar el directorio (debe estar vacío para que funcione)
path.rmdir()

# Renombrar el directorio a "Nuevo-nombre"
path.rename("Nuevo-nombre")

# Recorrer los elementos dentro del directorio y mostrarlos
for p in path.iterdir():
    print(p)

# Filtrar archivos dentro del directorio con diferentes métodos de búsqueda
archivos = [
    p for p in path.iterdir() if not p.is_dir()
]  # Lista solo archivos, excluyendo carpetas
archivos = [
    p for p in path.glob("01-*.py")
]  # Busca archivos que comiencen con "01-" y terminen en ".py"
archivos = [
    p for p in path.glob("**/*.py")
]  # Busca todos los archivos ".py" en subdirectorios recursivamente

print(archivos)  # Muestra los archivos encontrados según la búsqueda

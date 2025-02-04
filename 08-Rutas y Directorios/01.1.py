# Trabajando con archivos, directorios y rutas en Python

# El módulo pathlib nos permite trabajar con rutas de archivos y directorios de manera sencilla y multiplataforma.
# Path nos permite crear y manipular rutas, ya sean absolutas o relativas.
from pathlib import Path

# Crear una ruta absoluta (especifica toda la ubicación desde la raíz del sistema)
ruta_absoluta = Path("/usr/bin")  # Ruta en macOS/Linux

# Obtener la ruta del directorio home del usuario
ruta_home = Path.home()

# Crear una ruta relativa (su ubicación depende del directorio donde se ejecute el script)
ruta_relativa = Path("one/__init__.py")

# Crear una referencia a un archivo en un directorio (la ruta puede existir o no, simplemente se define)
ruta_archivo = Path("hola-mundo/mi-archivo.py")

# Métodos para verificar propiedades de una ruta
print(ruta_archivo.is_file())  # Verifica si la ruta es un archivo existente
print(ruta_archivo.is_dir())  # Verifica si la ruta es un directorio
print(ruta_archivo.exists())  # Verifica si la ruta existe en el sistema de archivos

# Obtener información de una ruta
print(ruta_archivo.name)  # Nombre del archivo con su extensión (mi-archivo.py)
print(ruta_archivo.stem)  # Nombre del archivo sin la extensión (mi-archivo)
print(ruta_archivo.suffix)  # Extensión del archivo (.py)
print(ruta_archivo.parent)  # Directorio padre de la ruta (hola-mundo/)
print(ruta_archivo.absolute())  # Ruta absoluta del archivo

# Crear una nueva ruta cambiando el nombre del archivo dentro del mismo directorio
ruta_modificada = ruta_archivo.with_name(
    "Skeletor.py"
)  # Reemplaza "mi-archivo.py" por "Skeletor.py"
print(ruta_modificada)  # Muestra la nueva ruta generada

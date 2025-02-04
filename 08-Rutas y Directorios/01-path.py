# Vamos a ver archvios directorios y con la ruta que son fundamentos
# path nos va a servir para referenciar una ruta dentro de nuestras maquinas
# No hace falta que la ruta exista, solo es una referencia

from pathlib import Path

# Macos
Path("/usr/bin")  # Crea una ruta para ese directorio y es una ruta absoluta

Path.home()  # Ruta a la carpeta home del usuario

Path("one/__init__.py")  # Es una ruta relativa

# Podria existir como no, solo es una referencia
Path = Path("hola-mundo/mi-archivo.py")

# Para ver si es un archivo
Path.is_file()
# Para ver si es un directorio
Path.is_dir()
# Para ver si existe
Path.exists()


# 1. Nombre del archvio incluyendo su extension
# 2. Nombre pero sin su extension
# 3. La extension
# 4. El directorio padre
# 5. La ruta absoluta
print(Path.name, Path.stem, Path.suffix, Path.parent, Path.absolute())

# Podemos crear otros metodos para trabajar con Path

p = Path.with_name("Skeletor.py")

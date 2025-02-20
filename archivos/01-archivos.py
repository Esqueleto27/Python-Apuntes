# Importa la clase Path desde pathlib para trabajar con rutas de archivos
from pathlib import Path

# Para ver la hora mas legible
from time import ctime

# Crea un objeto Path que representa la ruta del archivo
archivo = Path("09-archivos/archivo-prueba.txt")

# Dentro de los métodos que tiene archivo existen:

# Verifica si el archivo existe (retorna True o False)
archivo.exists()

# Renombra o mueve el archivo a una nueva ubicación
archivo.rename("nuevo-nombre.txt")

# Elimina el archivo de la ubicación especificada
archivo.unlink()

# Para ver las estadisticas que tiene el archvio
print(archivo.stat())

# Para ver el acceso, creacion, modificacion
print("acceso", ctime(archivo.stat().st_atime))
print("creacion", ctime(archivo.stat().st_ctime))
print("modificacion", ctime(archivo.stat().st_mtime))

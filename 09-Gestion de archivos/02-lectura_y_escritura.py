# --------------------------------------------
# GESTIÓN DE ARCHIVOS EN PYTHON USANDO PATHLIB
#
# Este código muestra cómo leer, modificar y escribir archivos de texto
# utilizando la biblioteca `pathlib`, que facilita el trabajo con rutas
# de archivos de forma más intuitiva y moderna.
# --------------------------------------------

# Importamos la clase Path del módulo pathlib.
# Esta clase nos permite trabajar con rutas de archivos y carpetas de forma sencilla.
from pathlib import Path

# Creamos una referencia (objeto Path) hacia el archivo 'archivo-prueba.txt'
# que se encuentra dentro de la carpeta '09-Gestion de archivos'.
archivo = Path("09-Gestion de archivos/archivo-prueba.txt")

# Leemos el contenido del archivo de texto usando codificación UTF-8.
# El método read_text() devuelve todo el texto como una cadena.
# Luego usamos .split("\n") para dividir esa cadena en una lista de líneas.
texto = archivo.read_text("utf-8").split("\n")

# Insertamos la línea "Hola Mundo!" al inicio de la lista de líneas del archivo.
# insert(0, "Hola Mundo!") coloca el nuevo texto al principio de la lista.
texto.insert(0, "Hola Mundo!")

# Unimos nuevamente la lista de líneas en una sola cadena de texto separada por saltos de línea.
# Luego escribimos ese contenido actualizado en el mismo archivo, reemplazando el contenido anterior.
archivo.write_text("\n".join(texto), "utf-8")

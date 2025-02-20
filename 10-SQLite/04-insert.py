# Aqui vamos a insertar datos dentro de una tabla con SQLite
#

# Importamos
import sqlite3

# Creamos nuestro bloque de with
#
# Para nosotros ingresar datos necesitamos crear nuestro objeto de cursor que se crea apartir de nuestro metodo de conexion
#
with sqlite3.connect("10-SQLite/app.db") as con:
    cursor = con.cursor()
    # Insert into la tabal (usuarios), value = SQL estandar
    # Ponemos dos signos de interogacion porque vamos a pasar dos valores, una primery key y un nombre
    # Pasamos un segundo argumento (tupla) y se hace asi para que no nos hagan  SQL injection
    # Se pasa primero la consulta y luego los valores mismo para prevenir
    cursor.execute("insert into usuarios values(?, ?)", (1, "Hola mundo"))
    # Y no ponemos el close porque la with ya lo cierra

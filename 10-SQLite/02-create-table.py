# Instrucciones para crear una tabla dentro de SQLite
# No olvidar importar SQLite3
import sqlite3

# Creamos la conexion en donde nos encontramos (archivo)
con = sqlite3.connect("10-SQLite/app.db")

# Para generar consultas debemos generar una variable
# Para nostros realizar consultas a nuestra base de datos, vamos a necesitar crear un objeto llamado cursor que se crea en apartir del objeto de conexion
# El objeto de cursor va a funcionar como intermediario entre la libreria de sqlite3 y nosotros
cursor = con.cursor()


# Aqui vamos a ejecutar un consulta y siempre lo hacemos con "execute"
cursor.execute(
    """
CREATE TABLE if not exists usuarios(id INTEGER primary key, nombre VARCHAR(50))
"""
)

# Aqui comprometemos los cambios, sin eso la consuta no puede ser posible
con.commit()

# Simpre cerramos
con.close()

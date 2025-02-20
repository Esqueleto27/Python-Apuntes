# Aqui vamos a ver como realizar operaciones sin necesidad de estar constantemenete comprometiendo los cambios y cerrando la conexion
# Aqui no ponemos commit y close
#


import sqlite3

# Aqui usamos el operador de with
with sqlite3.connect("10-SQLite/app.db") as con:

    cursor = con.cursor()

    cursor.execute(
        """

    CREATE TABLE if not exists usuarios (id INTEGER primary  key, nombre VARCHAR (50))"""
    )

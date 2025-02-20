# Aqui vamos a ver como insertar multiples valores utilizando SQLite
#

import sqlite3

with sqlite3.connect("10-SQLite/app.db") as con:
    cursor = con.cursor()
    cursor.execute("insert into usuarios values(?, ?)", (1, "Hola mundo"))

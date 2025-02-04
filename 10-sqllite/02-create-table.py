#
import sqlite3

con = sqlite3.connect("10-sqllite/app.db")

# Para generar consultas debemos generar una variable
cursor = con.cursor()
cursor.execute(
    """
CREATE TABLE if not exists usuarios(id INTEGER primary key, nombre VARCHAR(50))
"""
)
con.commit()

# Cerramos
con.close()

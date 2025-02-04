# Este es el modulo que nos va a permitir conectarnos a sqllite
import sqlite3

# generar la conexion con la base de datos
con = sqlite3.connect("10-sqllite/app.db")
# cerrar la conexion
con.close()

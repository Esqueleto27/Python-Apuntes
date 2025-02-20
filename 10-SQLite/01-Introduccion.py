# Algunas base de datos ya vienen ppr defecto en python como es SQLite
# Imporatmos el modulo que nos va a permitir conectarnos a sqllite
import sqlite3

# Creamos la variable "con" que viene de conexion
# Lugo llamamos al metodo de "connect" y luego indicamos la ruta de donde se encuntra almacenado el archvio que va a contener nuestra base da datos
# Si el archivo no existe pyhton lo va a crear
con = sqlite3.connect("10-SQLite/app.db")

# Siempre tenemos que cerrar la conexion
con.close()

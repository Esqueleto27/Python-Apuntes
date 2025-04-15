# =============================================
# SQLite en Python: Crear y Conectar a una Base de Datos
# =============================================

# 📌 Algunas bases de datos ya vienen integradas por defecto en Python.
# Una de ellas es **SQLite**, una base de datos liviana que guarda toda la información en un archivo local.

# 🛠️ Importamos el módulo 'sqlite3', que nos permite trabajar con bases de datos SQLite.
import sqlite3

# 🔌 PASO 1: Crear una conexión a la base de datos
# Creamos una variable llamada 'con', que representa la conexión.
# Usamos el método 'sqlite3.connect()' para conectarnos a la base de datos.
# Si el archivo no existe, Python lo crea automáticamente en la ruta especificada.
con = sqlite3.connect("10-SQLite/app.db")

# 📁 En este ejemplo, 'app.db' es el archivo que contendrá nuestra base de datos.
# Está ubicado en la carpeta '10-SQLite'.

# 🛑 PASO 2: Cerrar la conexión
# Siempre que terminamos de trabajar con la base de datos, es importante cerrar la conexión para liberar recursos.
con.close()

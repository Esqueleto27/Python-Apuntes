# =============================================
# Crear una Tabla en SQLite con Python
# =============================================

# 🧠 Recordatorio: SQLite viene incluido en Python, así que no necesitas instalar nada.
import sqlite3  # 🔁 Importamos el módulo para trabajar con SQLite

# 🔌 PASO 1: Conectarse (o crear) a la base de datos
# El archivo 'app.db' está en la carpeta '10-SQLite'.
# Si no existe, lo crea automáticamente.
con = sqlite3.connect("10-SQLite/app.db")

# 🎯 PASO 2: Crear un cursor
# Un cursor es como un intermediario que permite ejecutar comandos SQL en la base de datos.
cursor = con.cursor()

# 🛠️ PASO 3: Ejecutar una consulta SQL
# Usamos el método 'execute' para enviar instrucciones SQL.
# En este caso: creamos una tabla llamada 'usuarios' si no existe aún.
# La tabla tendrá:
# - una columna 'id' de tipo INTEGER, que será clave primaria (primary key),
# - una columna 'nombre' de tipo VARCHAR de máximo 50 caracteres.
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY,
        nombre VARCHAR(50)
    )
"""
)

# 💾 PASO 4: Confirmar los cambios
# 'commit()' guarda todos los cambios realizados durante la conexión.
con.commit()

# ❌ PASO 5: Cerrar la conexión
con.close()

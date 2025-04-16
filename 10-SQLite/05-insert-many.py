# =============================================
# Insertar registros en SQLite (con múltiples valores)
# =============================================

# 📌 Aquí vamos a insertar datos en la tabla 'usuarios' utilizando SQLite y el bloque 'with'.
# También usamos el símbolo de reemplazo (?) para evitar inyecciones SQL.

import sqlite3  # 🛠️ Importamos el módulo para trabajar con SQLite

# ✅ Usamos 'with' para gestionar automáticamente la conexión
with sqlite3.connect("10-SQLite/app.db") as con:
    cursor = con.cursor()  # Creamos el cursor para ejecutar las consultas

    # 👤 Insertamos un usuario con ID = 1 y nombre = "Hola mundo"
    # Usamos una consulta parametrizada para evitar errores e inyecciones SQL.
    cursor.execute("INSERT INTO usuarios (id, nombre) VALUES (?, ?)", (1, "Hola mundo"))

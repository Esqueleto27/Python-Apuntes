# =============================================
# Consultar datos en SQLite con Python
# =============================================

# 📌 En este ejemplo vamos a consultar datos de la tabla 'usuarios'.
# Usamos 'SELECT * FROM usuarios' para traer todos los registros.

import sqlite3  # 🛠️ Módulo de SQLite

# 🔍 Realizamos la consulta dentro de un bloque 'with' para que la conexión se maneje sola
with sqlite3.connect("10-SQLite/app.db") as con:
    cursor = con.cursor()  # Creamos el cursor para ejecutar la consulta

    # 🧾 Ejecutamos una consulta para obtener todos los registros de la tabla 'usuarios'
    cursor.execute("SELECT * FROM usuarios")

    # 📤 Usamos 'fetchone()' para obtener solo el primer registro encontrado
    resultado = cursor.fetchone()
    print("Primer registro encontrado:", resultado)

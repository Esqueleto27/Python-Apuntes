# =============================================
# Consultar TODOS los registros con SELECT * y fetchall()
# =============================================

import sqlite3  # 🛠️ Módulo de SQLite

# 🔍 Nos conectamos a la base de datos usando 'with' (manejo automático de conexión)
with sqlite3.connect("10-SQLite/app.db") as con:
    cursor = con.cursor()

    # 🧾 Ejecutamos la consulta para obtener todos los registros
    cursor.execute("SELECT * FROM usuarios")

    # 📤 Recuperamos todos los resultados con fetchall()
    registros = cursor.fetchall()

    # 🔁 Recorremos la lista de resultados
    print("Listado de usuarios:")
    for registro in registros:
        print(registro)

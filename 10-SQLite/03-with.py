# =============================================
# Usar el bloque 'with' para manejar conexiones SQLite
# =============================================

# 📌 En este ejemplo vamos a crear una tabla, pero utilizando la instrucción 'with',
# que nos permite gestionar la conexión automáticamente:
# - No hace falta llamar a con.commit()
# - No hace falta cerrar manualmente con.close()
# ¡Todo se hace automáticamente al salir del bloque!

import sqlite3  # 🛠️ Módulo para trabajar con SQLite

# ✅ Usamos 'with' para abrir la conexión. Esto se conoce como "context manager".
# Python se encargará de cerrar la conexión de forma segura cuando salgamos del bloque.
with sqlite3.connect("10-SQLite/app.db") as con:

    # Creamos el cursor como siempre para ejecutar comandos SQL
    cursor = con.cursor()

    # Ejecutamos la consulta para crear la tabla
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY,
            nombre VARCHAR(50)
        )
    """
    )

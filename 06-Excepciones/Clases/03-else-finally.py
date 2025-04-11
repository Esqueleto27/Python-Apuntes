# ---------------------------------------------
# ESTRUCTURA COMPLETA DE MANEJO DE ERRORES
# try - except - else - finally
# ---------------------------------------------

# try: Bloque donde se intenta ejecutar un código que podría fallar.
try:
    # Solicitamos un número al usuario
    n1 = int(input("Ingrese su primer número: "))

# except: Se ejecuta SOLO si ocurre un error en el bloque try.
# Captura cualquier tipo de excepción general.
except Exception as ex:
    print("❌ Ocurrió un error.")
    print(f"Tipo de error: {type(ex).__name__}")
    print(f"Descripción: {ex}")

# else: Se ejecuta SOLO si NO ocurre ningún error en el try.
else:
    print("✅ No ocurrió ningún error. El programa continúa normalmente.")

# finally: Se ejecuta SIEMPRE, ocurra o no un error.
# Ideal para cerrar archivos, liberar recursos, mostrar mensajes finales, etc.
finally:
    print("🔁 Este bloque se ejecuta siempre, sin importar si hubo error o no.")

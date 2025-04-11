# ---------------------------------------------
# EJEMPLO BÁSICO DE MANEJO DE ERRORES
# ---------------------------------------------
# try-except para capturar posibles errores al convertir una entrada a entero
# ---------------------------------------------

try:
    # Solicitamos un número al usuario
    n1 = int(input("Ingrese su primer número: "))

# Capturamos cualquier error que ocurra en el bloque try
except:
    # ❌ No se recomienda usar except sin tipo de error
    # porque captura TODO tipo de error, incluso errores graves
    print("❌ Ocurrió un error al ingresar el número.")

# ---------------------------------------------
# NOTA IMPORTANTE:
# Siempre que sea posible, especifica el tipo de excepción:
# ejemplo: except ValueError, except ZeroDivisionError, etc.
# ---------------------------------------------

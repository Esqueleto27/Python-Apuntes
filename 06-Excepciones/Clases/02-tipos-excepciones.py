# ---------------------------------------------
# MANEJO DE ERRORES EN PYTHON (try - except)
# ---------------------------------------------

# El bloque try nos permite intentar ejecutar código que puede causar errores.
# Si ocurre un error, Python buscará un bloque 'except' que pueda manejarlo.
try:
    # Solicitamos al usuario que ingrese un número
    n1 = int(input("Ingrese su primer número: "))

# ------------------------------------------------------------------
# BLOQUES EXCEPT: Capturan errores específicos que puedan ocurrir.
# ------------------------------------------------------------------

# 1. ValueError: Este error ocurre cuando se proporciona un valor inapropiado.
#    Ejemplo: intentar convertir letras a número con int("abc")
except ValueError as e:
    print("❌ Hubo un error: ingresaste un valor inapropiado.")
    print(f"Detalle del error: {e}")

# 2. NameError: Ocurre cuando tratamos de usar una variable que no ha sido definida.
#    Ejemplo: print(numero) ← si 'numero' no ha sido definido antes
except NameError as e:
    print("❌ Error dentro del código: variable no definida o mal escrita.")
    print(f"Detalle del error: {e}")

# 3. Exception: Este bloque es genérico. Captura cualquier otro tipo de error que no haya sido manejado antes.
#    Se recomienda usarlo como último recurso.
except Exception as ex:
    print("❗ Se ha producido un error inesperado.")
    print(f"Tipo de error: {type(ex)}")
    print(f"Detalle del error: {ex}")

# ---------------------------------------------
# NOTA:
# Siempre empieza por los errores más específicos (como ValueError),
# y termina con 'Exception' como una forma general de atrapar lo que no anticipaste.
# ---------------------------------------------

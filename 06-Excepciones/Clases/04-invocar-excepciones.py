# ---------------------------------------------
# EJEMPLO DE INVOCACIÓN MANUAL DE EXCEPCIONES
# ---------------------------------------------


# Definimos una función que lanza una excepción si se intenta dividir por 0
def division(n=0):
    # Si n es igual a 0, lanzamos manualmente una excepción
    if n == 0:
        # 'raise' se usa para generar una excepción de forma intencional
        raise ZeroDivisionError("❌ No se puede dividir por 0")

    # Si no hay error, hacemos la división normalmente
    return 5 / n


# Probamos la función dentro de un bloque try-except
try:
    division()  # No pasamos ningún valor → usa el valor por defecto n=0

# Capturamos la excepción específica ZeroDivisionError
except ZeroDivisionError as e:
    print(f"Error capturado: {e}")

# Referencia útil para más excepciones:
# https://docs.python.org/3/library/exceptions.html

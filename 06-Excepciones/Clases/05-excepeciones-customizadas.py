# ---------------------------------------------------------
# EXCEPCIONES PERSONALIZADAS EN PYTHON CON CLASES
# ---------------------------------------------------------


# Creamos una clase personalizada de excepción que hereda de 'Exception'
class MiError(Exception):
    """
    Esta clase representa una excepción personalizada.
    Puedes agregarle atributos y comportamiento propio.
    """

    def __init__(self, mensaje, codigo=0):
        self.mensaje = mensaje
        self.codigo = codigo

    # Redefinimos el método __str__ para mostrar el mensaje al imprimir el error
    def __str__(self):
        return f"🚨 Error {self.codigo}: {self.mensaje}"


# Función que lanza la excepción personalizada si el argumento es cero
def division(n=0):
    if n == 0:
        # Lanzamos nuestro error personalizado con un mensaje y un código
        raise MiError("No se puede dividir por 0", codigo=101)

    return 5 / n


# Bloque try para manejar nuestra excepción
try:
    division()  # No se pasa argumento → usa n=0 → lanza MiError

# Capturamos nuestro error personalizado
except MiError as e:
    print("❌ ¡Se capturó una excepción personalizada!")
    print(e)

# ---------------------------------------------------------
# DOCUMENTACIÓN OFICIAL (muy útil para profundizar):
# https://docs.python.org/3/library/exceptions.html
# ---------------------------------------------------------

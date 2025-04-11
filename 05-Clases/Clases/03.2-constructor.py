#


# Definición de una clase
class MiClase:
    # Método especial __init__: Constructor de la clase
    # Se ejecuta automáticamente cuando se crea una instancia de la clase.
    def __init__(self, atributo1, atributo2):
        # Atributos de instancia: Son variables asociadas a cada objeto creado a partir de esta clase.
        self.atributo1 = atributo1  # atributo1 es un atributo de instancia
        self.atributo2 = atributo2  # atributo2 es otro atributo de instancia

    # Método de la clase: Una función que pertenece a la clase y opera sobre una instancia
    def metodo(self):
        # El método retorna un mensaje que incluye los valores de los atributos de la instancia.
        return f"El atributo1 es {self.atributo1} y el atributo2 es {self.atributo2}"


# Crear una instancia de la clase MiClase
mi_objeto = MiClase("valor1", "valor2")
# Aquí "mi_objeto" es una instancia de la clase MiClase con los valores "valor1" y "valor2" para sus atributos.

# Acceso a los atributos de la instancia
print(mi_objeto.atributo1)  # Muestra el valor de atributo1 (Salida: valor1)
print(mi_objeto.atributo2)  # Muestra el valor de atributo2 (Salida: valor2)

# Llamar al método de la clase
print(
    mi_objeto.metodo()
)  # Llama al método metodo() y muestra su resultado (Salida: El atributo1 es valor1 y el atributo2 es valor2)

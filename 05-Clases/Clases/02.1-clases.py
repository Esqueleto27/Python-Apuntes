# Las clases permiten crear estructuras para organizar y reutilizar código, encapsulando datos (atributos) y comportamientos (métodos).

# Clase: Es como un molde o plantilla para crear objetos. Define qué atributos y métodos tendrán los objetos basados en ella.
# Objeto: Es una instancia de una clase. Es como un "producto" hecho a partir del molde de la clase.
# Atributos: Son las variables asociadas a una clase u objeto, que representan sus características.
# Métodos: Son funciones dentro de una clase que definen el comportamiento de los objetos.


# Ejemplo base de clases
class MiClase:
    def __init__(self, atributo1, atributo2):
        self.atributo1 = atributo1  # Atributo del objeto
        self.atributo2 = atributo2

    def metodo(self):  # Ya no es funcion si no, metodo
        return f"El atributo1 es {self.atributo1} y el atributo2 es {self.atributo2}"


# Ejemplo real de clase
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre  # Atributo del objeto
        self.edad = edad 

    def saludar(self):
        return f"Hola, me llamo {self.nombre} y tengo {self.edad} años."


# Crear un objeto Persona
persona1 = Persona("Matheo", 25)
print(persona1.saludar())  # Salida: Hola, me llamo Matheo y tengo 25 años.

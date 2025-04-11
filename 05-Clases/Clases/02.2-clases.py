# Ejemplo base
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre  # Atributo del objeto
        self.edad = edad


# Crear instancias de la clase Persona
persona1 = Persona("Matheo", 25)  # Instancia 1
persona2 = Persona("Carla", 30)  # Instancia 2

# Acceder a los atributos de cada instancia
print(persona1.nombre)  # Salida: Matheo
print(persona2.nombre)  # Salida: Carla


# Ejemplo real


class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre  # Atributo del objeto
        self.edad = edad

    def saludar(self):
        return f"Hola, soy {self.nombre} y tengo {self.edad} años."


persona1 = Persona("Matheo", 25)
persona2 = Persona("Carla", 30)

print(persona1.saludar())  # Salida: Hola, soy Matheo y tengo 25 años.
print(persona2.saludar())  # Salida: Hola, soy Carla y tengo 30 años.

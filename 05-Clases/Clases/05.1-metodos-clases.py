# Clase Perro con propiedades y métodos
class Perro:
    patas = 4  # Propiedad de clase que aplica a todos los perros

    def __init__(self, nombre, edad):
        """
        Constructor de la clase Perro.
        Se utiliza para inicializar las propiedades de instancia (nombre y edad).
        """
        self.nombre = nombre  # Propiedad de instancia (nombre del perro)
        self.edad = edad  # Propiedad de instancia (edad del perro)

    @classmethod
    def habla(cls):
        """
        Método de clase que imprime un mensaje.
        Los métodos de clase están vinculados a la clase, no a instancias específicas.
        """
        print("¡Guau!")  # Mensaje que representa el sonido de un perro

    @classmethod
    def factory(cls):
        """
        Método de clase (factory method) que crea y devuelve una nueva instancia de la clase Perro.
        Este método facilita la creación de objetos con valores predeterminados.
        """
        return cls("Skeletor", 6)  # Crea un perro con nombre "Skeletor" y edad 6


# Llamada al método de clase 'habla'
Perro.habla()  # Salida: ¡Guau!

# Crear instancias de la clase Perro
perro1 = Perro("Skeletor", 2)  # Perro con nombre "Skeletor" y edad 2
perro2 = Perro("Bobi", 5)  # Perro con nombre "Bobi" y edad 5

# Crear un nuevo perro utilizando el método factory
perro3 = Perro.factory()  # Perro con nombre "Skeletor" y edad 6

# Mostrar información de los perros creados
print(f"Perro 1: {perro1.nombre}, {perro1.edad} años")
print(f"Perro 2: {perro2.nombre}, {perro2.edad} años")
print(f"Perro 3: {perro3.nombre}, {perro3.edad} años")

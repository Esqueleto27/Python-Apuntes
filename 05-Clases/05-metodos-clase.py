#


class Perro:
    patas = 4  # Propiedades de clase

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    # Habla es un metodo y para convertirlo en un metodo de clase ponemos: @classmethod
    @classmethod  # Asi creamos un metodo propio de la clase perro
    def habla(
        cls,
    ):  # Que es una convencion cuando creamos metodos de clases para referirnos a la clase misma es como escribir Perro en este caso
        print("Guau!! ")


Perro.habla()

# Ejemplo digamos que nostros queremos crear un perro constanatemente
# Hay una manera mas facil de hacer esto mismo, creando un metodo de clase


perro1 = Perro("Skeletro", 2)
perro2 = Perro("Bobi", 5)


# Vamos a crear una instancia de perro y que la retorne eso se conoce como factory method
@classmethod
def factory(cls):
    return cls("Skeletor", 6)


perro3 = Perro.factory()

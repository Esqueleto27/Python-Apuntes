# Aqui podemos crear propiedades que vna a ser pricvadass que no se van a poder acceder desde fuera


# Clase
class Perro:

    # Constructor
    def __init__(self, nombre, edad):

        # Cuando queramos cambiar el nombre de las propiedades es lo mejor
        # SHIFT + CMD + P (RENAME SYMBOL) cambia el nombre de la propiedad aqui y abajo
        self.__nombre = nombre
        self.edad = edad

    # Creamos un metodo para que nos devuelva el valor de este
    def get_nombre(self):
        return self.__nombre

    # Si quisieramos cambiar el nombre del perro pero queremos validar esto primero
    # para que nos serviria, para ver que no sea string vacio,
    def set_nombre(self, nombre):
        self.__nombre = nombre

    # Metodo
    def habla(self):
        print(f"El {self.__nombre} dice Guau!!")

    # Metodo de clase
    @classmethod
    def factory(cls):
        return cls("Skeletor feliz", 4)


perro1 = Perro.factory()
perro1.habla()
# No podmeos acceder
print(perro1.nombre)
# Si podemos accder
print(perro1.get_nombre)

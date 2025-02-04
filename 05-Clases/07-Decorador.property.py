#


class Perro:
    def __init__(self, nombre):
        self.nombre = nombre

    @property     #SOlo se utiliza con funciones que nos devuelven valor 
    def nombre (self):
        return self.__nombre
    

    def set_nombre(self, nombre):
        if nombre.strip():
            self.__nombre = nombre #Si hacemos privada no podemos acceder 
        return

perro = Perro("Skeletor")
print(perro.)

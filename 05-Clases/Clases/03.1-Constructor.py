# Recapitulacion
# El constructor se tiene que definir con __init__
# Self vendria siendo una instancia
# Luego aprendimos que le podemos pasar valores al contructor en este caso como (nombre, edad)
# Y despues asignarles como propiedades a las instancias de la clase


class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    # Y tambien aprendimos que en los metodos nosotros podemos acceder a estas propiedades haciendo uso de self.(nombre de la propiedad)

    def habla(self):
        print(f"{self.nombre} dice : Guau")


mi_perro = Perro("Bobi", 1)
mi_perro.habla

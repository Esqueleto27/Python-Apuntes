# Diferencias entre propiedades de las clases y de las instacias


class Perro:
    # Tambien nosotors podemos tener una propiedad que se asigne a la clase de perro
    # Tendria que ser algo que tengan todas las instancias de perro
    # Cuando yo acceda a la propiedad me debe devolver el mismo valor
    patas = 4

    def __init__(self, nombre, edad):
        # Propiedades de las instancias y nosotros para crear eso estamos usando la palabra reservada de self.(nombre de la propiedad o atributo)
        self.nombre = nombre
        self.edad = (
            edad  # Edad viene siendo la propiedad o atributo de la instancia dela clase
        )

    def habla(self):
        print(f"{self.nombre} dice : Guau")


# Suposicion cambiamos el valor de patas
Perro.patas = 3

# Instancias de perro
mi_perro = Perro("Bobi", 1)
mi_perro2 = Perro("Maxi", 1)


# Primera opcion
print(Perro.patas)
print(mi_perro.patas)

# Segunda opcion

class Persona:
    # CLASE: Este es el molde llamado 'Persona'. Define cómo se comportan sus objetos.

    def __init__(self, nombre, edad):
        # CONSTRUCTOR: Este método especial se ejecuta automáticamente
        # cuando creamos una instancia de la clase.

        self.nombre = nombre  # PROPIEDAD: 'nombre' es un atributo del objeto.
        self.edad = edad  # PROPIEDAD: 'edad' es otro atributo del objeto.

    def saludar(self):
        # MÉTODO: Es una función que pertenece a la clase.
        # En este caso, retorna un mensaje que incluye las propiedades del objeto.
        return f"Hola, me llamo {self.nombre} y tengo {self.edad} años."


# Crear un objeto Persona
persona1 = Persona("Matheo", 25)
# INSTANCIA: 'persona1' es un objeto creado a partir de la clase 'Persona'.
# Los argumentos "Matheo" y 25 se pasan al constructor (__init__).

print(persona1.saludar())  # MÉTODO LLAMADO: Llama al método 'saludar' en la instancia.

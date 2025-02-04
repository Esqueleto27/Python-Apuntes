class Perro:  # Creamos la clase llamada Perro y esta debe de estar siempre con UpperCamelCase

    # Aqui agregamos todas las funciones y variables que se encuentren asociadas a la clase de Perro

    # Dejan de llamarse funciones a llamarse metodos y los metodos son funciones dentro de una clase
    def habla(self):  # Y siempre el primer parametro debe de ser self
        print("Guau")


# Usamos la mayuscula para saber que estamos llamando a una clase y no confundirnos con una funcion
Perro()

# Creamos una instancia de una clase
mi_perro = Perro()  # Asignamos a una variabble a la clase de perro

# Ahora imprimimos el tipo de la varibale
print(type(mi_perro))  # Main es el modulo de la instancia de perro

# Si nosotros queremos llamar al modulo de habla
mi_perro.habla()  # No tenemos que pasar ningun argumento porque el argumento de self ya lo pasa automaticamente, solo tenemos que preocuparnos de pasarle otro argumento si es que antes le pasamos otro argumento ademas self en la definicion de metodo

# podemos verificar si este objeto que hemos creado es una instancia de alguna en particular
print(
    isinstance(mi_perro, Perro)
)  # Si este objeto es una instancia de una clase de mi perro (True)

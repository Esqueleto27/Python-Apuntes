# Vamos a hacer una funcion para saludar

def saludo_curso():  # def es la funcion y lo que le sigue es el nombre de que asignamos a la funcion
    print("********************************")  # Cuerpo de la funcion
    print("***Bienvenido al curso***")


def saludo_persona(nombre, apellido):  # (nombre) parametro
    print(f"Nombre: {nombre} {apellido}")  # uso del parametro


saludo_curso()  # argumento
saludo_persona("Matheo", "Flores")  # argumento

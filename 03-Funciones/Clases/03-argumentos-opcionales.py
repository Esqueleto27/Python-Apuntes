# Esto sirve cuando no tenemos un argumento y se pone algo por default

def saludo_curso():  # def es la funcion y lo que le sigue es el nombre de que asignamos a la funcion
    print("********************************")  # Cuerpo de la funcion
    print("***Bienvenido al curso***")


def saludo_persona(nombre="Sin nombre", apellido="Sin apellido"):  # (nombre) parametro
    print(f"Nombre: {nombre} {apellido}")  # uso del parametro


saludo_curso()  # argumento
saludo_persona("Matheo", "Flores")  # argumento
saludo_persona("Nicolas")

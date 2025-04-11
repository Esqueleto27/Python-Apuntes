# Para nombrar argumentos especificamente

def saludo_curso():  # def es la funcion y lo que le sigue es el nombre de que asignamos a la funcion
    print("********************************")  # Cuerpo de la funcion
    print("***Bienvenido al curso***")


def saludo_persona(nombre="Sin nombre", apellido="Sin apellido"):  # (nombre) parametro
    print(f"Nombre: {nombre} {apellido}")  # uso del parametro


saludo_curso()  # argumento
saludo_persona("Matheo", "Flores")  # argumento
saludo_persona("Nicolas")  # Pone automaticamente sin apellido

# Ejm: En la linea 15 se pone automaticamente el primer string en nombre y si ponemos primero el apellido, estaria mal
saludo_persona("Flores", "Matheo")
# Aqui especificamos cual es el apellido y caul es el nombre
saludo_persona(apellido="Solano", nombre="David")

# keyboard arguments que es una forma de empauetar todods los parametros

def get_product(**datos):  # Funcion no es parametro porque estamos usando kwargs
    print(datos["id"], datos["nombre"])


# Aqui asignamos los parametros y los argumentos
get_product(id="id", nombre="iphone", argumento="es un iphone 16 pro")

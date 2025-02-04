#
mascotas = [
    "pablito",
    "miche",
    "blanca",
    "luna",
    "miche"
]

mascotas.insert(1, "Negra")  # para insertar un elemento en la lista
mascotas.append("michesss")  # agregar al final

# Maneras de eliminar
mascotas.remove("miche")  # Para eliminar y solo elimina el primer elemento
mascotas.pop(1)  # para eliminar por indice
del mascotas[1]
mascotas.clear()  # Para eliminar todo
print(mascotas)

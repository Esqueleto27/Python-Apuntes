# Sets que significa grupo o conjuntos
# Es una coleccion de datos que no se puede repetir y tampoco eesta ordenada
# Los sets siemopre se guardan entre {}


primer = {1, 1, 2, 2, 3, 4}
primer.add(5)  # Añadimos un elemento
primer.remove(1)  # Eliminamos un elemento si no hay lanza error
primer.discard(6)  # Elminamos un elemento pero si no hay no lanza error

print(primer)

# Vamos a convertir una lista en un set
segundo = [3, 4, 5]
segundo = set(segundo)

# Operadores interesantes dentro de python
# | Union
print(primer | segundo)  # Va a juntar las dos y no va agregar los repetidos

# & Interseccion
print(primer & segundo)  # Solo nos va a devolver los elementos que se repetian

# - Diferencia
# Eliminamos los elementos del segundo set en el primer set
print(primer - segundo)

# Para ordenar listas

numeros = [3, 15, 17, 5, 1, 18]

# Primera manera de ordenar
numeros.sort()
print(numeros)
# Segunda manera de ordenar pero creando otra lista
lista_nueva = sorted(numeros)
print(lista_nueva)

# Al reves
numeros.sort(reverse=True)
print(numeros)

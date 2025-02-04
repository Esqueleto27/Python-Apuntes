# Se refiere a

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

primero = numeros[0]
segundo = numeros[1]
tercero = numeros[2]
print(numeros)
print(primero)

# Segunda manera

# first, second, third = numeros
first, *otros, ultimo = numeros
print(first, otros, ultimo)

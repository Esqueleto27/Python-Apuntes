# Y que pasaria si queremos agregar varios argumentos o menos argumentos y en los parametros se excede o falta
# Manera de agregar tantos argumentos como queramos


def suma(*numeros):  # tranforma a nustros parametros en iterables
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)


suma(2, 5, 7)
suma(8, 9, 8, 7)

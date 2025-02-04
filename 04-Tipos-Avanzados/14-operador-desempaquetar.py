lista = [1, 2, 3, 4]
print(*lista)

lista2 = [5, 6]

combinada = ["Lista combinada"*lista, *lista2]
print(combinada)

# Crear  un diccionrio en un diccionario
dic1 = {"g": 66}
dic2 = {"j": 77}

dic = {**dic1, **dic2}
print(dic)

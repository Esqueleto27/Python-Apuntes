#

casa = [
    [4, "Diego"],
    [2, "Matheo"],
    [8, "Oscar"],
    [6, "Sebas"]
]

casa.sort()
print(casa)


amigos = [
    ["Alejandro", 4],
    ["Kevin", 8],
    ["Nicolas", 2],
    ["Carlos", 6]
]


def ordena(elemento):
    return elemento[1]


amigos.sort(key=ordena)  # ,reverse=True
print(amigos)

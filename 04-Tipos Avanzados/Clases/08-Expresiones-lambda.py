# Funciones ambiguas

amigos = [
    ["Alejandro", 4],
    ["Kevin", 8],
    ["Nicolas", 2],
    ["Carlos", 6]
]


def ordena(elemento):
    return elemento[1]


amigos.sort(key=lambda elemento: elemento[1])  # ,reverse=True
print(amigos)

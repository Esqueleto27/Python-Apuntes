# Vamos a pasar de usuarios a nombres

usuarios = [
    ["Alejandro", 4],
    ["Kevin", 8],
    ["Nicolas", 2],
    ["Carlos", 6]
]

# Primera manera
nombres = []  # Aqui creamos una lista vacia
for usuario in usuarios:
    nombres.append(usuario[0])
print(nombres)


# Segunda manera mas elegante #map
# names =[expresion for item in items]

usuario = [usuario[1] for usuario in usuarios]

usuario = [usuario for usuario in usuarios if usuario[1] > 2]

print(nombres)

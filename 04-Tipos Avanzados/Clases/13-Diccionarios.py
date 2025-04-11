# Los diccionarios son los conjuntos mas usados en python
# Son una colecion de datos que se encuntran agrupados por una llave y un valor

punto = {"x": 25, "y": 50}
print("Lista", punto)
print("Valor de x", punto["x"])
print("Valor de y", punto["y"])

punto["z"] = 45  # Añadimos un caracter a la lista
print("Agregamos z", punto)

# Para encontrar un carcater
if "a" in punto:
    print("Encontre a", punto["a"])

# Para acceder a un valor de un diccionario
print("Otra manera de obtener datos")
print(punto.get("x"))
print(punto.get("u", 97))

# Eliminamos el valor de y
del punto["y"]
print("Eliminamos y", punto)

#
for valor in punto:
    print("Valor", valor, punto[valor])

# obtener duplas
for valor in punto.items():
    print("Dupla", valor)

# Ejemplo
usuarios = [
    {"id": 1, "nombre": "Matheo"},
    {"id": 2, "nombre": "David"},
    {"id": 3, "nombre": "Kevin"},
    {"id": 4, "nombre": "Nicolas"},
]

for usuario in usuarios:
    print(usuario["nombre"])

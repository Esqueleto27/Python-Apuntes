animal = "   Chanchito   FELIZ"

# Para poner mayusculas
print("Mayusculas")
print(animal.upper())

# Para poner en minusculas
print("Minusculas")
print(animal.lower())

# Primera letra en mayuscula
print("Primera letra en mayuscula")
print(animal.capitalize())

# Cada primera letra en mayusculas
print("Cada primera letra en mayusculas")
print(animal.title())

# Borra los espacios del inicio y final
print("Borra los espacios")
print(animal.strip())

# Borra los espacios en la mitad
# print("Borra los espacios dela mitad")
# print(animal.replace())

# Buscar letra el indice(primera letra ubi)
print("Buscar letra ubi")
print(animal.find("ito"))

# Remplazar
print("Remplaza letras")
print(animal.replace("Chanch", "cul"))

# Boolean
print("o verdadero o falso")
print("ito" in animal)

# Boolean
print("o verdadero o falso")
print("ito" not in animal)

# Juntamos 2
print("Juntamos 2,boora espacio, primera mayucula")
print(animal.strip().capitalize())

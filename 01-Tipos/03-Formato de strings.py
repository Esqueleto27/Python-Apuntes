# El formato de strings en Python se refiere a la forma de insertar valores dentro de una cadena de texto (string) de manera dinámica
nombre = "Matheo"
apellido = "Flores"

# 1.(Basica)
print(nombre, apellido)

# 2.(Concatenación básica usando el operador + )
nombre_completo = nombre + " " + apellido

# 3.(String literal)
print("EL nombre completo es:  ", nombre, apellido)

# 4.(f-strings)
nombre_completo = f"{nombre} {apellido}"
print(nombre_completo)

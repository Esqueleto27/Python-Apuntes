# Acceder a los elementos de un listado
gatos = ["Miche", "Pablito", "Blanca", "Negra", "Luna"]
print("EL gato mas lindo es:", gatos[1])

# Cambiamos un elemento de un listado
gatos[1] = "Pablito precioso"

# Sleccionamos caules vamos a imprimir
print("Los gatos del Diego son: ",  gatos[2:5])

# Vamos un elemento 1 por 1
print(gatos[::2])


# Numeros pares y hacemos que se salte de 2 en 2
numeros = list(range(21))
print(numeros[::2])

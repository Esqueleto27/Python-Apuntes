# For else

buscar = int(input("Ingrese el numero a buscar: "))

for numero in range(5):
    print(numero)
    if numero == buscar:
        print("Se encontro su numero", buscar)
        break
else:
    print("No se encontros")

n1 = input("Ingrese primer numero")
n2 = input("Ingrese primer numero")

n1 = int(n1)
n2 = int(n2)

suma = n1 + n2
resta = n1 - n2
multiplicacion = n1 * n2
div = n1 / n2

mensaje = f"""
Para los numeros {n1} y {n2},
suma {suma}.
resta {resta}.
multi {multiplicacion}.
div {div}.
"""
print(mensaje)

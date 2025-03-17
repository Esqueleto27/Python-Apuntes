# Calculadora de cambio

print("***Ayudamos a calcular su cambio***")
producto = int(input("Ingrese el valor del producto: "))
dinero = int(input("Ingrese cuanto dinero le dio: "))

resultado = dinero - producto
if producto > dinero:
    print("Le falta dinero")
else:
    print(f"Su cambio es: {resultado}")
    

# Para prevenir posibles errores

try:
    n1 = int(input("Ingre su primer numero: "))

# Vamos a ingresar a esta parte del coidgo siempre que ocurra un error arriba
except Exception as ex:
    print("ingrese un valor que corresponda")
except NameError as ex:
    print("Hubo un error en el codigo")

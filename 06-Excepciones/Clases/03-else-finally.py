# Para prevenir posibles errores

try:
    n1 = int(input("Ingre su primer numero: "))

# Vamos a ingresar a esta parte del coidgo siempre que ocurra un error arriba
except Exception as ex:
    print("Ocurrio un error")
else:
    print("No ocorrio ningun error")
finally:
    print("se ejecuta simepre! ")

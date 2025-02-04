# and cuando tengamos 2 condiciones, las dos tienen que ser true para que todo sea true
# En este ejemplo tanto la calificacion como la asistencia se tienen que cumplir, para pasar
calificacion = int(input("Ingrese su calificacion final:  "))
asistencia = int(input("Ingrese su asistencia final:  "))

if calificacion >= 7 and asistencia < 5:
    print("Aprobo")
else:
    print("Reprobo")


# or cuando tengamos 2 condiciones, basta con que una sea true para que todo sea true
# En este ejemplo si cualquiera de las 2 es verdadero, es porque la pantalla esta encedida

teclas_prendidas = True
pantalla_encendida = False

if teclas_prendidas or pantalla_encendida:
    print("La computadora esta prendida")

# not se usa para cabiar el valor Ejm:si es True, lo convierte a False
# En este ejemplo
tengo_llaves = False

if not tengo_llaves:
    print("No tienes las llaves. ¡No olvides llevarlas!")
else:
    print("Ya tienes las llaves. Puedes salir.")

# Ahora un ejemplo de todos

gas = True
encendido = True
edad = 18
# if not gas and (encendido or edad > 17)
if gas and (encendido and edad) > 17:
    print("Puedes avanzar")
else:
    print("No puedes avanzar")

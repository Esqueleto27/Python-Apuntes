# String signifca una secuencia de caracteres, que se utiliza para almacenar y manipular texto
nombre_juego = ("Call of Duty")

# Aqui usamos las triple comillas para texto largo
descripcion_juego = """
Call of Duty es una popular franquicia de videojuegos de disparos en primera persona
Ambientada en distintos escenarios de guerra
se destaca por su acción intensa, realismo, y modos multijugador competitivos.
"""

# La funcion de len sirve para obtener la longitud de un string
print(len(nombre_juego))

# Va a aparecer la primera letra del valor de la varible C
print(nombre_juego[0])

# Va a imprimir la letra desde la 0(C) hasta la 3(l) Call
print(nombre_juego[8:12])

# Si dejamos sin completar va a poner la letra desde donde pusimos hasta el final
print(nombre_juego[6:])

# Va a imprimir todo el valor de la variable
print(nombre_juego[:])

# Función para convertir a segundos
def a_segundos(cantidad, unidad):
    if unidad == "segundo" or unidad == "segundos":
        return cantidad
    elif unidad == "minuto" or unidad == "minutos":
        return cantidad * 60
    elif unidad == "hora" or unidad == "horas":
        return cantidad * 3600
    elif unidad == "día" or unidad == "días":
        return cantidad * 86400
    else:
        return "Error"

# Función para convertir de segundos


def de_segundos(cantidad, unidad):
    if unidad == "segundo" or unidad == "segundos":
        return cantidad
    elif unidad == "minuto" or unidad == "minutos":
        return cantidad / 60
    elif unidad == "hora" or unidad == "horas":
        return cantidad / 3600
    elif unidad == "día" or unidad == "días":
        return cantidad / 86400
    else:
        return "Error"

# Función principal para convertir entre unidades de tiempo


def convertir_tiempo(cantidad, unidad_origen, unidad_destino):
    cantidad_en_segundos = a_segundos(cantidad, unidad_origen)

    if cantidad_en_segundos == "Error":
        return "Unidad de tiempo no válida"

    cantidad_convertida = de_segundos(cantidad_en_segundos, unidad_destino)

    if cantidad_convertida == "Error":
        return "Unidad de tiempo no válida"

    return f"{cantidad} {unidad_origen}(s) son {cantidad_convertida:.2f} {unidad_destino}(s)"


# Ejemplo de uso
print(convertir_tiempo(2, 'hora', 'minuto'))

# Importamos los módulos necesarios
import datetime  # Para trabajar con fechas y horas

# Creamos dos fechas específicas
fecha1 = datetime.datetime(2023, 1, 1)
fecha2 = datetime.datetime(2023, 2, 1)

# Calculamos la diferencia entre las dos fechas
delta = fecha2 - fecha1

# Mostramos la diferencia
print("Diferencia entre las fechas:", delta)  # Nos muestra la diferencia en días

# Usamos timedelta para sumar y restar días

# Sumar 10 días a fecha1
nuevo_fecha = fecha1 + datetime.timedelta(days=10)
print("Fecha 1 + 10 días:", nuevo_fecha)

# Restar 5 días a fecha2
fecha2_resta = fecha2 - datetime.timedelta(days=5)
print("Fecha 2 - 5 días:", fecha2_resta)

# También podemos sumar o restar horas, minutos, etc.
# Sumar 2 horas a fecha1
fecha_mas_2horas = fecha1 + datetime.timedelta(hours=2)
print("Fecha 1 + 2 horas:", fecha_mas_2horas)

# Restar 30 minutos a fecha2
fecha_menos_30min = fecha2 - datetime.timedelta(minutes=30)
print("Fecha 2 - 30 minutos:", fecha_menos_30min)

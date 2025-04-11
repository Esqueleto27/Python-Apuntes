import time  # Importamos el módulo time para trabajar con el tiempo

# Muestra el número de segundos desde el 1 de enero de 1970 (Epoch time) hasta ahora.
print(
    time.time()
)  # Nos devuelve la cantidad de segundos que han pasado desde la "época Unix" (1970)

# Para convertirlo a hora UTC o con una zona horaria específica, necesitamos hacer más pasos,
# ya que time.time() solo devuelve el valor en segundos.

# Ahora importamos datetime para trabajar con fechas más fácilmente
import datetime

# Crear una fecha específica (1 de enero de 2023)
fecha = datetime.datetime(2023, 1, 1)
print(fecha)  # Imprime la fecha que creamos

# Forma más fácil de obtener la fecha y hora actual
ahora = (
    datetime.datetime.now()
)  # Usamos datetime.now() para obtener la fecha y hora actuales
print(ahora)  # Imprime la fecha y hora actuales

# Si necesitas convertir el tiempo de UTC a Ecuador (que está en UTC -5), puedes usar:
utc_time = datetime.datetime.utcnow()  # Obtiene el tiempo UTC
ecuador_time = utc_time - datetime.timedelta(
    hours=5
)  # Resta 5 horas para obtener la hora de Ecuador
print("Hora en Ecuador:", ecuador_time)

# https://docs.python.org/3/library/datetime.html

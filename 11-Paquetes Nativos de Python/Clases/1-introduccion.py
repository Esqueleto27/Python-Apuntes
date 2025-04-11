# Importamos paquetes nativos de Python
import math  # Para funciones matemáticas
import datetime  # Para trabajar con fechas y horas
import random  # Para generar números aleatorios
import os  # Para interactuar con el sistema operativo
import json  # Para trabajar con datos en formato JSON

# Usando math: calcular la raíz cuadrada de 16
print("Raíz cuadrada de 16:", math.sqrt(16))

# Usando datetime: obtener la fecha y hora actual
ahora = datetime.datetime.now()
print("Fecha y hora actual:", ahora)

# Usando random: generar un número aleatorio entre 1 y 10
print("Número aleatorio entre 1 y 10:", random.randint(1, 10))

# Usando os: obtener el directorio actual
print("Directorio actual:", os.getcwd())

# Usando json: convertir un diccionario a formato JSON
persona = {"nombre": "Matheo", "edad": 25}
persona_json = json.dumps(persona)
print("Diccionario en formato JSON:", persona_json)

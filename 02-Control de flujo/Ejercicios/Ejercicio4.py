import random

# Solicitar al usuario cuántas veces quiere lanzar el dado
num_lanzamientos = int(input("¿Cuántas veces deseas lanzar el dado? "))

# Inicializar un diccionario para contar las frecuencias de cada cara
frecuencias = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

# Simular los lanzamientos
for _ in range(num_lanzamientos):
    cara = random.randint(1, 6)  # Generar un número aleatorio entre 1 y 6
    frecuencias[cara] += 1

# Calcular y mostrar la frecuencia porcentual de cada cara
print("\nFrecuencia porcentual de cada cara:")
for cara, cuenta in frecuencias.items():
    porcentaje = (cuenta / num_lanzamientos) * 100
    print(f"Cara {cara}: {porcentaje:.2f}% ({cuenta} veces)")

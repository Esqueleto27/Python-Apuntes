# Aqui vamos a ver el modulo de random

# Importamos el modulo
import random

# Devuelve un número flotante aleatorio entre 0.0 y 1.0.
print(random.random())  # Ejemplo: 0.6345

# Devuelve un entero aleatorio entre a y b
print(random.randint(1, 10))  # Ejemplo: 7

# Devuelve un número decimal (float) entre a y b
print(random.uniform(1, 5))  # Ejemplo: 3.27

# Devuelve un elemento aleatorio de una lista (o cualquier secuencia)
frutas = ["manzana", "pera", "banana"]
print(random.choice(frutas))  # Ejemplo: 'banana'

# Devuelve una lista de n elementos aleatorios con posibilidad de repetirse
print(random.choices(frutas, k=2))  # Ejemplo: ['pera', 'pera']

# Devuelve n elementos aleatorios sin repetición
print(random.sample(frutas, k=2))  # Ejemplo: ['banana', 'pera']

# Mezcla (desordena) los elementos de la lista en el mismo lugar (no retorna nada)
cartas = [1, 2, 3, 4, 5]
random.shuffle(cartas)
print(cartas)  # Ejemplo: [3, 5, 1, 2, 4]

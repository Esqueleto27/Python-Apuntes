# 🎲 Módulo random: para generar valores aleatorios
import random

# ✅ 1. random.random() → Número decimal aleatorio entre 0 y 1
print("Número decimal aleatorio entre 0 y 1:", random.random())

# ✅ 2. random.randint(a, b) → Número entero aleatorio entre 'a' y 'b' (incluye ambos)
print("Número entero aleatorio entre 1 y 10:", random.randint(1, 10))

# ✅ 3. random.shuffle(lista) → Desordena una lista (modifica la original)
lista = [1, 2, 3, 4, 45, 6, 78, 89, 4]
random.shuffle(lista)
print("Lista desordenada:", lista)

# ✅ 4. random.choice(lista) → Elige un elemento aleatorio de una lista
lista2 = [1, 2, 3, 4, 455, 6, 7, 78, 4]
print("Elemento aleatorio de lista2:", random.choice(lista2))

# ✅ 5. random.choices(lista, k=n) → Elige 'k' elementos aleatorios con repetición
print("3 elementos aleatorios con repetición:", random.choices(lista2, k=3))

# ✅ 6. Simulación simple: elegir aleatoriamente un producto para comprar
comprar = ["Audífonos", "Celular", "Mouse", "Teclado", "Monitor"]
producto_elegido = random.choice(comprar)
print("🛒 Producto elegido para comprar:", producto_elegido)

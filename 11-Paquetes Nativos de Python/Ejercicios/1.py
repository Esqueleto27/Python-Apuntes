# Generador de contraseña
# 🔐 Generador de contraseñas aleatorias
import string  # Para obtener letras y dígitos
import random  # Para seleccionar elementos al azar

# ✅ 1. Caracteres que usaremos: letras (mayúsculas + minúsculas) y dígitos
chars = string.ascii_letters  # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
digitos = string.digits  # 0123456789

# ✅ 2. Unimos todos los caracteres posibles
caracteres_posibles = chars + digitos

# ✅ 3. Generamos una contraseña aleatoria de 10 caracteres
# Puedes cambiar el valor de k si quieres más o menos caracteres
seleccion = random.choices(caracteres_posibles, k=10)

# ✅ 4. Convertimos la lista de caracteres en un string
contrasena = "".join(seleccion)

# ✅ 5. Mostramos la contraseña generada
print("🔐 Contraseña generada:", contrasena)

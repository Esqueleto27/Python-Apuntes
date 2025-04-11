# Razones:
# Quiero abrir un navegador web automáticamente desde mi script en Python.
# Ejemplo: estoy haciendo una app en producción o un web scraper, y cuando
# se detecta un producto o resultado, quiero que se abra una página.

import webbrowser  # Módulo nativo para interactuar con el navegador

# Simulación de que encontré un producto
print("Producto encontrado")

# Abrir una página web en una pestaña del navegador predeterminado
webbrowser.open(
    "https://www.youtube.com"
)  # Sirve para abrir una URL en una nueva pestaña

# También puedes abrir una nueva ventana (depende del navegador)
webbrowser.open_new(
    "https://www.google.com"
)  # Sirve para abrir una URL en una nueva ventana

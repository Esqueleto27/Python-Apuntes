# Variables de entorno

# Supongamos que vamos a crear una cuenta en SendGrid.
# SendGrid nos va a enviar una API Key para poder usar su servicio.
# Es importante recordar que la API Key es una especie de contraseña que te permite interactuar con el servicio de SendGrid de manera segura.
# En lugar de colocar la API Key directamente en el código, es mejor usar variables de entorno para evitar exponerla.

# Supongamos que tienes una clave de API de SendGrid como esta (NO uses esta clave en producción):
SENGRID_API_KEY = "ASDFGH"  # Este es un ejemplo de cómo se podría guardar la clave de API de SendGrid en el código (aunque NO es recomendable).

# **¡Advertencia!** Si subimos este código a un repositorio público como GitHub, cualquier persona podrá ver esta clave y usarla. Esto sería muy riesgoso, ya que podría permitir a otras personas hacer uso indebido de tu cuenta.

# Para evitar esto, lo mejor es guardar la clave de API en un archivo `.env` que no se suba al repositorio.

# **Paso 1: Crear un archivo `.env`**
# Creamos un archivo llamado `.env` en el mismo directorio donde está nuestro archivo Python. Este archivo contendrá nuestras variables de entorno.

# Contenido del archivo `.env` (NO lo subas a GitHub):
# .env
# SENGRID_API_KEY="ASDFGH"  # Aquí guardas tu API Key de SendGrid de manera segura.

# **Paso 2: Usar la clave de API de manera segura en tu código**
# En lugar de escribir la clave directamente en el código, vamos a leerla desde el archivo `.env`.

# Para hacer esto, puedes usar el paquete `python-dotenv` para cargar las variables de entorno desde el archivo `.env` en tu código.

# Primero, instala `python-dotenv` con el siguiente comando en tu terminal:
# pip install python-dotenv

# Luego, en tu código Python, agrega las siguientes líneas para cargar las variables de entorno:
import os
from dotenv import (
    load_dotenv,
)  # Importamos 'load_dotenv' para cargar las variables de entorno desde el archivo '.env'.

load_dotenv()  # Carga las variables del archivo '.env'.

apikey = os.environ.get(
    "SENGRID_API_KEY"
)  # Ahora obtenemos la clave de API de SendGrid desde la variable de entorno.

print(
    apikey
)  # Imprime la API Key para asegurarnos de que se cargó correctamente desde el archivo '.env'.

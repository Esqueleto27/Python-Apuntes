# Para mandar mensajes de texto a los usuarios
# Descargamos a traves de la consola (pipenv install twilio)

import os
import twilio.rest import Client
sid= os.environ.get("TWILIO_TOKEN")

cliente = Client(sid, token)
mensaje =cliente.messages.com
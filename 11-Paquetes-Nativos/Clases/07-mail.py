# Importamos las librerías necesarias

import smtplib  # Para conectarse al servidor SMTP y enviar correos electrónicos

from email.mime.multipart import (
    MIMEMultipart,
)  # Para crear un mensaje que pueda incluir varios elementos (texto, imagen, etc.)
from email.mime.text import (
    MIMEText,
)  # Para crear y adjuntar texto plano (sin formato HTML)
from email.mime.image import MIMEImage  # Para adjuntar imágenes al correo

from pathlib import (
    Path,
)  # Para trabajar con rutas de archivos de forma flexible y multiplataforma

# Obtenemos la imagen desde la misma carpeta del archivo
path = Path(
    "/Users/matheoflores/Documents/Programacion/HolaMundo/Python/Apuntes/11-Paquetes-Nativos/Clases/imagen.jpg"
)
# Ruta relativa a la imagen
mime_image = MIMEImage(
    path.read_bytes()
)  # Leemos la imagen y la convertimos a un objeto MIME para enviarlo por correo

# Opcional: darle un nombre a la imagen adjunta
mime_image.add_header("Content-Disposition", "attachment", filename="imagen.jpg")

# Configuración del servidor de Gmail
smtp_host = "smtp.gmail.com"  # Servidor SMTP de Gmail
smtp_puerto = 587  # Puerto para conexión segura STARTTLS

# Credenciales del remitente
usuario = "matheofloresloor@gmail.com"
contraseña = "lhvj kxwb guim hjpg"  # Contraseña de aplicación

# Creamos el mensaje
mensaje = MIMEMultipart()  # Creamos un contenedor para el correo
mensaje["From"] = "Matheo <matheofloresloor@gmail.com>"  # Nombre y correo del remitente
mensaje["To"] = "nicobelick55@gmail.com"  # Correo del destinatario
mensaje["Subject"] = "Correo con imagen desde Python"  # Asunto del correo

# Creamos el cuerpo del mensaje
cuerpo = MIMEText(
    "Nico eres mi hijo jsjsj gg NO BRIM ",
)  # Texto plano sin HTML

mensaje.attach(cuerpo)  # Adjuntamos el texto al mensaje
mensaje.attach(mime_image)  # Adjuntamos la imagen

# Enviamos el correo
try:
    with smtplib.SMTP(
        smtp_host, smtp_puerto
    ) as smtp:  # Nos conectamos al servidor SMTP de Gmail
        smtp.ehlo()  # Iniciamos la conexión
        smtp.starttls()  # Activamos la conexión segura
        smtp.login(usuario, contraseña)  # Iniciamos sesión en Gmail
        smtp.send_message(mensaje)  # Enviamos el mensaje
        print("✅ Correo enviado correctamente con la imagen adjunta.")
except Exception as e:
    print("❌ Ocurrió un error al enviar el correo:", e)

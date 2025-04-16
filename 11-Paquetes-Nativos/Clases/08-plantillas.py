import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
import string

plantilla = """<b>Hola!!! $usuario</b>"""

# Usamos string.Template para crear el mensaje personalizado
template = string.Template(plantilla)
cuerpo = MIMEText(template.substitute(usuario="Matheo"), "html")

path = Path(
    "/Users/matheoflores/Documents/Programacion/HolaMundo/Python/Apuntes/11-Paquetes-Nativos/Clases/imagen.jpg"
)
mime_image = MIMEImage(path.read_bytes())
mime_image.add_header("Content-Disposition", "attachment", filename="imagen.jpg")

smtp_host = "smtp.gmail.com"
smtp_puerto = 587

usuario = "matheofloresloor@gmail.com"
contraseña = "lhvj kxwb guim hjpg"

mensaje = MIMEMultipart()
mensaje["From"] = "Matheo <matheofloresloor@gmail.com>"
mensaje["To"] = "nicobelick55@gmail.com"
mensaje["Subject"] = "Correo con imagen desde Python"

# Ponemos que es el cuerpo
mensaje.attach(cuerpo)
mensaje.attach(mime_image)

try:
    with smtplib.SMTP(smtp_host, smtp_puerto) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(usuario, contraseña)
        smtp.send_message(mensaje)
        print("✅ Correo enviado correctamente con la imagen adjunta.")
except Exception as e:
    print("❌ Ocurrió un error al enviar el correo:", e)

from twilio.rest import Client

# Sustituye con tus credenciales de Twilio
account_sid = "TU_ACCOUNT_SID"
auth_token = "TU_AUTH_TOKEN"
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_="whatsapp:+14155238886",  # Número de Twilio (sandbox)
    body="Hola, este mensaje es automático desde Twilio y Python 🚀",
    to="whatsapp:+593TU_NUMERO",  # Tu número con código de país
)

print("Mensaje enviado con SID:", message.sid)

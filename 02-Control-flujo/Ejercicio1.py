# Verificacion de tweets

tweet = input("Ingrese su tweet: ")
if not tweet:
    print("vacio")
elif len(tweet) > 20:
    print("Exceso de caracteres")
else:
    print("Se ha publicado correctamente")

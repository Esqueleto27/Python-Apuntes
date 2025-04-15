# 📦 Usamos sys para recibir argumentos desde la terminal
import sys
import os  # Para trabajar con archivos

# ✅ Mostramos los argumentos que llegan desde la terminal
print("📥 Argumentos recibidos:", sys.argv)


# ✅ Función principal que maneja los argumentos
def cli(args):
    # Si no se pasan argumentos adicionales
    if len(args) == 1:
        print("⚠️ No se pasaron argumentos.")
        return

    # Si no se pasan exactamente 2 argumentos además del nombre del script
    if len(args) != 3:
        print(
            "⚠️ Se necesitan exactamente 2 argumentos: <archivo_origen> <nuevo_nombre>"
        )
        return

    archivo_origen = args[1]
    nuevo_nombre = args[2]

    # ✅ Comprobamos si el archivo existe
    if not os.path.exists(archivo_origen):
        print(f"❌ El archivo '{archivo_origen}' no existe.")
        return

    # ✅ Renombramos el archivo
    os.rename(archivo_origen, nuevo_nombre)
    print(f"✅ Archivo renombrado de '{archivo_origen}' a '{nuevo_nombre}'")


# ✅ Ejecutamos la función con los argumentos de la terminal
cli(sys.argv)

# Inyección de Dependencias en Python

# Sin Inyección de Dependencias:
# La función depende de una implementación específica (usuario).
import usuario


def guardar_sin_inyeccion():
    # Aquí se depende directamente de la clase/función 'guardar' del módulo 'usuario'
    usuario.guardar()


# Con Inyección de Dependencias:
def guardar_con_inyeccion(entidad):
    # Aquí se pasa la entidad con el método 'guardar' como parámetro
    entidad.guardar()


# Ejemplo de uso:
class Usuario:
    def guardar(self):
        print("Guardando usuario...")


class Producto:
    def guardar(self):
        print("Guardando producto...")


# Crear instancias de las clases
usuario_obj = Usuario()
producto_obj = Producto()

# Usar la función con inyección de dependencias
guardar_con_inyeccion(usuario_obj)  # Salida: Guardando usuario...
guardar_con_inyeccion(producto_obj)  # Salida: Guardando producto...

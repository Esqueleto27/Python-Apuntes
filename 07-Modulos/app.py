# Para poder importar codigo de otro lado de nuestra pc

from usuarios.acciones import saludo, despedida

saludo()
despedida()

# Otra manera
from usuarios import acciones

acciones.saludo()


# Otra manera pero mas tediosa

import usuarios.acciones

usuarios.acciones.saludo()

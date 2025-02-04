# Aplicar descuento

def aplicar_descuento(total_cuenta, porcentaje_descuento):
    descuento = total_cuenta * (porcentaje_descuento / 100)
    total_con_descuento = total_cuenta - descuento
    return total_con_descuento


total = 1000
descuento = 20

total_final = aplicar_descuento(total, descuento)
print(f"El total después del descuento es: {total_final}")

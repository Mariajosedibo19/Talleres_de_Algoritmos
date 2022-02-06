"""
Datos de entrada
Cantidad de galones = g = float


Datos de salida
Valor a pagar por el concepto de gasolina = f

"""
# Entradas

g=float(input("Inserte la cantidad de galones que dispenso en la venta "))


# Caja Negra
f= (g*3.785)*50_000 # Conversion de galones a litros para luego multiplicar por el valor de cada litro (50000) y asi hallar el total a pagar.

# Salidas
print("Valor a pagar por el cliente, por el concepto de gasolina es de ",f )

"""
Datos de entrada
Precio final pagado por un producto = pf = int
Precio de venta al publico = pvp = int



Datos de salida
Porcentaje de descuento  = t = int

"""
# Entradas
pf=int(input("Inserte el precio final pagado por un producto "))
pvp=int(input("Inserte el precio de venta al publico "))


# Caja Negra
a=(pvp-pf) # Diferencia entre el precio el pvp y el precio final pagado por un producto.
b=(a/pvp)*100 # El descuento realizado dividido en el precio final ( que hace referencia al precio full al cual se debia vender determinado producto ...)

# Salidas
print ("Porcentaje de descuento que le ha sido aplicado es el : ",b ,"%" )
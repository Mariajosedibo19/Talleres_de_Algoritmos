"""
Datos de entrada
    Valor de la compra total sin descuento = c = int

Datos de salida
El precio final a pagar = t = int

"""
# Entradas
c=int(input("Inserte el valor total de su compra "))


# Caja Negra
d=(c*0.15) # El valor del descuento es del 15% sobre el valor de la compra
t=(c-d) # El valor que debera pagar como precio final(Incluyendo el descuento) el usuario

# Salidas
print("El precio final que debera pagar es de ",t ) 

	
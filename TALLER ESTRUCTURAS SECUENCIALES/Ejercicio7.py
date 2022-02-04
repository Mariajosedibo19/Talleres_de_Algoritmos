"""
Datos de entrada
cantidad de metros que va a convertir = m = int

Datos de Salida
La conversion de a pies es de = f = float
La conversion de a pulgadas es de = p = float
"""
# Entradas
m=int(input(" Introduzca la cantidad en metros que va a convertir "))

# Caja Negra
p= m*39.27 # la cantidad en metros convertida a pulgadas/ 1 metro = 39.27 inch (Se hace con ayuda de la regla de tres)
f= p/12 # la cantidad en metros convertida a pies / 1 pie = 12 inch / Se sigue usando la regla de tres

# Salidas
print(" La conversion de metros a pies es de  ",f ) 
print(" La conversion de metros a pulgadas es de  ", p ) 
"""
Datos de entrada
 El sueldo base = s = int
Venta No. 1= v1= int
Venta No.2 = v2= int

Datos de salida
La comision que ganara por las 3 ventas es del 10% = c = float
El total que recibira el empleado incluyendo su salario y su comision de ventas t = float

"""
# Entradas
s=int(input("Inserte su sueldo base "))
v1=int(input("Inserte el valor de su venta No. 1"))
v2=int(input("Inserte el valor de su venta No. 2"))
v3=int(input("Inserte el valor de su venta No. 3"))

# Caja Negra
v=(v1+v2+v3) #La suma de las 3 ventas que realizo en el mes
c=(v*0.1) #La comision que ganara por las 3 ventas es del 10%
t=(s+c) # El total que recibira el empleado incluyendo su salario y su comision de ventas

# Salidas
print("La comision extra a pagar por sus ventas es de : ", c) 
print("El total de dinero que recibira en el mes tomando sueldo base + comisiones es de : ", t) 
	

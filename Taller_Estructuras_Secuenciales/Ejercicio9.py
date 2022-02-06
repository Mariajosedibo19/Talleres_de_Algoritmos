"""
Datos de entrada
Pago por hora trabajada = p = int
cantidad de horas trabajadas = h = int
Datos de Salida
El salario neto de un trabajador = sn = int

"""
# Entradas
p=int(input(" Introduzca la cantidad que le pagan por hora trabajada "))
h=int(input(" Introduzca la cantidad de horas trabajadas "))
# Caja Negra
pa=p*h  # Corresponde al pago que obtendra de acuerdo a las horas trabajadas
d=pa*0.2 # Corresponde al descuento fijo al sueldo base por un 20%
sn=pa-d # Corresponde al salario neto (En donde ya esta aplicado el descuento del 20 % por el concepto de impuestos)
# Salidas
print(" El salario neto que recibira usted sera  ",sn ) 

"""
Datos de entrada
Su nombre = n = int
Numero de horas normales trabajadas = hn = int
Pago por hora normal trabajada = p = int 
Cantidad de horas extras trabajadas = he = int

Datos de salida
Las asignaciones son = a = int
Las deducciones son = d = int
El sueldo neto del trabajador = sn= int

"""
# Entradas
n=str(input("Inserte su nombre "))
hn=int(input("Numero de horas normales trabajadas "))
p=float(input("Pago por hora normal trabajada "))
he=int(input("Cantidad de horas extras trabajadas "))
x=int(input("Inserte la cantidad de hijos "))

# Caja Negra
sb=p*(hn)
a=(250000+173000*(x)+180000)# Son las asignaciones 
de=sb*(0.14) # Deduccion /Descuento del 14% sobre el sueldo base 
d=sb-de # salario del trabajador con los descuentos aplicados
ce=(p*he)# Pago por las horas extras trabajadas sin el 15% adicional
cx=(ce*0.25)+ce # Pago por las horas extras trabajadas incluyendo el 15% adicional
sn=(a+d+cx) # Corresponde al sueldo neto que recibira
# Salidas
print(" Las asignaciones son de   ", a)
print(" Las deducciones son de    ", de)
print(f" El Sueldo neto que recibira {n} en el mes de diciembre es de : {sn}")
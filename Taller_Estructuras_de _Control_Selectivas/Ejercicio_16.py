"""
Datos de entrada

valor para A en la formula cuadratica = a= float
valor para B en la formula cuadratica = b = float
valor para C en la formula cuadratica = c = float


Datos de salida
Resultado de la ecuacion = A X**2 +BX + C =0

"""
# Entradas



a=float(input("valor para A en la formula cuadratica "))
b=float(input("valor para B en la formula cuadratica "))
c=float(input("valor para C en la formula cuadratica "))  

# Caja Negra

from cmath import sqrt
x1=(-b-sqrt(b**2-4*a*c))/(2*a)
x2=(-b+sqrt(b**2-4*a*c))/(2*a)
discriminante=b**2-4*a*c # discriminante
solucion=""
if (discriminante==0):
    solucion= -b/(2*a) # Tiene 1 solucion real 
elif (discriminante>0):
    solucion= x1,x2 
elif (discriminante<0):
    solucion= "No tiene solucion en los reales"

# Salidas
print(f" La solucion o soluciones de la ecuacion de segundo grado son {solucion}")


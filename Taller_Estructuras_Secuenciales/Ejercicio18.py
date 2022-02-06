"""
Datos de entrada
Cantidad de Bolivares prestados = x = int
Cantidad de intereses pagados en los 4 años = y = int


Datos de salida
Porcentaje anual de intereses  = pa = int

"""
# Entradas
x=int(input("Cantidad de Bolivares prestados "))
y=int(input("Cantidad de intereses pagados en 4 años "))


# Caja Negra 

r= ((y*100)/(x*4)) # Despues de tener la formula de interes , se despejo la razon , para hallar el porcentaje de interese cobrados durante los cuatro años. 
p=r/4 # se divide la razon en los 4 años para hallar el porciento ( la razon ) anual cobrada por intereses.


# Salidas
print(" El Porcentaje anual de intereses que usted pago durante los 4 años fue de : ", p ," % ")
"""
Entradas
Capital que va a invertir = i = int
Meses transcurridos despues de un mes de haber invertido = m = int
Razon de pago mensual (2% = 0.02) por parte del banco  = r = float 
Salida
Dinero ganado despues de un mes de invertir = int
"""
# Entradas 
i=int(input("Ingrese el monto a invertir "))
m=int(input("Ingrese la cantidad de meses a los cuales quiere proyectar su inversion "))
# Caja Negra
g=i*(0.02*m) # Representa la ganancia real ( No incluye el valor invertido)que tendra la persona luego de haber invertido el dinero
t=i+g #representa el monto total que tendra por cada mes teniendo en cuenta la cant. de dinero que haya invertido
print("La ganancia que tendra usted luego de haber invertido es de ",g)
print("El monto final que tendra usted luego de haber invertido es de ",t)

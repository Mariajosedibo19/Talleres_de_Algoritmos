"""
Datos de entrada
Lectura anterior kw = lv = int
Lectura actual en kw = la = int
Costo por kilovatio = c = float


Datos de salida
Monto total pago recibo de luz = t = int

"""
# Entradas
lv=int(input("Inserte la lectura anterior de kivolatios usados "))
la=int(input("Inserte la lectura actual de kivolatios usados "))
c=float(input("Inserte el costo por kilovatio "))

# Caja Negra
f=abs(la-lv)*c # Resta entre la lectura actual y la anterior para determinar el consumo real de kw usados multimplicado por el costo por kw
# Salidas
print(" Monto final que debera pagar para el recibo de luz ", f)

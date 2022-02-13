"""
Datos de entrada
Lectura anterior kw = lv = int
Lectura actual en kw = la = int


Datos de salida
Monto total pago recibo de luz = t = int

"""
# Entradas
lv=int(input("Inserte la lectura anterior de kivolatios usados "))
la=int(input("Inserte la lectura actual de kivolatios usados "))
consumo=abs(la-lv) #Resta entre la lectura actual y la anterior para determinar el consumo real de kw usados 


# Caja Negra
monto_pagar=''
if(consumo>=0)or(consumo<=100):
    monto_pagar=(consumo*4600) # se multiplica el consumo por el valor del kw , para ese rango de consumo
elif(consumo>=101)or(consumo<=300):
    monto_pagar=(consumo*80.00)
elif(consumo>=301)or(consumo<=500):
    monto_pagar=(consumo*100_000)
elif(consumo>=501):
    monto_pagar=(consumo*120_000)

# Salidas

print(f" Monto final que debera pagar por el consumo de luz electrica y aseo urbano es de : {monto_pagar}")



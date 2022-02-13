"""
Datos de entrada

Distancia recorrida en kilometros = x = int


Datos de salida

Pago que debe realizar el cliente = pago_cliente  = int


"""
# Entradas
x=int(input( "Inserte la distancia recorrida por usten en kilometros : "))


# Caja Negra 
d=(x-1000)# representa los kilometros adicionales que se cobraran despues de los 1000 km 

Precio=''
if (x<= 300):
    precio= 50_000
elif(x>300 and x<1000):
    precio= (70_000+(30000*(x-300))) # se cobra 30000 demas por cada km superior a 300 km
elif(x>1000):
    precio= ((150_000+(9000*(d)))+(((x-d)-300)*30000)) # Se cobra 9000 por cada km adicional despues de los 1000 km /se cobra 30000 demas por cada km superior a 300 km

# Salidas 
print(f" El Pago que debe realizar el cliente es de ${precio}")


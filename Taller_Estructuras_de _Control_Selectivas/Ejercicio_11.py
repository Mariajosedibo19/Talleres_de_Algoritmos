"""
Datos de entrada

Temperatura = t = float

Datos de salida
Deporte = d = str

"""
# Entradas

t=float(input(" Digite temperatura "))

# Caja Negra 

deporte= ''
if(t>85 and t< 120):
    deporte= "Natacion "
elif(t>70 and t<= 85 ):
    deporte= "Tenis "
elif(t>32 and t<= 70 ):
    deporte = "Golf "
elif(t>10 and t<= 32 ):
    deporte = "Esqui "
elif(t>=0 and t<= 10 ):
    deporte = "Marcha "
else:
    deporte= "No hay ningun deporte a practicar"
# Datos de Salida

print(f"El deporte apropiado para practicar es : {deporte} ")

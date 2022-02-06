"""
Datos de entrada
Presupuesto anual del hospital = p = int 



Datos de salida
Presupuesto que recibira el area de Ginecologia = pg = int
Presupuesto que recibira el area de Traumatologia = pt = int
Presupuesto que recibira el area de Pediatria  = pp = int
"""
# Entradas
p=int(input(" Inserte el presupuesto anual del hospital  "))


# Caja Negra
g=p*0.4  # Presuesto por el 40% para determinar la cant. de dinero que le corresponde a ginecologia
tp=p*0.3 # Presupuesto por el 30% que le corresponde a traumatologia y pediatria

# Salidas
print (" El Presupuesto que recibira el area de Ginecologia ", g )
print (" El Presupuesto que recibira el area de Traumatologia ", tp )
print (" El Presupuesto que recibira el area de Pediatria ", tp )

"""
Datos de entrada
Primera calificacion parcial= a = int
Segunda calificacion parcial = b = int
Tercera calificacion parcial = c = int 
Nota de su examen final= d = int
Calificacion de su trabajo final= e = int

Datos de salida
La calificacion final en la materia de algoritmos sera de = nf = int
"""
# Entradas
a=int(input("Inserte su Primera calificacion parcial "))
b=int(input("Inserte su Segunda calificacion parcial "))
c=int(input("Inserte su Tercera calificacion parcial "))
d=int(input("Nota de su examen final "))
e=int(input("Calificacion de su trabajo final "))
# Caja Negra
p=((a+b+c)/3) # el promedio de las tres calificaciones parciales
nf=((p*0.55)+(d*0.30)+(e*0.15)) #La comision que ganara por las 3 ventas es del 10%

# Salidas
print(" La calificacion final en la materia de algoritmos sera de  ", nf) 
	
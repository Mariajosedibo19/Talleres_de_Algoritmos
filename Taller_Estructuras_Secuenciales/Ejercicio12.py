"""
Datos de entrada
Primera tarea de matematicas = pm = float
Segunda tarea de matematicas = sm = float
Tercera tarea de matematicas = tm = float
Examen matematicas = em= float

Primera tarea de fisica = pf = float
Segunda tarea de fisica = sf = float
examen fisica = ef = float

Primera tarea de Quimica = pq = float
Segunda tarea de Quimica = sq = float
Tercera tarea de Quimica = tq = float
examen quimica = eq = float

Datos de salida
promedio general de las tres materias = pg= float
Promedio en matematicas = m = float
Promedio en fisica  = f = float
Promedio en Quimica = q = float

"""
# Entradas
pm=float(input("Inserte su primera nota tarea de matematicas "))
sm=float(input("Inserte su segunda nota tarea de matematicas"))
tm=float(input("Inserte su tercera nota tarea de matematicas"))
em=float(input("Nota examen de matematicas"))
pf=float(input("Inserte su primera nota tarea de fisica"))
sf=float(input("Inserte su segunda nota tarea de fisica"))
ef=float(input("Nota examen de fisica"))
pq=float(input("Inserte su primera nota tarea de quimica"))
sq=float(input("Inserte su segunda nota tarea de quimica "))
tq=float(input("Inserte su tercera nota tarea de quimica"))
eq=float(input("Nota examen de quimica"))
# Caja Negra
mt=(((pm+sm+tm)/3)*0.1)+em*(0.9)# Promedio general de matematicas
fs=(((pf+sf)/2)*0.2)+ef*(0.8) # Promedio general de fisica
qu=(((pq+sq+tq)/3)*0.15)+eq*(0.85) # Promedio general de quimica
pg=((mt+fs+qu)/3)
# Salidas
print("El promedio general de las tres materias ", pg )
print(" El Promedio de la materia de matematicas  ", mt )
print(" El Promedio de la materia de fisica", fs )
print(" El Promedio de la materia de quimica", qu )
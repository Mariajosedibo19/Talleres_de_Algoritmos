"""
Datos de entrada
Cantidad billetes de 50000 = n1 = int
Cantidad billetes de 20000 = n2 = int
Cantidad billetes de 10000 = n3 = int
Cantidad billetes de 5000 = n4 = int
Cantidad billetes de 2000 = n5 = int
Cantidad billetes de 1000 = n6 = int
Cantidad billetes de 500 = n7 = int
Cantidad billetes de 100 = n8 = int

Datos de salida
La cantidad de dinero que hay en un banco es de = t = int

"""
# Entradas
n1=int(input("Cantidad billetes de 50000 "))
n2=int(input("Cantidad billetes de 20000 "))
n3=int(input("Cantidad billetes de 10000 "))
n4=int(input("Cantidad billetes de 5000 "))
n5=int(input("Cantidad billetes de 2000 "))
n6=int(input("Cantidad billetes de 1000 "))
n7=int(input("Cantidad billetes de 500 "))
n8=int(input("Cantidad billetes de 100 "))
# Caja Negra
t=((n1*50000)+(n2*20000)+(n3*10000)+(n4*5000)+(n5*2000)+(n6*1000)+(n7*500)+(n8*100))
# Salidas
print(" La cantidad de dinero que hay en un banco es de  ", t)

"""
Datos de entrada

dato 1 = a = int
dato 2 = b = int
dato 3 = c = int
dato 4 = d = int


Datos de salida
Resultado de las operaciones planteadas = r = int


"""
# Entradas
a=int(input( "Inserte un numero entero que represente a : "))
b=int(input( "Inserte un numero entero que represente b : "))
c=int(input( "Inserte un numero entero que represente c : "))
d=int(input( "Inserte un numero entero que represente d : "))


# Caja Negra 

if int(d < 1 and d > -1): # La condicion dice que d sea menor a 1 o mayor a -1 , solo se toman los enteros
# Salidas
    print(f"El resultado de la siguiente operacion es de :{(a-c)**2}") 
elif(d>0):
    print(f"El resultado de la siguiente operacion es de : {((a-b)**3)/d}")
    

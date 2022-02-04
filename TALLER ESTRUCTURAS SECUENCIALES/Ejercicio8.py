"""
Datos de entrada
Longitud primer lado triangulo = p = float
Longitud segundo lado triangulo = s = float
Longitud tercer lado triangulo = t = float

Datos de salida
El area del triangulo = a = float

"""
# Entradas
a=int(input("Inserte la Longitud del primer lado del triangulo "))
b=int(input("Inserte la Longitud del segundo lado del triangulo"))
c=int(input("Inserte la Longitud del tercer lado del triangulo"))


# Caja Negra
sp=((a+b+c)/2) # La formula del semiperimetro : sumar los tres lados y dividirlos sobre 2
e=((sp*(sp-a)*(sp-b)*(sp-c))**0.5) 


# Salidas
print("El area del triangulo",e )

	

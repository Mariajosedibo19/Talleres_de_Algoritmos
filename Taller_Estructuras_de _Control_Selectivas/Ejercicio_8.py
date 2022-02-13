"""
Datos de entrada

Primer valor entero = p = int
Segundo valor entero = q = int


Datos de salida

Caso afirmativo = " Los valores de p y q satisfacen la expresion "
Caso Negativo = " Los valores de p y q no satisfacen la expresion "


"""
# Entradas
p=int(input( "Inserte el valor que le dara a P : "))
q=int(input( "Inserte el valor que le dara a Q : "))


# Caja Negra 
resultado=''
if ((p**3 + q**4 - 2*p**2) > 680):
    resultado=(f"Los valores de P: {p} y Q :{q} satisfacen la expresion ")
else:
    resultado=(f"Los valores de P :{p} y Q :{q} no satisfacen la expresion ")

# Salidas 
print(f"{resultado}")



"""
Datos de entrada

monto total de la compra = monto_total =int



Datos de salida
Cantidad a invertir fondos empresa = fondos_empresa = int
Cantidad a pagar a credito = cant_credito = int
Cantidad a pagar por intereses = cant_int = int
Cantidad prestada por el banco = cant_banco = int


"""
# Entradas
monto_total=int(input( "Inserte el monto total de la compra : "))

# Caja Negra 

# Operaciones para cuando la compra excede de $ 5_000_000
fe = (monto_total*0.55) # 55% paga empresa recursos propios
b= (monto_total*0.3) # 30% Banco 
cf=(monto_total*0.15) # 15% credito fabricante 
i=(cf*0.2) #{intereses del 20% sobre la cantidad prestada}


# Operaciones para cuando la compra no excede de $ 5_000_000
sa= (monto_total*0.7) # 70% paga empresa recursos propios
ba=(monto_total*0.30) # 30% credito fabricante
intereses= (ba*0.2) # Sobre el 30% credito al fabricante{intereses del 20% sobre la cantidad prestada}

# Salidas 
if (monto_total > 5_000_000):
    print(f" La Cantidad a invertir de los fondos empresa es :{fe} ")
    print(f" La Cantidad a pagar a credito es de :{b+cf} ")
    print(f" La Cantidad a pagar por intereses es de : {i}")
    print(f" La cantidad prestada por el banco es de : {b}")
else:
    print(f" La Cantidad a invertir de los fondos empresa es :{sa} ")
    print(f" La Cantidad a pagar a credito al fabricante es de : {ba}")
    print(f" La Cantidad a pagar por intereses es de :{intereses}")
    print(f" En este caso el banco no le presta ninguna cantidad a la empresa ")
    

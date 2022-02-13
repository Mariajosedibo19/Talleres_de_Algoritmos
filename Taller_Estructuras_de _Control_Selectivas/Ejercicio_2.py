"""
Datos de entrada

Sueldo de un trabajador = sueldo = int



Datos de salida
Sueldo final que tendra el trabajador = sueldo_final = int


"""
# Entradas

sueldo= int(input(" Digite su sueldo "))

# Caja Negra 

if (sueldo < 900_000):

    # Datos de Salida
    print(f"El sueldo final de usted sera de :{(sueldo*0.15)+sueldo}")
else:
    print(f"El sueldo final de usted sera de : {(sueldo*0.12)+sueldo}")
    

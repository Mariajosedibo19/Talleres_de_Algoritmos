"""
Datos de entrada

categoria = cat = int
sueldo bruto trabajador = sueldo_bruto =int

Datos de salida
Aumento correspondiente segun el sueldo y la categoria = d = str

"""
# Entradas

cat=int(input(" Digite su categoria "))
sueldo_bruto=int(input(" Digite su salario bruto "))
# Caja Negra 

#AUMENTO QUE TENDRA EL EMPLEADO DE ACUERDO A SU SALARIO
aumento= ''
if(cat==1 and sueldo_bruto== 5_000_000):
    aumento=(sueldo_bruto*0.10)
elif(cat==2 and sueldo_bruto==4_300_000 ):
    aumento= (sueldo_bruto*0.15)
elif(cat==3 and sueldo_bruto== 3_600_000):
    aumento=(sueldo_bruto*0.20)
elif(cat==4 and sueldo_bruto== 2_000_000):
    aumento = (sueldo_bruto*0.40)
elif(cat==5 and sueldo_bruto== 900_000):
    aumento = (sueldo_bruto*0.60)
else:
    aumento= "No hay ningun aumento a aplicar "

# NUEVO SUELDO BRUTO
nuevo_sueldo=''
if(cat==1 and sueldo_bruto== 5_000_000):
    nuevo_sueldo=((sueldo_bruto*0.10)+sueldo_bruto)
elif(cat==2 and sueldo_bruto==4_300_000 ):
    nuevo_sueldo= ((sueldo_bruto*0.15)+sueldo_bruto)
elif(cat==3 and sueldo_bruto== 3_600_000):
    nuevo_sueldo=((sueldo_bruto*0.20)+sueldo_bruto)
elif(cat==4 and sueldo_bruto== 2_000_000):
    nuevo_sueldo = ((sueldo_bruto*0.40)+sueldo_bruto)
elif(cat==5 and sueldo_bruto== 900_000):
    nuevo_sueldo = ((sueldo_bruto*0.60)+sueldo_bruto)
else:
    nuevo_sueldo= (f" El sueldo se mantendra igual {sueldo_bruto} ")

# Datos de Salida
print(f"La categoria del trabajador es {cat}, el aumento que tendra sera de {aumento} y su nuevo sueldo bruto sera de {nuevo_sueldo} ")



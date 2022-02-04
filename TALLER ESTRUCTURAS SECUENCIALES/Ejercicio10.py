"""
Datos de entrada
Chelines austriacos = ca = int
Dracmas Griegos = dg= int
Pesetas = p = int

Datos de salida
equivalente de chelines en pesetas = pe = float
equivalente de Dracmas Griegos en franco frances = ff = float
equivalente de pesetas en dolares = d = float
equivalente de pesetas en liras italianas = li = float

"""
# Entradas
ca=int(input(" Inserte la cantidad de chelines Austriacos a convertir en pesetas  "))
dg=int(input("Inserte la cantidad de Dracmas Griegos a convertir en franco frances "))
p=int(input("Inserte la cantidad de pesetas a convertir en dolares y liras italianas"))


# Caja Negra
cp=(ca*9568.71) # La conversion de chelines a pesetas / 1 chelin austriaco equivale a 9568.71 pesetas
df=((dg*8860.7)/20110) # La conversion de Dracmas a francos , teniendo en cuenta / 1dg equivale a 8860.7 y 1 franco equivale a 20110 pesetas
pd=(p*0.00000816) # La conversion de pesetas a dolares / 1 peseta equivale a 0.00000816 dolares
pl=(p/92.89) # La conversion de peseta a liras italianas / 1 lira equivale a 92.89 pesetas

# Salidas
print("El equivalente de chelines a pesetas ", cp) 
print("El equivalente de dragmas griegos a francos ", df) 
print("El equivalente de pesetas a dolares ", pd) 
print("El equivalente de pesetas a liras italianas ", pl) 
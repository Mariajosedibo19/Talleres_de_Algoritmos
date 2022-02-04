"""
# Datos de entrada
numero de mujeres = m = int
numero de hombres = h = int


# Datos de Salida
porcentaje hombres = ph = float
porcentaje mujeres = pm = float
"""
# Entradas
m=int(input("Ingrese cantidad de mujeres"))
h=int(input("Ingrese cantidad de hombres"))
# Caja Negra
total=h+m
ph=(h/total)*100
pm=(m/total)*100
print("El porcentaje de mujeres es",pm)
print("El porcentaje de hombres es" , ph)
print(f"El porcentaje de hombre es :{int(ph)} % " )
print(f"El porcentaje de hombre es : "+str(int(pm))+"%")
"""
Datos de entrada
Cantidad de naranjas  = x = int
Precio por la docena de naranjas = y =int
Precio en el que vendio las naranjas a los detallistas = k= int


Datos de salida
Porcentaje de ganancia ontenido en la inversion  = pa = int

"""
# Entradas
x=int(input("Inserte la Cantidad de naranjas compradas "))
y=int(input(" Inserte el Precio por la docena de naranjas "))
k=int(input(" Inserte el Precio en el que vendio las naranjas a los detallistas "))


# Caja Negra 
inv=((x*y)/12) # Precio en el que el mayorista compro las naranjas al agricultor
g=(((k-inv)*100)/inv) # Porcentaje de ganancia obtenido en la inversion 



# Salidas
print("El Porcentaje de ganancia obtenido en la inversion es del ", g ," % ")

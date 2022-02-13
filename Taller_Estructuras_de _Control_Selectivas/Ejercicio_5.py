"""
Datos de entrada

Ventas departamento No 1 en el mes = venta_primer =int
Ventas departamento No 2 en el mes = venta_segun = int
Ventas departamento No 3 en el mes = venta_ter = int


Datos de salida
Comision que recibiran cada uno de los empleados del departamento No 1 en el mes = com_primer = int
Comision que recibiran cada uno de los empleados del departamento No 2 en el mes = com_segun  = int
Comision que recibiran cada uno de los empleados del departamento No 3 en el mes = com_ter  = int


"""
# Entradas
venta_primer=int(input( "Inserte las Ventas que obtuvo el departamento No 1 en el mes : "))
venta_segun=int(input( "Inserte las Ventas que obtuvo el departamento No 2 en el mes : "))
venta_ter=int(input( "Inserte las Ventas que obtuvo el departamento No 3 en el mes: "))
sueldo_empleados=int(input(" Inserte el salario que tienen los empleados ")) # Todos los empleados ganan lo mismo

# Caja Negra 

# Operaciones para cuando la compra excede de $ 5_000_000
s = ((venta_primer + venta_segun + venta_ter)*0.33) # Total de ventas en el mes con el 0.33 que deben exceder los departamentos para ganar la comision

e=(sueldo_empleados*0.2)# al SUELDO DE EMPLEADOS se le saca la COMISION DEL 20 % 
sf=(e+sueldo_empleados) #al SUELDO DE EMPLEADOS se le suma la  COMISION DEL 20 % de su salario
 # SUELDO DE EMPLEADOS MAS LA COMISION DEL 20 % , si cumplen el requisito

# Salidas 

if (venta_primer > s):
    
    print(f" Comision que recibiran cada uno de los empleados del departamento No 1 en el mes es de :{e} , por lo tanto su sueldo final es de {sf} ")
else:

    print(f" Los empleados del departamento 1 no recibiran comision , recibiran su salario normal : {sueldo_empleados} ")

if(venta_segun > s):

    print(f" La Comision que recibiran cada uno de los empleados del departamento No 2 en el mes es de :{e}, por lo tanto su sueldo final es de {sf} ")
else:

    print(f"Los empleados del departamento 2 no recibiran comision , recibiran su salario normal : {sueldo_empleados} ")

if(venta_ter > s ):

    print(f" La Comision que recibiran cada uno de los empleados del departamento No 3 en el mes es de {e} , por lo tanto su sueldo final es de : {sf} ")

else:
    print(f"Los empleados del departamento 3 no recibiran comision , recibiran su salario normal : {sueldo_empleados} ")

   

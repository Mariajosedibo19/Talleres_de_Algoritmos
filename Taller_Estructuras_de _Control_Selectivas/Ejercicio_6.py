"""
Datos de entrada
Variable A = a = int
Variable B = b = int
Variable C = c = int
Variable D = d = int

Datos de salida
Resultado redondeado = r = int


"""
# Entradas

a =int(input( "Inserte el digito que sera A "))
b =int(input( "Inserte el digito que sera B "))
c =int(input( "Inserte el digito que sera C "))
d =int(input( "Inserte el digito que sera D "))


# Caja Negra 

t= a,b+1 # si b es menor a cinco y c es mayor o igual a cinco
f= a,b # si b y c son menores a 5
o= a+1 # Si b y c son mayores a 5
n=int(str(a)+str(b)+str(c)+str(d)) 
#(b<5 and c>=5):
#t=((b+1)and(c,d==0)) 
#f=((a+1) and (b,c,d==0))
#a=(f{a},{b+1},"0 0")

# Salidas 
print(f"El numero entero a redondear es el siguiente : {n}")
if b<5 and c>=5:
    print(f"El resultado redondeado sera de : {t}00")
elif b<5 and c<5:
            print(f"El resultado redondeado sera de : {f} 00")
else:
        print(f"El resultado redondeado sera de : {o}000")




    

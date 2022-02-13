"""
Datos de entrada

La fecha de nacimiento = t = float

Datos de salida
Nombre signo del Zodiaco
Edad


"""
#Entradas
fecha_nacimiento=input("Digite en este formato 'dd/mm,yy : ")
day,month,year = fecha_nacimiento.split("/")
dia_nacimiento=int(day)
mes_nacimiento=int(month)
año_nacimiento =int(year)

# Caja Negra 

import datetime
x = datetime.datetime.now() # Hora de la maquina
mes_actual = int(x.strftime("%m"))
año_actual = int(x.strftime("%Y"))
dia_actual = int(x.strftime("%d"))
edad=(año_actual-año_nacimiento)



signo=""
if ((mes_nacimiento==11) and (dia_nacimiento>=22)) or ((mes_nacimiento==12) and (dia_nacimiento<=21)):
    signo=("Su signo zodiacal es Sagitario ")
if ((mes_nacimiento==12) and (dia_nacimiento>=22)) or ((mes_nacimiento==1) and (dia_nacimiento<=20)):
    signo=("Su signo zodiacal es Capricornio ")
if ((mes_nacimiento==1) and (dia_nacimiento>=21)) or ((mes_nacimiento==2) and (dia_nacimiento<=19)):
    signo=("Su signo zodiacal es Acuario ")
if ((mes_nacimiento==2) and (dia_nacimiento>=20)) or ((mes_nacimiento==3) and (dia_nacimiento<=19)):
    signo=("Su signo zodiacal es Piscis ") 
if ((mes_nacimiento==3) and (dia_nacimiento>=21)) or ((mes_nacimiento==4) and (dia_nacimiento<=20)):
    signo=("Su signo zodiacal es Aries ")
if ((mes_nacimiento==4) and (dia_nacimiento>=21)) or ((mes_nacimiento==5) and (dia_nacimiento<=21)):
    signo=("Su signo zodiacal es Tauro ")
if ((mes_nacimiento==5) and (dia_nacimiento>=22)) or ((mes_nacimiento==6) and (dia_nacimiento<=21)):
    signo=("Su signo zodiacal es Geminis ")
if ((mes_nacimiento==6) and (dia_nacimiento>=22)) or ((mes_nacimiento==7) and (dia_nacimiento<=22)):
    signo=("Su signo zodiacal es Cancer ")
if ((mes_nacimiento==7) and (dia_nacimiento>=23)) or ((mes_nacimiento==8) and (dia_nacimiento<=23)):
    signo=("Su signo zodiacal es Leo ")
if ((mes_nacimiento==8) and (dia_nacimiento>=24)) or ((mes_nacimiento==9) and (dia_nacimiento<=22)):
    signo=("Su signo zodiacal es Virgo ")
if ((mes_nacimiento==9) and (dia_nacimiento>=23)) or ((mes_nacimiento==10) and (dia_nacimiento<=22)):
    signo=("Su signo zodiacal es Libra ")
if ((mes_nacimiento==10) and (dia_nacimiento>=23)) or ((mes_nacimiento==11) and (dia_nacimiento<=21)):
    signo=("Su signo zodiacal es Escorpion ")

# Datos de Salida

print(f" Su signo del Zodiaco es {signo} ")
print(f" Su edad es de :{edad} años ")

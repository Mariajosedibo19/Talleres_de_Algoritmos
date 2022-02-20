""""
XP= VALOR Experiencia del jugador
exp = valor incremento monsytuos

"""

# Entradas
x=int(input(" Incremento experiencia monstruos "))
m=int(input(" Valor experiencia monstruos "))

#   Caja Negra 
while(0<x<=3): 
    if (10<=m<=(2**32)-1) and (0<x<=3):
        incremento=m*x
        print(incremento)
    elif x==0 and m==0:
        break 

         





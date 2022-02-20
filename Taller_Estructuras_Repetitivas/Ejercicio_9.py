
#Entradas
alcool=0
diesel=0
gasoline=0


while True:
    numero=int(input())
    if numero==1:
        alcool=alcool+1
    elif numero==2:
        gasoline=gasoline+1
    elif numero==3:
        diesel=diesel+1
    elif numero==4:
        break
print(f"MUITO OBRIGADO \nAlcool:{alcool} \nGasolina:{gasoline} \nDiesel:{diesel}")










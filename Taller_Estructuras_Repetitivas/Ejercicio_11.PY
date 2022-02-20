listas=[]
aguardiente=0
ron=0
cerveza=0
tequila=0
whisky=0
otro=0
respuesta=0
listapreferencias=[]
lista_mujeres_menores=[]
listaedad=[]
listahombres=[]
listacerveza=[]
listawhisky=[]
listaprefcerveza=[]   
respuesta=int(input("Consume usted licor si inserte 1 / no , Inserte 2 "))
while True:
    if(respuesta==1):
        edad=int(input("¿cual es tu edad? "))
        listaedad.append(edad)
        sexo=str(input("Inserte su sexo? M para masculino y F para femenino: "))
        if(edad<=18)and(sexo=="F"):
            mujeres_menores=edad
            lista_mujeres_menores.append(mujeres_menores)   
        preferencia=int(input(" Digite el numero acorde a su licor de preferencia 1-aguardiente, 2-ron, 3-cerveza, 4-tequila, 5-whisky, 6-otro: "))
        listas.append(preferencia)
        print(" Continuar con la encuesta")
        respuesta=int(input("desea continuar con la investigacion si es SI , inserte 1, si es no inserte 2: "))        
        if(preferencia==1):
            aguardiente=aguardiente+1
        elif(preferencia==2):
            ron=ron+1
        elif(preferencia==3):
            cerveza=cerveza+1
            listacerveza.append(cerveza)
            if(preferencia==3 and edad>0):
                pref_cerveza=edad
                listaprefcerveza.append(pref_cerveza)
                continue
        elif(preferencia==4):
            tequila=tequila+1   
        elif(preferencia==5):
            whisky=whisky+1
            listawhisky.append(whisky)
        elif(preferencia==6):
            otro=otro+1   
        elif(edad>=0):
            listaedad.append(edad)
            continue
        elif(20>=edad<=25)and(sexo=="M") and (preferencia!=1):
            hombres=edad+sexo
            if(preferencia!=1):
                listahombres.append(hombres)
                continue
    elif((respuesta==2)):
        listacervezat=sum(listacerveza)
        if(listacervezat==0):
            listacerveza=[1]
            print(f" El total de personas que consumen licor son {(aguardiente+ron+cerveza+tequila+whisky+otro) }")
            print(f" La cantidad de mujeres que consumen licor y que son menores de 18 años son : {len(lista_mujeres_menores)}")
            print(f" El promedio de hombre entre 20 y 25 años que no consumen aguardiente es de :{len(listahombres)}")
            print(f" El promedio de personas que consumen cerveza es de :{sum(listaprefcerveza)/sum(listacerveza)}")
            print(f" El total de Porcentaje de personas que consumen whisky en relacion con el total encuestado es de : {(len(listawhisky)/len(listas))*100} %")
            break
        else:
            print(f" El total de personas que consumen licor son {(aguardiente+ron+cerveza+tequila+whisky+otro) }")
            print(f" La cantidad de mujeres que consumen licor y que son menores de 18 años son : {len(lista_mujeres_menores)}")
            print(f" El promedio de hombre entre 20 y 25 años que no consumen aguardiente es de :{len(listahombres)}")
            print(f" El promedio de personas que consumen cerveza es de :{sum(listaprefcerveza)/sum(listacerveza)}")
            print(f" El total de Porcentaje de personas que consumen whisky en relacion con el total encuestado es de : {(len(listawhisky)/len(listas))*100} %")
            break
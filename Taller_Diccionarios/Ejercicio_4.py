
estudiantes = {
 "1": {
 "nombre": "Lorea",
 "nota": 8
 },
 "2": {
 "nombre": "Markel",
 "nota": 4.2
 },
 "3": {
 "nombre": "Julen",
 "nota": 6.5
 }
}
keys=[]
lista=[]
estudiantes_lista=3
while True:
    datos=input("Inserte nombre y nota final (La nota debe ser de 0 a 10) ")
    nom_nt=(nom,nt)=datos.split(" ")
    nom=str(nom)
    nt=float(nt)
    lista.append(datos)
    estudiantes_lista=estudiantes_lista+1
    if estudiantes_lista==11:
        break
    for i in lista:
        estudiantes.update({f"{estudiantes_lista}":{"nombre":nom,"nota":nt}})
    print(estudiantes)

    lista_notas=[]
    for i in range(1,(estudiantes_lista+1)):
        a=(estudiantes[f"{i}"]["nota"])
        lista_notas.append(int(a))
    promedio=(sum(lista_notas)/(estudiantes_lista))
    print(f"El promedio es de:{promedio} ")
    
    
listaprobados=[]
listaperdieron=[]
# Perdieron
for i in range(1,(estudiantes_lista+1)):
    if(estudiantes[f"{i}"]["nota"]<6.0):
        c=(estudiantes[f"{i}"]["nombre"])
        d=(estudiantes[f"{i}"]["nota"])
        listaperdieron.append(c)
        listaperdieron.append(d)
print(f"La lista de los estudiantes que perdieron son : {listaperdieron}")        

# Aprobaron        
for i in range(1,(estudiantes_lista+1)):
    if(estudiantes[f"{i}"]['nota']>=6.0):
        e=(estudiantes[f"{i}"]["nombre"])
        f=(estudiantes[f"{i}"]["nota"])
        listaprobados.append(e)
        listaprobados.append(f)
print(f"La lista de los estudiantes que aprobaron son : {listaprobados}")


    
    



 




        



    

    

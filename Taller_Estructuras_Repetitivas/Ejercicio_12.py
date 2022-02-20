

lista_punt_finales=[]
lista_nombres=[]
lista_nombre_puntaje=[]
cantidad_estudiantes=int(input(" Inserte la cantidad de estudiantes que presentaron la prueba : "))
for i in range(0, cantidad_estudiantes):
    datos=input("Inserte su nombre y separado por una coma su puntaje en el examen final")
    nombre_puntaje_final=(nombre,puntaje_final)=datos.split(" ")
    puntaje_final=int(puntaje_final)
    nombre=str(nombre)
    lista_punt_finales.append(puntaje_final)
    lista_nombres.append(nombre)
    lista_nombre_puntaje.append(nombre_puntaje_final)
    promedio_puntaje=sum(lista_punt_finales)/len(lista_punt_finales)
    puntajes_debajo_prom = [i for i in lista_punt_finales if i<promedio_puntaje]
    pordebajo_promedio=((sum(puntajes_debajo_prom)/len(lista_punt_finales))*100)
    puntajes_encima_promedio = [i for i in lista_punt_finales if i>promedio_puntaje]
    porencima_promedio=((sum(puntajes_encima_promedio)/len(lista_punt_finales))*100)

print(f"El estudiante que obtuvo mayor puntaje es:", (lista_nombre_puntaje[lista_punt_finales.index(max(lista_punt_finales))]))
print(f"el estudiante que obtuvo menor puntaje es:", (lista_nombre_puntaje[lista_punt_finales.index(min(lista_punt_finales))]))
print(f" El mayor puntaje es de : ", max(lista_punt_finales))
print(f" El menor puntaje es de : ", min(lista_punt_finales))
print(" El Promedio de los puntajes es de : ", promedio_puntaje)
print(f" El porcentaje que estuvo por debajo del promedio: {pordebajo_promedio}%")
print(f" El porcentaje que estuvo sobre del promedio: {porencima_promedio}%") 
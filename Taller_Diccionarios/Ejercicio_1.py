ejercicio=[12, 23, 5, 12, 92, 5,12, 5, 29, 92, 64,23]
diccionario={ }
for i in ejercicio:
    a=ejercicio.count(i)
    diccionario.update({i:a})
print(diccionario)

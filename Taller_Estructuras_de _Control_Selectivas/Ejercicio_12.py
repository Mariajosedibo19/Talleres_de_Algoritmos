"""
Datos de entrada

Cantidad en COP = cant_cop = int

Datos de salida
Descomposicion de la cantidad en los billetes y monedas = descomposicion = int

"""
# Entradas

cant_cop=int(input(" Digite la cantidad entera en COP (pesos colombianos) "))


# Caja Negra 

dinero=''
if cant_cop>=100_000:
    n_billetes= (cant_cop/100_000)
    n_billetes100=int(n_billetes)
    r_billetes100=cant_cop%100_000
    print(f"Hay {n_billetes100} billetes de 100_000")
    cant_cop= cant_cop%100_000
if cant_cop>=50000:
    n_billetes= (cant_cop/50_000)
    n_billetes50=int(n_billetes)
    r_billetes50=cant_cop%50_000
    print(f"Hay {n_billetes50} billetes de 50_000")
    cant_cop= cant_cop%50_000
if cant_cop>=20000:
    n_billetes= (cant_cop/20_000)
    n_billetes20=int(n_billetes)
    print(f"Hay {n_billetes20} billetes de 20_000")
    cant_cop=cant_cop%20_000 
if cant_cop>=10000:
    n_billetes= (cant_cop/10_000)
    n_billetes10=int(n_billetes)
    r_billetes10=cant_cop%10_000
    print(f"Hay {n_billetes10} billetes de 10_000") 
    cant_cop=cant_cop%10_000 
if cant_cop>=5000:
    n_billetes= (cant_cop/5_000)
    n_billetes5=int(n_billetes)
    r_billetes5=cant_cop%5_000
    print(f"Hay {n_billetes5} billetes de 5_000")
    cant_cop=cant_cop%5_000 
if cant_cop>=2000:
    n_billetes= (cant_cop/2_000)
    n_billetes2=int(n_billetes)
    r_billetes2=cant_cop%2_000
    print(f"Hay {n_billetes2} billetes de 2_000")
    cant_cop=cant_cop%2_000 
if cant_cop>=1000:
    n_billetes= (cant_cop/1000)
    n_billetes1000=int(n_billetes)
    r_billetes1000=cant_cop%1000
    print(f"Hay {n_billetes1000} billetes de 1_000") 
    cant_cop=cant_cop%1_000  
if cant_cop>=500:
    n_billetes= (cant_cop/500)
    n_billetes500=int(n_billetes)
    r_billetes500=cant_cop%500
    print(f"Hay {n_billetes500} billetes de 500")
    cant_cop=cant_cop%500     
if cant_cop>=200:
    n_billetes= (cant_cop/200)
    n_billetes10=int(n_billetes)
    r_billetes10=cant_cop%200
    print(f"Hay {n_billetes10} billetes de 200")
    cant_cop=cant_cop%200   
if cant_cop>=100:
    n_billetes= (cant_cop/100)
    n_billetes10=int(n_billetes)
    r_billetes10=cant_cop%100
    print(f"Hay {n_billetes10} billetes de 100")
    cant_cop=cant_cop%100 
if cant_cop>=50:
    n_billetes= (cant_cop/50)
    n_billetes50=int(n_billetes)
    r_billetes50=cant_cop%50
    print(f"Hay {n_billetes50} billetes de 50")
    cant_cop=cant_cop%50  

        





    


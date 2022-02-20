lista=[]

while True:
    n=float(input("altura"))
    if n>0:
        lista.append(n)
    elif n ==0:    
        print("la mayor altura:", max(lista)) 
        break

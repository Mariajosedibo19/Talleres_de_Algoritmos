n=1
k=0
list=[]
while k<1000:
    k=(n**2+1)/n
    print(k)
    list.append(n)
    n=n+1
    print(len(list))

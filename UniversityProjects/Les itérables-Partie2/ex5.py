n=int(input("Donner votre entier: "))
L=[]
for i in range(2,n+1):
    L.append(i)
listmultiple=L.copy()
for i in range (len(L)):
    if listmultiple[i]!=0:
        courant=listmultiple[i]
        for j in range(i+courant,len(listmultiple),courant):
            listmultiple[j]=0
for i in range(len(listmultiple)):
    if listmultiple[i]!=0:
        print(listmultiple[i],end="|")

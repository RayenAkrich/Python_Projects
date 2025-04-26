n=int(input("Donner la taille de la liste: "))
liste=[]
for i in range(n):
    liste.append(int(input("Donner un entier: ")))
liste.sort()
liste2=list(i for i in liste if i%2==0)
liste2+=list(i for i in liste if i%2!=0)
print("La liste après tri par parité est: ",liste2)
n=int(input("Donner la taille de la liste: "))
liste=[]
for i in range(n):
    liste.append(int(input("Donner un entier: ")))
liste.sort()
number=int(input("Donner un entier à insérer: "))
i=0
while i<len(liste) and liste[i]<number:
    i+=1
liste.insert(i,number)
print("La liste après insertion de l'entier ",number," est: ",liste)
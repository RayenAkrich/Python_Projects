n=int(input("Donner la taille de la liste: "))
liste=[]
for i in range(n):
    liste.append(int(input("Donner un entier: ")))
print("La liste est: ",liste)
x=int(input("Donner un entier à supprimer: "))
while x in liste:
    liste.pop(liste.index(x))
print("La liste après suppression de l'entier ",x," est: ",liste)

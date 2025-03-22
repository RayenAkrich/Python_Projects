#Écrire un script python qui cherche le premier et le deuxième maximum présents dans une liste L en faisant un seul parcours de la liste.
#Exemple : L= [32, 5, 12, 8, 3, 75, 2, 15]. Le programme affichera : "le premier maximum est 75, le deuxième est 32"
L=[]
n=int(input("Donner la taille de la liste (>=2): "))
while (n<2):
    n=int(input("Donner la taille de la liste (>=2): "))
for i in range(n):
    L.append(int(input("Donner un entier: ")))
MaxOne=L[0]
MaxTwo=L[1]
for i in range(n):
    if L[i]>MaxOne:
        MaxTwo=MaxOne
        MaxOne=L[i]
    elif L[i]>MaxTwo:
        MaxTwo=L[i]
print("le premier maximum est",MaxOne,", le deuxième est",MaxTwo)
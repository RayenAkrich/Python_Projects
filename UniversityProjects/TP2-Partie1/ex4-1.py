#Écrire un script qui lit une chaîne de caractères et construit un dictionnaire contenant la fréquence
#de tous les caractères de la chaîne saisie (les clefs du dictionnaire sont les différents caractères
#de la chaîne, les valeurs sont les fréquences associées).
chaine=input("Donner une chaine de caractères: ")
dico={}
for i in chaine:
    if i in dico:
        dico[i]+=1
    else:
        dico[i]=1
print(dico)
 
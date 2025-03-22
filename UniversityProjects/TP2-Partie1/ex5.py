#Soit un dictionnaire Classe permettant de mémoriser les noms des étudiants d’une classe, leurs âges
#et leurs moyennes. Le nom servira de clé du dictionnaire et les valeurs seront constituées des tuples de
#la forme (âge, moyenne).
#1. Donner le code python qui permet de remplir le dictionnaire Classe avec les informations de n étudiants.
n=int(input("Donner le nombre d'étudiants: "))
Classe={}
for i in range(n):
    nom=input("Donner le nom de l'étudiant: ")
    age=int(input("Donner l'âge de l'étudiant: "))
    moyenne=float(input("Donner la moyenne de l'étudiant: "))
    Classe[nom]=(age,moyenne)
#2.Donner le code python qui permet de consulter les informations relatives à un étudiant donné. Le
#résultat de la consultation devra être une ligne de texte de la forme suivante :
#Nom : Ben Moussa Ahmed – Age :19 – Moyenne :12.1 ;
#NB : Si le nom n’existe pas, le programme devra afficher : "Étudiant non reconnu".
nom=input("Donner le nom de l'étudiant à consulter: ")
if nom in Classe:
    print("Nom :",nom,"- Age :",Classe[nom][0],"- Moyenne :",Classe[nom][1],";")
else:
    print("Étudiant non reconnu")
#3.Donner le code python qui permet de déterminer le nombre d’étudiants dont l’âge ne dépasse pas
#20 ans et ayant une moyenne supérieure ou égale à 10.
cpt=0
for i in Classe:
    if Classe[i][0]<=20 and Classe[i][1]>=10:
        cpt+=1
print("Le nombre d'étudiants dont l'âge ne dépasse pas 20 ans et ayant une moyenne supérieure ou égale à 10 est:",cpt)

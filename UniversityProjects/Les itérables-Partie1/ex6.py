#Soit le le dictionnaire Livres_BD de la forme suivante :
#    Clef             |   valeur
#    Titre_Livre<str> |   tuple(<Auteur>,<nb_exemplaires>)

#1. Créer et remplir le dictionnaire Livres_BD.
print("---------------------------")
n=int(input("Donner le nombre de livres: "))
Livres_BD={}
for i in range(n):
    Titre_Livre=input("Donner le titre du livre: ")
    Auteur=input("Donner l'auteur du livre: ")
    nb_exemplaires=int(input("Donner le nombre d'exemplaires du livre: "))
    Livres_BD[Titre_Livre]=(Auteur,nb_exemplaires)
#2. Afficher l’auteur d’un livre donné ainsi que le nombre d’exemplaires.
print("---------------------------")
Titre_consulté=input("Donner le titre du livre à consulter: ")
if Titre_consulté in Livres_BD:
    print("L'auteur du livre",Titre_consulté,"est",Livres_BD[Titre_consulté][0],"et le nombre d'exemplaires est",Livres_BD[Titre_consulté][1])
else:
    print("Livre non trouvé")
#3. Afficher l’ensemble des auteurs de la base.
print("---------------------------")
print("Les auteurs de la base sont:")
for i in Livres_BD:
    print(Livres_BD[i][0])
#4. Afficher l’ensemble des livres empruntables.
print("---------------------------")
print("Les livres empruntables sont:")
for i in Livres_BD:
    if Livres_BD[i][1]>0:
        print(i)
#5. Étant donné le nom d’un auteur, afficher l’ensemble des titres des livres écrits par cet auteur.
print("---------------------------")
Auteur_consulté=input("Donner le nom de l'auteur à consulter: ")
for i in Livres_BD:
    if Livres_BD[i][0]==Auteur_consulté:
        print(i)


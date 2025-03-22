#Écrire un script qui accepte une chaîne et crée un palindrome en ajoutant à la fin une copie inversée de cette chaîne.
def Palindrome(chaine):
    return chaine[-1::-1]

Chaine = input("Entrez une chaine de caractères : ")
print(Chaine + Palindrome(Chaine))

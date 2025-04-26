#Écrire un script (avec 2 versions : une avec une boucle for ou while et une avec du slicing) qui
#détermine si une chaîne de caractères donnée est un palindrome.

def PalindromeFor(Chaine):
    Chaine=Chaine.lower()
    for i in range(len(Chaine)//2):
        if Chaine[i] != Chaine[-i-1]:
            print("Ce n'est pas un palindrome")
            exit()
    print("C'est un palindrome")
    
def PalindromeWhile(Chaine):
    Chaine=Chaine.lower()
    i=0
    while i < len(Chaine)//2:
        if Chaine[i] != Chaine[-i-1]:
            print("Ce n'est pas un palindrome")
            exit()
        i+=1
    print("C'est un palindrome")

Chaine=input("Entrez une chaine de caractères : ")
PalindromeFor(Chaine)






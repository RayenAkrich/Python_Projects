base = int(input("Donner une base (2-8) : "))
while (base < 2 or base > 8):
    base = int(input("Erreur. Donner une base entre 2 et 8 : "))

nombre = input("Donner un entier en base "+str(base)+" : ")
valid = False

while (not valid):
    valid = True
    for c in nombre:
        if int(c) >= base: 
            valid = False
            break
    
    if (not valid):
        nombre = input("Erreur. Chiffre(s) trop grand(s) pour la base "+str(base)+". Réessayez : ")
    else:
        break

res = 0
puissance = 1  
longueur = len(nombre)
for i in range(longueur - 1, -1, -1):
    chiffre = int(nombre[i])          
    res += chiffre * puissance
    puissance *= base

print("Conversion de "+nombre+" (base "+str(base)+") en base 10 : "+str(res))




#Créez cette fois le dictionnaire tel que les clefs sont les fréquences des caractères et les valeurs
#sont des listes des caractères ayant la même fréquence.
#Exemple: "abracadabra" donnera {5: ['a'], 2: ['b', 'r'], 1: ['c', 'd']}
chaine=input("Donner une chaine de caractères: ")
dico={}
for i in chaine: 
    if i in dico:
        dico[i]+=1
    else:      
        dico[i]=1   
dico2={}    
for i in dico:  
    if dico[i] in dico2:        
        dico2[dico[i]].append(i)    
    else:    
        dico2[dico[i]]=[i] 
print(dico2)

L1= [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
L2 = ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"]
#Créer la liste L3 par compréhension à partir de L1 et L2 telle que :
#L3= [("Janvier",31),("Février",28),("Mars",31),...].
L3=list([L1(i),L2[i]] for i in range(12))
print(L3)

suite=[]
moyenne=[]
print("Donner votre suite :")
j=0
while(True):
    n=int(input("Donner un entier : "))
    if(n==-1 and j>3):
        break
    while(n<0):
        n=int(input("Donner un entier positif: "))
    suite.append(n)
    j+=1
moyenne=["-","-"]
for i in range(2,len(suite)):
    moyenne.append((suite[i-2]+suite[i-1]+suite[i])/3)
print("la moyenne de chaque triplet est : ",moyenne)
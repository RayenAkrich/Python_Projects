n=int(input("Donner la taille de la liste: "))
liste=[]
for i in range(n):
    liste.append(int(input("Donner un entier: ")))
sum=0
for i in liste:
    sum+=i
m=sum/n
sum2=0
for i in liste:
    sum2+=abs(i-m)
var=sum2/n
print("la variance de la liste est: ",var)
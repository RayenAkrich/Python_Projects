#Soit la liste L=[0,1,2,3,4,5,6,7,8,9,10], créer les listes suivantes par compréhension à partir de
L=[0,1,2,3,4,5,6,7,8,9,10]
#           L=list(i for i in range (11))
L1=[]
L2=[]
L3=[]
L4=[]
L5=[]
#L1=[0,2,4,6,8,10,12,14,16,18,20]
#           L1=list(i*2 for i in L)
for i in range(len(L)):
    L1.append(L[i]*2)
#L2=[[0,0],[1,1],[2,2],[3,3,[4,4],[5,5],[6,6],[7,7],[8,8],[9,9],[10,10]]
#           L2=list([i,i] for i in L))
for i in range(len(L)):
    L2.append([L[i],L[i]])
#L3=[0,0,1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10]
#           L3=list(i for i in L for j in range(2))
for i in range(len(L)):
    L3.append(L[i])
    L3.append(L[i])
#L4=[0,1,2,3,4,5,6,7,8,9,10, 0,1,2,3,4,5,6,7,8,9,10]
#           L4=list(L+L)
for i in range(len(L)):
    L4.append(L[i])
for i in range(len(L)):
    L4.append(L[i])
#L5=[1,2,2,3,3,3,4,4,4,4,5,5,5,5,5,6,6,6,6,6,6,7,7,7,7,7,7,7,8,8,8,8,8,8,8,8,9,9,9,9,9,9,9,9,9,10,10,10,10,10,10,10,10,10,10]
#           L5 = list(i for i in range(11) for j in range(i))
for i in range(1,len(L)):
    for j in range(i):
            L5.append(L[i])
print("L1 = ",L1)
print("L2 = ",L2)
print("L3 = ",L3)
print("L4 = ",L4)
print("L5 = ",L5)
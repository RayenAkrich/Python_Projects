
#version1 - on écrit ligne par ligne avec write
def remplir_fichier1(nom_fichier,n):
  f=open(nom_fichier,'w')
  for i in range(n):
    nom=input("Donner le nom ")
    note=float(input("Donner la note "))
    f.write(nom+':'+str(note)+'\n')
  f.close()

#version2 - On écrit toutes les lignes en utilisant une liste L avec writelines
def remplir_fichier2(nom_fichier,n):
  f=open(nom_fichier,'w')
  L=[]
  for i in range(n):
    nom=input("donner le nom")
    note=float(input("donner la note"))	
    L.append(nom+':'+str(note)+'\n')
  f.writelines(L)
  f.close()



#version 1 - on lit le fichier avec readlines (le résulat est une liste fomée des différentes lignes du fichier).
def calculer_moyenne1(nom_fichier):
  f=open(nom_fichier,'r')
  L=f.readlines()
  f.close()
  s=0
  for ch in L:
    E=ch.split(":")
    s=s+float(E[1])
  return(s/len(L))


#version 2 - On lit le fichier ligne par ligne avec readline
def calculer_moyenne2(nom_fichier):
  f=open(nom_fichier,'r')
  s,n=0,0    
  while True:
    ch=f.readline()
    if ch!='':
      E=ch.split(":")
      s=s+float(E[1])
      n=n+1
    else: break
  f.close()
  return(s/n)




#version 3 - On lit le fichier ligne par ligne avec readline 
def calculer_moyenne3(nom_fichier):
  #lecture par ligne
  f=open(nom_fichier,'r')
  s,n=0,0
  ch=f.readline()
  while ch!='':
    E=ch.split(":")
    s=s+float(E[1])
    n=n+1
    ch=f.readline()
  f.close()
  return(s/n)



remplir_fichier2("Notes.txt",3)
moy=calculer_moyenne2("Notes.txt")
print('La moyenne est',moy)

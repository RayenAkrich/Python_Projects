# Version 1 - Lecture ligne par ligne avec readlines
def liste_munip(fichier):
    f = open(fichier, 'r')
    L = f.readlines()
    f.close()
    
    resultat = []
    for ligne in L:
        resultat.append(ligne.strip().lstrip('#'))
    return resultat

# Version 2 - Lecture ligne par ligne avec readline
def tuple_munip(fichier):
    lignes = liste_munip(fichier)
    resultat = []
    
    for ligne in lignes:
        elements = ligne.split(';') 
        resultat.append((elements[0], elements[1], int(elements[2])))
    
    return tuple(resultat)

# Recherche de la municipalité avec le nom le plus long et le plus court
def lc_munip(fichier):
    municipalites = tuple_munip(fichier)
    noms = [mun[0] for mun in municipalites]
    return max(noms, key=len), min(noms, key=len)


# Municipalités avec population inférieure à un seuil
def seuil_munip(fichier, N):
    municipalites = tuple_munip(fichier)
    resultat = [(nom, gov) for nom, gov, pop in municipalites if pop < N] 
    return resultat 

# Création d'un dictionnaire par gouvernorat
def gouv_munip(fichier):
    municipalites = tuple_munip(fichier) 
    dico = {}

    for nom, gouv, pop in municipalites:
        if gouv in dico:
            dico[gouv] = (dico[gouv][0] + 1, dico[gouv][1] + pop)
        else:
            dico[gouv] = (1, pop)
    
    return dico


# Création d'un fichier à partir du dictionnaire
def creer_fich(fichier1, fichier2):
    dico = gouv_munip(fichier1)
    
    f = open(fichier2, 'w')
    f.write("CodeGouv (NbMuni,NbPop)\n")
    for gouv, data in dico.items():
        f.write(gouv + " " + str(data) + "\n")
    f.close()

    creer_fich('munip.txt', 'gouv.txt')
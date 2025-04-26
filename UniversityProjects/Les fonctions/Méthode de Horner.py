def saisir_nombre_base():
    N = int(input("Entrez un nombre N : "))
    b = int(input("Entrez la base b (2 ≤ b ≤ 8) : "))
    return N, b

def est_valide_base(N, b):
    chiffres = str(N)
    for ch in chiffres:
        if int(ch) >= b:
            return False
    return True

def horner_conversion(N, b):
    chiffres = str(N)
    res = 0
    for ch in chiffres:
        res = res * b + int(ch)
    return res

N, b = saisir_nombre_base()
if est_valide_base(N, b):
    print("Conversion :", horner_conversion(N, b))
else:
    print("Nombre invalide pour la base", b)
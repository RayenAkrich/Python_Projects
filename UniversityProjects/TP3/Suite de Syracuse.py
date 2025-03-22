def terme_suivant(a):
    if a == 1:
        return 1
    elif a % 2 == 0:
        return a // 2
    else:
        return 3 * a + 1

def nbr_iter(a):
    iterations = 0
    while a != 1:
        a = terme_suivant(a)
        iterations += 1
    return iterations

def nbr_iter_min(L):
    return max(nbr_iter(a) for a in L)

L = list(map(int, input("Entrez une liste d'entiers séparés par des espaces : ").split()))
print("Nombre d'itérations minimum nécessaire :", nbr_iter_min(L))
def saisir_entier():
    while True:
        n = int(input("Entrez un entier ≥ 0 : "))
        if n >= 0:
            return n

def puissance_naive(x, n):
    result = 1
    for _ in range(n):
        result *= x
    return result

def puissance_naive_rec(x, n):
    return 1 if n == 0 else x * puissance_naive_rec(x, n - 1)

def puissance_rapide(x, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        temp = puissance_rapide(x, n // 2)
        return temp * temp
    else:
        temp = puissance_rapide(x, (n - 1) // 2)
        return x * temp * temp

def puissance_rapide_rec(x, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        temp = puissance_rapide_rec(x, n // 2)
        return temp * temp
    else:
        temp = puissance_rapide_rec(x, (n - 1) // 2)
        return x * temp * temp
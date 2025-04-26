def euclide_iter(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def euclide_recursif(a, b):
    return a if b == 0 else euclide_recursif(b, a % b)
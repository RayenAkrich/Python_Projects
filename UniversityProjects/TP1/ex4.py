n = 0
while (n <= 0):
    n = int(input("Donner un entier N ≥ 1 : "))
somme = 0.0
for k in range(1, n + 1):
    terme = 1 / ((4 * k - 3) * (4 * k - 1))
    somme += terme

pi_approx = 8 * somme
print("Approximation de π avec N=",n,": ",pi_approx)
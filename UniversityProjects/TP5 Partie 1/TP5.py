import numpy as np
import matplotlib.pyplot as plt

# Question 1
a1 = np.zeros(10)
a2 = np.ones(10)
a3 = np.full(10, 5)

# Question 2
b = np.arange(30, 71)

# Question 3
c = np.arange(30, 71, 2)

# Question 4
d = np.eye(3)

# Question 5
e = np.arange(10, 22).reshape(3, 4)

# Question 6
f = np.zeros((10, 10))
f[0, :] = 1
f[-1, :] = 1
f[:, 0] = 1
f[:, -1] = 1

# Question 7
g = np.diag([1, 2, 3, 4, 5])

# Question 8
def somme_matrice(m):
    print("Somme totale:", np.sum(m))
    print("Somme par colonne:", np.sum(m, axis=0))
    print("Somme par ligne:", np.sum(m, axis=1))

# Question 9
def somme_diagonales(m):
    diag_principale = np.trace(m)
    diag_secondaire = np.trace(np.fliplr(m))
    print("Diagonale principale:", diag_principale)
    print("Diagonale secondaire:", diag_secondaire)

# Question 10
x = np.linspace(-3*np.pi, 3*np.pi, 1000)
y = np.sin(x)
plt.plot(x, y)
plt.title("Courbe de la fonction sinus")
plt.show()

# Question 11
T1 = np.arange(6, 12)
M1 = T1.reshape(2, 3)
M2 = T1.reshape(3, 2)
M3 = T1.reshape(6, 1)

# Question 12
def augmenter_taille(t):
    return np.tile(t, 4)

# Question 13
M = np.zeros((5, 3))
M_ajoutee = np.pad(M, ((0, 1), (0, 2)), mode='constant')

# Question 14
def transpose_sans_numpy(M):
    return np.array([[M[j, i] for j in range(M.shape[0])] for i in range(M.shape[1])])

# Question 15
def permuter_colonnes(M):
    return M[:, ::-1]

# Question 16
def voisins(M, i, j):
    print("4 voisins:", M[i-1, j], M[i+1, j], M[i, j-1], M[i, j+1])
    print("8 voisins:", M[i-1, j-1], M[i-1, j], M[i-1, j+1], 
          M[i, j-1], M[i, j+1], 
          M[i+1, j-1], M[i+1, j], M[i+1, j+1])

# Question 17
def voisins_interieurs(M):
    for i in range(1, M.shape[0]-1):
        for j in range(1, M.shape[1]-1):
            print(f"Élément ({i},{j}):", 
                  M[i-1, j], M[i+1, j], M[i, j-1], M[i, j+1])


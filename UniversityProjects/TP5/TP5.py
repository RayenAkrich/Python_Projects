#Manipulation d’une image couleur

#1. Charger l'image
import numpy as np
from matplotlib.image import imread

def charger_image(chemin):
    return imread(chemin)

I = charger_image('image.png')

#2. Tester la fonction
print("Type de I:", type(I)) #Type de I: <class 'numpy.ndarray'>
print("Dimensions de I:", I.shape) #Dimensions de I: (hauteur, largeur, 3)
print("Type des éléments de I:", I.dtype) #Type des éléments de I: uint8

#3. Afficher une image 
import matplotlib.pyplot as plt

def afficher_image(image):
    if len(image.shape) == 2:
        plt.imshow(image, cmap='gray')  # Forcer cmap='gray' pour les images 2D
    else:
        plt.imshow(image)              # Afficher normalement pour les images RGB
    plt.axis('off')
    plt.show()

afficher_image(I)

#4. Extraire les composantes de couleur
def composante_rouge(image):
    rouge = image.copy()
    rouge[:, :, [1, 2]] = 0  # Met les canaux vert et bleu à 0
    return rouge

def composante_verte(image):
    vert = image.copy()
    vert[:, :, [0, 2]] = 0  # Met les canaux rouge et bleu à 0
    return vert

def composante_bleue(image):
    bleu = image.copy()
    bleu[:, :, [0, 1]] = 0  # Met les canaux rouge et vert à 0
    return bleu

    # Exemple d'utilisation
I_rouge = composante_rouge(I)
I_vert = composante_verte(I)
I_bleu = composante_bleue(I)

#5. Afficher quatre images dans un graphique
def afficher_quatre_images(original, rouge, vert, bleu):
    plt.figure(figsize=(10, 8))
    
    plt.subplot(2, 2, 1)
    plt.imshow(original)
    plt.xlabel('Originale')
    
    plt.subplot(2, 2, 2)
    plt.imshow(rouge)
    plt.xlabel('Rouge')
    
    plt.subplot(2, 2, 3)
    plt.imshow(vert)
    plt.xlabel('Vert')
    
    plt.subplot(2, 2, 4)
    plt.imshow(bleu)
    plt.xlabel('Bleu')
    
    plt.tight_layout()
    plt.show()

afficher_quatre_images(I, I_rouge, I_vert, I_bleu)

#6. Conversion en niveaux de gris (moyenne RGB)
def convertir_niveaux_de_gris(image_couleur):
    # Calcul de la moyenne des canaux RGB (résultat 2D)
    gris = np.mean(image_couleur, axis=2)
    gris = (gris * 255).astype(np.uint8) 
    return gris

I_gris = convertir_niveaux_de_gris(I)
afficher_image(I_gris)

#Manipulation d’une image en niveaux de gris
#1. Symétrie verticale et horizontale
def symetrie_verticale(image):
    return image[:, ::-1]

def symetrie_horizontale(image):
    return image[::-1, :]

I_vertical = symetrie_verticale(I_gris)
I_horizontal = symetrie_horizontale(I_gris)
afficher_image(I_vertical)
afficher_image(I_horizontal)

#2. Négatif de l'image
negatif = lambda x: 255 - x

def appliquer_negatif(image):
    return negatif(image)

I_negatif = appliquer_negatif(I_gris)
afficher_image(I_negatif)

#3. Amélioration du contraste
f = lambda x: np.sqrt(x) * (255 / np.sqrt(255))  # Normalisation
g = lambda x: 0.5 + 0.5 * np.sin(np.pi * (x / 255 - 0.5)) * 255  # Ajustement pour [0, 255]

def appliquer_fonction(image, fonction):
    return fonction(image).astype(np.uint8)

I_f = appliquer_fonction(I_gris, f)
I_g = appliquer_fonction(I_gris, g)
afficher_image(I_f)
afficher_image(I_g)

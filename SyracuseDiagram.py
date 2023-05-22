# -*- coding: utf-8 -*-
"""
Created on Thu May 18 14:47:42 2023

@author: steph
"""

import matplotlib.pyplot as plt

def syracuse_tree(n, x=0, y=0, depth=0):
    # Dessiner le cercle pour le nombre n
    circle = plt.Circle((x, y), 0.5, color='white', ec='black')
    plt.gcf().gca().add_artist(circle)
    plt.text(x, y, str(n), ha='center', va='center')
    if depth == 0:
        return
    # Calculer les deux prochains nombres de la suite de Syracuse
    a = 2 * n if n % 2 == 0 else 3 * n + 1
    b = 2 * a if a % 2 == 0 else 3 * a + 1
    # Calculer les coordonnées des deux prochains cercles
    x1, y1 = x - 2 ** (depth - 1), y - 1
    x2, y2 = x + 2 ** (depth - 1), y - 1
    # Dessiner les deux liens vers les prochains cercles
    plt.plot([x, x1], [y, y1], color='black')
    plt.plot([x, x2], [y, y2], color='black')
    # Appeler la fonction récursivement pour dessiner les deux prochains cercles
    syracuse_tree(a, x1, y1, depth - 1)
    syracuse_tree(b, x2, y2, depth - 1)

# Dessiner l'arbre de Syracuse pour le nombre initial 27 avec une profondeur de 4 niveaux
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_aspect('equal')
syracuse_tree(27, depth=4)
plt.axis('off')
plt.show()
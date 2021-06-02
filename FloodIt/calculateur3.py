'''
le flood va être récursif


le problème rencontré sur les calculateurs précédents est que la détection de voisin est faîte en regardant UNE fois sur les côtés 

départ
    |           donne
   -0 0 0 1 2   ->  1 1 0 1 2   ->  2 2 0 1 2   ->  3 3 0 1 2
    2 3 1 1 2       2 3 1 1 2       2 3 1 1 2       3 3 1 1 2
    
or je veux :
   -0 0 0 1 2   ->  1 1 1 1 2   ->  2 2 2 2 2   ->  3 3 3 3 3
    2 3 1 1 2       2 3 1 1 2       2 3 2 2 2       3 3 3 3 3

il me faut en fait que, lorsqu'un copain est trouvé, je relance la détection sur ce nouveau collègue

-> tableau pour gérer le général
-> ensemble des valeurs connus
-> tableau pour les voisins

'''
from random import randrange,seed
from time import time


#importés de calculateur2.py

#construction du jeu
def initialisation(taille,nb_couleur):
    matrice=[]
    for i in range(taille*taille):
        matrice.append(randrange(0,nb_couleur))
    return matrice

#affichage joli
def montre(t,m):
    i=0
    while m!=[]:
        print(m[0],end=" ")
        m=m[1:]
        i+=1
        if i%t == 0:
            print()


#construit la nouvelle génération
#renvoie les nouveaux voisins et ajoute des positions
#couleur : correspond à la couleur du tour
def generation(matrice, ensemble_pos, liste_voisins, couleur):
    
    
    
    #
    #travail
    #
    return position,voisins


#prend une cellule, regarde ses voisins et renvoie une liste des cellules identiques
def observe(coordo, matrice, ensemble_pos):
    #
    #travail
    #
    return une_liste

if __name__=='__main__': 
    #les infos obligatoires
    nb_couleur=6
    taille=7
    voisins = {0} #stocke les numéros des cases à contrôler
    change = [0]

    seed(0)#pour avoir tout le temps la même matrice
    
    matrice = initialisation(taille,nb_couleur)
    montre(taille,matrice)

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



#on regarde si la cellule à encore besoin d'être mémorisé pour étudier les générations
#on regarde si les cellules sont connus
def controleVoisin(cell, ensemble_pos, taille):
    l = taille*taille
    
    #contrôle droite
    if cell != l-1:
        a = cell+1 in ensemble_pos
    else:
        a = True
        
    #contrôle gauche
    if cell!=0:
        b = cell-1 in ensemble_pos
    else:
        b = True
    
    #contrôle bas
    if cell< l-taille:
        c = cell+taille in ensemble_pos
    else:
        c = True
        
    #contrôle haut
    if cell> taille-1:
        d = cell-taille in ensemble_pos
    else:
        d = True
        
    return a and b and c and d

#prend une cellule, regarde ses voisins et renvoie une liste des cellules identiques
def observe(cell, matrice, liste, taille):
    try : #check droite 
        #print("check droite",matrice[cell] == matrice[cell+1] and cell+1 not in liste)
        if matrice[cell] == matrice[cell+1] and cell+1 not in liste:
            liste.append(cell+1)
            a = observe(cell+1,matrice,liste[:])
            for k in a:
                liste.append(k)
    except:
        pass
    
    try : #check gauche
        #print("check gauche",matrice[cell] == matrice[cell-1] and cell-1 not in liste)
        if matrice[cell] == matrice[cell-1] and cell-1 not in liste and cell!=0:
            liste.append(cell-1)
            a = observe(cell-1,matrice,liste[:])
            for k in a:
                liste.append(k)
    except:
        pass
    
    try : #check bas
        #print("check bas",matrice[cell] == matrice[cell+taille] and cell+taille not in liste)
        if matrice[cell] == matrice[cell+taille] and cell+taille not in liste:
            liste.append(cell+taille)
            a = observe(cell+taille,matrice,liste[:])
            for k in a:
                liste.append(k)
    except:
        pass
    
    try : #check haut
        #print("check haut",matrice[cell] == matrice[cell-taille] and cell-taille not in liste)
        if matrice[cell] == matrice[cell-taille] and cell-taille not in liste and cell>taille:
            liste.append(cell-taille)
            a = observe(cell-taille,matrice,liste[:])
            for k in a:
                liste.append(k)
    except:
        pass

    return liste

#construit la nouvelle génération
#renvoie les nouveaux voisins et ajoute des positions
def generation(matrice, ensemble_pos, liste_voisins, taille):
    nouveau_voisins=liste_voisins[:]
    
    for cell in liste_voisins:
        liste = observe(cell, matrice, [cell], taille)
        if liste != [] :
            
            for nouveau in liste:
                if nouveau not in liste_voisins:
                    liste_voisins.append(nouveau)

                if nouveau not in ensemble_pos:
                    ensemble_pos.add(nouveau)
            
        #module de voisinage
        if controleVoisin(cell, ensemble_pos, taille):
            nouveau_voisins=nouveau_voisins[1:]
        
    return ensemble_pos,liste_voisins[len(nouveau_voisins)-1:]


#on change la matrice avec un nouveau chiffre
def transform(matrice, ensemble_pos, couleur):
    for i in ensemble_pos:
        matrice[i]=couleur
    return matrice

if __name__=='__main__': 
    #les infos obligatoires
    nb_couleur=6
    taille=7
    position = {0}    #stocke les numéros à changer
    voisins = [0]   #stocke les cell à examiner

    seed(0)         #pour avoir tout le temps la même matrice
    
    matrice = initialisation(taille,nb_couleur)
    montre(taille,matrice)
    print()
    couleur = 2
    position, voisins = generation(matrice, position, voisins, taille)
    
    matrice =  transform(matrice, position, couleur)
    
    montre(taille, matrice)
    
    ###########################
    
    for k in [4,1,2,4,5,2,3,0,4,5,3,1]:
        print()
        couleur = k
        position, voisins = generation(matrice, position, voisins, taille)
        print(position,end="\n")
        print(voisins,end="\n")
        
        matrice =  transform(matrice, position, couleur)
        
        montre(taille, matrice)

    ###########################
    print()
    print("Lancement calcul temps")
    for taille in range(2,35):
        temps=time()
        nb_couleur=6
        
        position = {0}    #stocke les numéros à changer
        voisins = [0]   #stocke les cell à examiner
        
        matrice = initialisation(taille,nb_couleur)
        #montre(taille,matrice)
        i=0
        while len(position)!=taille*taille:
            #print(generation(matrice, position, voisins))
            position, voisins = generation(matrice, position, voisins, taille)
            
            matrice =  transform(matrice, position, i%6)
            i+=1
        #montre(taille,matrice)
        print("Taille :",taille,"->",time()-temps)

    temps=time()
    nb_couleur=6
    taille=100
    position = {0}    #stocke les numéros à changer
    voisins = [0]   #stocke les cell à examiner
    
    matrice = initialisation(taille,nb_couleur)
    #montre(taille,matrice)
    i=0
    while len(position)!=taille*taille:
        #print(generation(matrice, position, voisins))
        position, voisins = generation(matrice, position, voisins, taille)
        
        matrice =  transform(matrice, position, i%6)
        i+=1
    #montre(taille,matrice)
    print("Taille :",taille,"->",time()-temps)

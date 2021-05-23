from random import randrange,seed
from copy import deepcopy

seed(0)



def initialisation(matrice):
    for i in range(14):
        liste = []
        for j in range(14):
            liste.append(randrange(0,6))
        matrice.append(liste)
        liste=[]

    return matrice


def transition(matrice,ensemble_pos,elem):
    for position in ensemble_pos:
        x = int(position[1],base=10)
        y = int(position[4],base=10)
        matrice[x][y]=elem
    return matrice



def affiche(matrice):
    for j in range(len(matrice)):
        for i in range(14):
            print(matrice[j][i],end=" ")
        print()
    print()

def detecte(matrice, ensemble_pos):
    ancien=deepcopy(ensemble_pos)
    for position in ancien:
        x = int(position[1],base=10)
        y = int(position[4],base=10)
        if matrice[x-1][y]==matrice[x][y]:
            if x>0:
                ensemble_pos.add(str([x-1,y]))
        elif matrice[x+1][y]==matrice[x][y]:
            if x<14:
                ensemble_pos.add(str([x+1,y]))
        elif matrice[x][y-1]==matrice[x][y]:
            if y>0:
                ensemble_pos.add(str([x,y-1]))
        elif matrice[x][y+1]==matrice[x][y]:
            if y<14:
                ensemble_pos.add(str([x,y+1]))
    return ensemble_pos

matrice=[]

ensemble_pos=set()

ensemble_pos.add(str([0,0]))

print(ensemble_pos)
matrice=initialisation(matrice)
affiche(matrice)
##tour
ensemble_pos=detecte(matrice,ensemble_pos)
elem=2
affiche(transition(matrice,ensemble_pos,elem))

ensemble_pos=detecte(matrice,ensemble_pos)
elem=9
affiche(transition(matrice,ensemble_pos,elem))

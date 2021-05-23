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
        position=position.split(",")
        x = int(position[0],base=10)
        y = int(position[1],base=10)
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
        position=position.split(",")
        x = int(position[0],base=10)
        y = int(position[1],base=10)
        
        if x>0:
            if matrice[x-1][y]==matrice[x][y]:
                ensemble_pos.add(str(x-1)+","+str(y))
        if x<13:
            if matrice[x+1][y]==matrice[x][y]:
                ensemble_pos.add(str(x+1)+","+str(y))
        if y>0:
            if matrice[x][y-1]==matrice[x][y]:
                ensemble_pos.add(str(x)+","+str(y-1))
        if y<13:
            if matrice[x][y+1]==matrice[x][y]:
                ensemble_pos.add(str(x)+","+str(y+1))
    return ensemble_pos

matrice=[]

ensemble_pos=set()

ensemble_pos.add("0,0")

print(ensemble_pos)

matrice=initialisation(matrice)
affiche(matrice)
'''
##tour
ensemble_pos=detecte(matrice,ensemble_pos)
elem=2
affiche(transition(matrice,ensemble_pos,elem))

ensemble_pos=detecte(matrice,ensemble_pos)
elem=1
affiche(transition(matrice,ensemble_pos,elem))

ensemble_pos=detecte(matrice,ensemble_pos)
elem=0
affiche(transition(matrice,ensemble_pos,elem))

ensemble_pos=detecte(matrice,ensemble_pos)
elem=2
affiche(transition(matrice,ensemble_pos,elem))
'''


i=0
while len(ensemble_pos)!=196: # nombre de cases
    i+=1
    ensemble_pos = deepcopy(detecte(matrice,ensemble_pos))
    elem=i%6
    matrice = deepcopy(transition(matrice,ensemble_pos,elem))

affiche(matrice)


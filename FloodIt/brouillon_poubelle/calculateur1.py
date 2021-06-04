'''
On construit une matrice

On utilise un ensemble pour avoir les positions connus

IMPROVE : Utiliser un second ensemble pour avoir uniquement les cases à contrôler et oublier celles qui sont sûres
'''


from random import randrange,seed
from time import time

seed(0)


#construction du jeu
def initialisation(taille):
    matrice=[]
    for i in range(taille):
        liste = []
        for j in range(taille):
            liste.append(randrange(0,6))
        matrice.append(liste)
        liste=[]
    return matrice

#changement entre la matrice et les elements connus
def transition(matrice,ensemble_pos,elem):
    for position in ensemble_pos:
        position=position.split(",")
        x,y = int(position[0],base=10),int(position[1],base=10)
        matrice[x][y]=elem
    return matrice



def affiche(matrice,t):
    for j in range(len(matrice)):
        for i in range(t):
            print(matrice[j][i],end=" ")
        print()
    print()


#regarde si des cases connus, les voisins snt identiques
def detecte(matrice, ensemble_pos, taille):
    ancien=ensemble_pos.copy()
    for position in ancien:
        position=position.split(",")
        x = int(position[0],base=10)
        y = int(position[1],base=10)
        
        if x>0:
            if matrice[x-1][y]==matrice[x][y]:
                ensemble_pos.add(str(x-1)+","+str(y))
        if x<taille-1:
            if matrice[x+1][y]==matrice[x][y]:
                ensemble_pos.add(str(x+1)+","+str(y))
        if y>0:
            if matrice[x][y-1]==matrice[x][y]:
                ensemble_pos.add(str(x)+","+str(y-1))
        if y<taille-1:
            if matrice[x][y+1]==matrice[x][y]:
                ensemble_pos.add(str(x)+","+str(y+1))
    return ensemble_pos


for j in range(2,35):
    taille=j
    matrice=initialisation(taille)
    #affiche(matrice,taille)
    ensemble_pos=set()
    ensemble_pos.add("0,0")
    #print(ensemble_pos)
    a=time()
    i=0
    while len(ensemble_pos)!=taille*taille: # nombre de cases
        i+=1
        ensemble_pos = detecte(matrice,ensemble_pos,taille)
        elem=i%6
        matrice = transition(matrice,ensemble_pos,elem)
        '''
        affiche(matrice,taille)

    affiche(matrice,taille)
    '''
    print("Taille :",taille,"->", time()-a)
    
    
    
    
taille=100
matrice=initialisation(100)
#affiche(matrice,taille)
ensemble_pos=set()
ensemble_pos.add("0,0")
#print(ensemble_pos)
a=time()
i=0
while len(ensemble_pos)!=taille*taille: # nombre de cases
    i+=1
    ensemble_pos = detecte(matrice,ensemble_pos,taille)
    elem=i%6
    matrice = transition(matrice,ensemble_pos,elem)
    '''
    affiche(matrice,taille)

affiche(matrice,taille)
'''
print("Taille : 100 ->", time()-a)

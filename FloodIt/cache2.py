'''
si on prend un unique tableau...
et qu'il a un rendu matricielle

alors un unique parcours de tableau suffit

avec un second tableau qui stocke les cellules à contrôler !!!
et un troisième pour avoir les cellules à changer
'''

from random import randrange,seed
from time import time

seed(0)


#les infos obligatoires
nb_couleur=6
taille=14
voisins = [0] #stocke les numéros des cases à contrôler
change = [0]


#les méthodes à utiliser

#construction du jeu
def initialisation(taille,nb_couleur):
    matrice=[]
    for i in range(taille*taille):
        matrice.append(randrange(0,nb_couleur))
    return matrice

#changement entre la matrice et les elements connus
#E : tableau, liste position, et l'élément sélectionner
#
#S : tableau
def transition(matrice,change,elem):
    for pos in change:
        matrice[pos]=elem
    return matrice


#prends la matrice et les cases à observer et on regarde si à côté c'est pareil
# E : tableau du jeu, tableau de voisins, tableau de position, taille
#
# S : tableau de voisins, tableau de position
def etude(matrice,voisins,position, taille):
    #test si la cellule est intéressante à conserver dans voisins
    g,d,h,b = False,False,False,False
    voisins2=voisins[:]
    
    for test in range(len(voisins)):
        a=matrice[voisins[test]]
        
        #si c'est la première case
        if voisins[test]==0:
            #contrôle droite
            if matrice[voisins[test]+1]==a:
                d=True
                if voisins[test]+1 not in position:
                    voisins.append(voisins[test]+1)
                    position.append(voisins[test]+1)
            
            #contrôle gauche
            g=True
            
            #contrôle haut
            h=True
          
            #contrôle bas
            if matrice[voisins[test]+taille]==a:
                b=True
                if voisins[test]+taille not in position:
                    voisins.append(voisins[test]+taille)
                    position.append(voisins[test]+taille)
        
        
        #si c'est la dernière case
        elif voisins[test]==taille*taille-1:
            #contrôle droite
            d=True
            
            #contrôle gauche
            if matrice[voisins[test]-1]==a:
                g=True
                if voisins[test]-1 not in position:
                    voisins.append(voisins[test]-1)
                    position.append(voisins[test]-1)
            
            #contrôle haut
            if matrice[voisins[test]-taille]==a:
                h=True
                if voisins[test]-taille not in position:
                    voisins.append(voisins[test]-taille)
                    position.append(voisins[test]-taille)
            
            #contrôle bas
            b=True
            
        #si c'est la première ligne
        elif voisins[test] <= taille :   
            #contrôle droite
            if matrice[voisins[test]+1]==a:
                d=True
                if voisins[test]+1 not in position:
                    voisins.append(voisins[test]+1)
                    position.append(voisins[test]+1)
            
            #contrôle gauche
            if matrice[voisins[test]-1]==a:
                g=True
                
                if voisins[test-1] not in position:
                    voisins.append(voisins[test]-1)
                    position.append(voisins[test]-1)
            
            #contrôle haut
            h=True
            
            #contrôle bas
            if matrice[voisins[test]+taille]==a:
                b=True
                if voisins[test]+taille not in position:
                    voisins.append(voisins[test]+taille)
                    position.append(voisins[test]+taille)
        
        #si c'est la dernière ligne 
        elif voisins[test] >= taille*taille - taille :
            #contrôle droite
            if matrice[voisins[test]+1]==a:
                d=True
                if voisins[test]+1 not in position:
                    voisins.append(voisins[test]+1)
                    position.append(voisins[test]+1)
            
            #contrôle gauche
            if matrice[voisins[test]-1]==a:
                g=True
                if voisins[test]-1 not in position:
                    voisins.append(voisins[test]-1)
                    position.append(voisins[test]-1)
            
            #contrôle haut
            if matrice[voisins[test]-taille]==a:
                h=True
                if voisins[test]-taille not in position:
                    voisins.append(voisins[test]-taille)
                    position.append(voisins[test]-taille)
            
            #contrôle bas
            b=True
            
        
        #ailleurs
        else:
            #contrôle droite
            if matrice[voisins[test]+1]==a:
                d=True
                if voisins[test]+1 not in position:
                    voisins.append(voisins[test]+1)
                    position.append(voisins[test]+1)
            
            #contrôle gauche
            if matrice[voisins[test]-1]==a:
                g=True
                if voisins[test]-1 not in position:
                    voisins.append(voisins[test]-1)
                    position.append(voisins[test]-1)
            
            #contrôle haut
            if matrice[voisins[test]-taille]==a:
                h=True
                if voisins[test]-taille not in position:
                    voisins.append(voisins[test]-taille)
                    position.append(voisins[test]-taille)
            
            #contrôle bas
            if matrice[voisins[test]+taille]==a:
                b=True
                if voisins[test]+taille not in position:
                    voisins.append(voisins[test]+taille)
                    position.append(voisins[test]+taille)
        
        if g and d and h and b :
            #print(g,d,h,b,voisins2[0])
            voisins2=voisins2[1:]
    
    #quand c'est finis, on mets à jours les cases qui seront contrôlé au prochain tour
    #print(voisins2)
    voisins=voisins[len(voisins2)-1:]
    print(voisins,"\n",position)
    return voisins, position

#affichage joli
def montre(t,m):
    i=0
    while m!=[]:
        print(m[0], end=" ")
        m=m[1:]
        i+=1
        if i%t == 0:
            print()


###zone de test###########################################################
#les infos obligatoires
matrice=[]
nb_couleur=6
taille=3
voisins = [0] #stocke les numéros des cases à contrôler
change = [0]


matrice=initialisation(taille,nb_couleur)
montre(taille,matrice)
print()
a=time()
i=0
while len(change)!=taille*taille-1 : # nombre de cases
    i+=1
    montre(taille, matrice)
    voisins,change = etude(matrice,voisins,change,taille)
    elem=i%6
    matrice = transition(matrice,change,elem)
    print()

montre(taille, matrice)
print("Taille :",taille,"\nTemps de résolution :", time()-a)




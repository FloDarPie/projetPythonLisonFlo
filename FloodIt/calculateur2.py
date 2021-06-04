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
    controle = len(voisins2)
    
    for test in range(len(voisins)):
        a=matrice[voisins[test]]
        
        
        
        ######### MODULE de contrôle d'UNE cellule
        
        #si c'est la première case
        if voisins[test]==0:
            #contrôle droite
            if matrice[voisins[test]+1]==a:
                if voisins[test]+1 not in position:
                    d=True
                    voisins.append(voisins[test]+1)
                    position.append(voisins[test]+1)
            
            #contrôle gauche
            g=True
            
            #contrôle haut
            h=True
          
            #contrôle bas
            if matrice[voisins[test]+taille-1]==a:
                if voisins[test]+taille-1 not in position:
                    b=True
                    voisins.append(voisins[test]+taille-1)
                    position.append(voisins[test]+taille-1)
        
        
        #si c'est la dernière case
        elif voisins[test]==taille*taille-1:
            #contrôle droite
            d=True
            
            #contrôle gauche
            if matrice[voisins[test]-1]==a:
                if voisins[test]-1 not in position:
                    g=True
                    voisins.append(voisins[test]-1)
                    position.append(voisins[test]-1)
            
            #contrôle haut
            if matrice[voisins[test]-taille]==a:
                if voisins[test]-taille not in position:
                    h=True
                    voisins.append(voisins[test]-taille)
                    position.append(voisins[test]-taille)
            
            #contrôle bas
            b=True
            
        #si c'est la première ligne
        elif voisins[test] <= taille :   
            #contrôle droite
            if matrice[voisins[test]+1]==a:
                if voisins[test]+1 not in position:
                    d=True
                    voisins.append(voisins[test]+1)
                    position.append(voisins[test]+1)
            
            
            #contrôle gauche
            if matrice[voisins[test]-1]==a:
                if voisins[test]-1 not in position:
                    g=True
                    voisins.append(voisins[test]-1)
                    position.append(voisins[test]-1)
            
            #contrôle haut
            h=True
            
            #contrôle bas
            if matrice[voisins[test]+taille-1]==a:
                if voisins[test]+taille-1 not in position:
                    b=True
                    voisins.append(voisins[test]+taille-1)
                    position.append(voisins[test]+taille-1)
        
        #si c'est la dernière ligne 
        elif voisins[test] >= taille*taille - taille :
            #contrôle droite
            if matrice[voisins[test]+1]==a:
                if voisins[test]+1 not in position:
                    d=True
                    voisins.append(voisins[test]+1)
                    position.append(voisins[test]+1)
            
            #contrôle gauche
            if matrice[voisins[test]-1]==a:
                if voisins[test]-1 not in position:
                    g=True
                    voisins.append(voisins[test]-1)
                    position.append(voisins[test]-1)
            
            #contrôle haut
            if matrice[voisins[test]-taille]==a:
                if voisins[test]-taille not in position:
                    h=True
                    voisins.append(voisins[test]-taille)
                    position.append(voisins[test]-taille)
            
            #contrôle bas
            b=True
        
        #ailleurs
        else:
            #contrôle droite
            if matrice[voisins[test]+1]==a:
                if voisins[test]+1 not in position:
                    d=True
                    voisins.append(voisins[test]+1)
                    position.append(voisins[test]+1)
            
            #contrôle gauche
            if matrice[voisins[test]-1]==a:
                if voisins[test]-1 not in position:
                    g=True
                    voisins.append(voisins[test]-1)
                    position.append(voisins[test]-1)
            
            #contrôle haut
            if matrice[voisins[test]-taille]==a:
                if voisins[test]-taille not in position:
                    h=True
                    voisins.append(voisins[test]-taille)
                    position.append(voisins[test]-taille)
            
            #contrôle bas
            if matrice[voisins[test]+taille-1]==a:
                if voisins[test]+taille-1 not in position:
                    b=True
                    voisins.append(voisins[test]+taille-1)
                    position.append(voisins[test]+taille-1)
        
        ################
        if g and d and h and b :
            voisins2=voisins2[1:]
    
    #quand c'est finis, on mets à jours les cases qui seront contrôlé au prochain tour
    if len(voisins2)!=controle:
        voisins=voisins[len(voisins2)-1:]
        return etude(matrice,voisins,position,taille)
    print("v",voisins,"\n","pos",sorted(position),len(position))
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

#verif si une matrice est pleine
def controlage(matrice):
    for i in matrice:
        if matrice[0]!=i:
            return False
    return True
###zone de test###########################################################

#les infos obligatoires
matrice=[]
nb_couleur=6
taille=12
voisins = [0] #stocke les numéros des cases à contrôler
change = [0]


matrice=initialisation(taille,nb_couleur)
montre(taille,matrice)
a=time()
i=0
while len(change)!=taille*taille and i<10: # nombre de cases
    i+=1
    montre(taille, matrice)
    voisins,change = etude(matrice,voisins,change,taille)
    elem=i%6
    matrice = transition(matrice,change,elem)
    print()
    

#montre(taille, matrice)
print("Taille :",taille,"\nTemps de résolution :", time()-a)


#calcul des capacités du calculateur
for i in range(2,12):
    a=time()
    taille=i
    nb_couleur=6
    voisins = [0] #stocke les numéros des cases à contrôler
    change = [0]
    
    matrice=initialisation(taille,nb_couleur)
    
    i=0
    while len(change)!=taille*taille : # nombre de cases
        i+=1
        #print("n°",i)
        #montre(taille, matrice)
        voisins,change = etude(matrice,voisins,change,taille)
        elem=i%6
        #print()
        matrice = transition(matrice,change,elem)
    #montre(taille,matrice)
    print("Taille :",taille,"->", time()-a)


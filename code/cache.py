import os
import random
from copy import deepcopy

path=os.getcwd()

path=path[:-4]
path+="data/data.txt"

def color():
    path=os.getcwd()
    path=path[:-4]
    chemin=path+"/data/couleurs.txt"
    alea=random.randrange(0,368)
    with open(chemin,'r') as data:
        contenu=data.readlines()
    a= contenu[alea]
    return a

def niv_aléatoire():
    with open(path,'r') as data:
        num=int(data.readline(2),base=10)
        for i in range(random.randrange(1,20)):
            data.readline(200)
        return data.readline(200).rstrip("\n")
 
 #convertie une chaîne de string en matrice de niveau
def niveau():
    M=lecteur()
    niv=[]
    ligne=[]
    val=0
    M=M[1:]
    while M != "":
        if len(ligne)==6:
            niv.append(ligne)
            ligne=[]
            
        try:
            a=int(M[0],base=10)
            try:
                b=int(M[1],base=10)
                c=M[0]+M[1]
                ligne.append(c)
                M=M[2:]
            except:
                ligne.append(a)
                M=M[1:]
        except:
            chiffre=1
            M=M[1:]

    return niv
 
 
 

def lecteur():
    with open(path,'r') as data:
        num=int(data.readline(2),base=10)
        if num==21:
            return niv_aléatoire()
        for i in range(num):
            data.readline(200)
        return data.readline(200).rstrip("\n")
    
def lecture_ligne(niveau):
    with open(path,'r') as data:
        for i in range(niveau+1):
            data.readline(200)
        return data.readline(200).rstrip("\n")
    
    


def enregistreur(matrice):
    print(type(matrice))
    contenu=""
    compteur=0
    balise=1
    with open(path,'r') as data:
        contenu=data.readlines()
    num_lines = sum(1 for line in open(path))
    
    contenu=contenu[:num_lines-1]
    contenu+=matrice
    
    with open(path,'w') as data:
        while num_lines!=0:
            if num_lines==1:
                data.write(str(contenu))
            else:
                data.write(str(contenu[0]))
            contenu=contenu[1:]
            num_lines-=1


def ecriture(num_lines,contenu,ancien_niv):
    with open(path,'w') as data:
        cpt=1
        while num_lines!=0:
            if num_lines==1:
                data.write(str(contenu))
            elif cpt==ancien_niv+1:
                if contenu[0][0]=="F":
                    data.write(contenu[0])
                else:
                    data.write("F"+contenu[0])
            else:
                data.write(contenu[0])
            contenu=contenu[1:]
            num_lines-=1
            cpt+=1

def augmente_niv(niv):
        niv=str(niv)
        if len(niv)==1:
            niv="0"+niv+"\n"
        else:
            niv+="\n"
        return niv

def victoire(matrice):
    if matrice[2][5]==1:
        with open(path,'r') as data:
            niv=int(data.readline(2),base=10)
            ancien_niv=deepcopy(niv)
        with open(path,'r') as data:
            contenu=data.readlines()

        num_lines = sum(1 for line in open(path))
        
        niv+=1
        if niv==22:
            return "vic"
        if niv==21:
            niv=augmente_niv(niv)
            contenu=[niv]+contenu[1:]
            ecriture(num_lines,contenu,ancien_niv)
            return "vic"
        '''
        niv=str(niv)
        if len(niv)==1:
            niv="0"+niv+"\n"
        else:
            niv+="\n"
        '''
        niv=augmente_niv(niv)
        contenu=[niv]+contenu[1:]
        '''
        with open(path,'w') as data:
            cpt=1
            while num_lines!=0:
                if num_lines==1:
                    data.write(str(contenu))
                elif cpt==ancien_niv+1:
                    data.write("F"+contenu[0])
                else:
                    data.write(contenu[0])
                contenu=contenu[1:]
                num_lines-=1
                cpt+=1
        '''
        ecriture(num_lines,contenu,ancien_niv)
        return True


def deplacement(matrice,pos):
    #valeur=matrice[pos[0]][pos[1]]
    if pos[1]>=6 or pos[0]>=6 or matrice[pos[0]][pos[1]]==0:
        return matrice#,valeur

    def position(M,val):
        XY=[]
        if val != 0: #[0][0]:       
            for i in range(len(M)):
                for j in range (len(M[0])):
                    if M[i][j] == val:
                        XY.append([i,j])
            return XY      

    def sens(position):
        if position[0][0]==position[1][0]:
            return "horiz"
        else:
            return "verti"
    
    def bouge(sens,coordoClick,position):
        avant=False
        mouv = False
        if coordoClick== position[0]:
            avant = True
       
        #contrôle si le mouvement est possible et altération de la matrice
        if (sens=="verti" and avant ==True):
            try :
                mouv = matrice[coordoClick[0]-1][coordoClick[1]] == 0
                #pb avec [coordoClick[0]-1]-> retourne [-1]
                #print(mouv,sens,coordoClick,coordoClick[0]-1,matrice[coordoClick[0]-1][coordoClick[1]])
                if mouv and (coordoClick[0]-1!=-1):
                    
                    matrice[coordoClick[0]-1][coordoClick[1]] =matrice[coordoClick[0]][coordoClick[1]]
                    matrice[position[-1][0]][position[-1][1]] = 0
            except IndexError:
                return matrice#,valeur
           
        elif (sens=="verti" and avant ==False):
            try :
                mouv = matrice[position[-1][0]+1][position[-1][1]] == 0
                #print(mouv,sens,avant)
                if mouv:
                    matrice[position[-1][0]+1][position[-1][1]] = matrice[position[-1][0]][position[-1][1]]
                    matrice[position[0][0]][position[0][1]] = 0
            except IndexError:
                return matrice#,valeur
     
        elif (sens=="horiz" and avant ==True):
            try:
                mouv = matrice[coordoClick[0]][coordoClick[1]-1] == 0
                #pb avec [coordoClick[1]-1]-> retourne [-1]
                #print(mouv,sens,avant)
                if mouv and (coordoClick[1]-1!=-1):
                    matrice[coordoClick[0]][coordoClick[1]-1] = matrice[position[0][0]][position[0][1]]
                    matrice[position[-1][0]][position[-1][1]] = 0
                    
            except IndexError:
                return matrice#,valeur
            
        elif (sens=="horiz" and avant ==False):
            try:
                mouv = matrice[position[-1][0]][position[-1][1]+1] == 0
                #print(mouv,sens,avant)
                if mouv:
                    matrice[position[-1][0]][position[-1][1]+1] = matrice[position[-1][0]][position[-1][1]]
                    matrice[position[0][0]][position[0][1]] = 0
            except IndexError:
                return matrice#,valeur
        
    a=position(matrice,matrice[pos[0]][pos[1]])
    

    if pos[0]==a[1][0] and pos[1]==a[1][1] and len(a)==3: #contrôle du click, savoir si c'est au milieu de la voiture
        return matrice#,valeur
    
    #new_position=position(matrice,valeur)
    b=sens(a)
    c=bouge(b,pos,a)
    '''
    la première ligne sert de contrôle d'une éventuelle erreur d'entrée lors d'un click
    
    -position
        renvoie la liste des éléments de la voiture sur laquelle on a cliqué
    
    -sens
        avoir l'orientation
    
    -bouge
        construit en 2 temps
            -> premièrement où la variable "mouv" était renvoyé, ie test si la case "devant" est libre
            -> enfin, on a ajouté le déplacement
    
    Pour que cela marche : 
        -une matrice de niveau       => matrice
        -coordonnées du click souris => pos
        
    (pensez à mettre les coordonnées en: int
                                         //6)
    '''
    return matrice#,new_position
'''            
matrice=[[0,0,0, 4, 4,12],[0,0,0, 0, 3,12],[1,1,0, 0, 3,12],[0,0,9,11,11,11],[2,0,9, 0, 0, 0],[2,0,9,10,10,10]]
print(matrice)
pos=[0,1]
print(matrice[pos[0]][pos[1]])
print(deplacement(matrice,pos))

M=[[0,0,0,4,4,12],[0,0,0,0,3,12],[0,1,1,0,3,12],[0,0,9,11,11,11],[2,0,9,0,0,0],[2,0,9,10,10,10]]
L=[[4, 0], [4, 0]]#, [2, 4], [4, 0], [4, 0], [4, 0], [4, 0], [3, 0], [3, 0], [4, 0], [3, 0], [3, 0], [4, 0], [5, 0]] #, [3, 0], [2, 2], [0, 3], [0, 2], [0, 2], [0, 3], [0, 3], [0, 2], [0, 1], [0, 1], [0, 2], [0, 3], [3, 0], [3, 0], [3, 0], [3, 0], [3, 0], [4, 0], [3, 0], [4, 0]]

def affiche(M):
    for i in range(6):
        print(M[i])
    print()
affiche(M)
for i in L:
    print(i)
    affiche(deplacement(M,i))
'''








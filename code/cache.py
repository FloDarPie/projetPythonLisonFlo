import os
import random
from copy import deepcopy

path=os.getcwd()

path=path[:-4]
path+="data/data.txt"

#renvoie le niveau en cours
def numero():
    with open(path,'r') as data:
        num=int(data.readline(2),base=10)
        return num

#prend une couleur de manière aléatoire du fichier COULEUR
def color():
    path=os.getcwd()
    path=path[:-4]
    chemin=path+"/data/couleurs.txt"
    alea=random.randrange(0,368)
    with open(chemin,'r') as data:
        contenu=data.readlines()
    a= contenu[alea]
    return a

#renvoie le scoring depuis la base de donnée des scores
def score(numero):
    with open(path[:-8]+"score.txt",'r') as data:
        for i in range(numero):
            data.readline(7)
        score= data.readline(7).rstrip("\n")
    print(score)
    return [score[:-3],score[3:]]

def information_niveau():
        
    a = numero()
    print(a)
    
    if a==1:
        coul = "turquoise1"
        classification = "tuto"
    if a > 1 :
        coul = "SeaGreen1"
        classification =  "très facile"
    if a > 6:
        coul = "green"
        classification =  "facile"
    if a > 12:
        coul = "orange"
        classification =  "moyen"
    if a>17:
        coul = "red"
        classification =  "difficile"

    chiffre = score(a)
    print(chiffre)
    '''
    meilleur_score = chiffre[0]
    score_joueur = chiffre[1]
    '''
    if chiffre[1]=="XX":
        return [chiffre[0], "Non établi",coul,classification,str(a)]
    
    return [chiffre[0], chiffre[1],coul,classification,str(a)]


#renvoie un niveau aléatoire de la base de donnée
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
 

 



#mise à jour de la base de donnée des scores
def enregistre_score(ligne,score):
    if score > 99:
        score = "X"
    elif score <10:
        score = "0"+str(score)
    else:
        score=str(score)
    with open(path[:-8]+"score.txt",'w') as data:
        contenu = data.readlines()
    with open(path[:-8]+"score.txt",'r') as data:
        for i in range(ligne):
            if i==ligne:
                data.write(contenu[0][:-3]+score)
            else:
                data.write(contenu[0])
            contenu=contenu[1:]
        while contenu !="":
            data.write(contenu[0])
            contenu=contenu[1:] 

#lit le niveau et le renvoie sous forme de STRING
def lecteur():
    with open(path,'r') as data:
        num=int(data.readline(2),base=10)
        if num==21:
            return niv_aléatoire()
        for i in range(num):
            data.readline(200)
        return data.readline(200).rstrip("\n")


#lit une ligne en particulier //INUTILISÉ
def lecture_ligne(niveau):
    with open(path,'r') as data:
        for i in range(niveau+1):
            data.readline(200)
        return data.readline(200).rstrip("\n")
    
    

#enregistre le dernier mouvement sur la dernière ligne du fichier
def enregistreur(matrice):
    #print(type(matrice))
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

#enregistre lorsque le niveau est complété
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

#change le niveau en respectant les codes du fichier
def augmente_niv(niv):
        niv=str(niv)
        if len(niv)==1:
            niv="0"+niv+"\n"
        else:
            niv+="\n"
        return niv

#lorsqu'un niveau est termine, applique les changements nécessaires
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

        niv=augmente_niv(niv)
        contenu=[niv]+contenu[1:]

        ecriture(num_lines,contenu,ancien_niv)
        return True
    
def change_niveau(chiffre):
    a = augmente_niv(chiffre)
    with open(path,'r') as data:
        contenu = data.readlines()
    with open(path,'w') as data:
        data.write(a)
        contenu=contenu[1:]
        while contenu!="":
            data.write(contenu[0])
            contenu=contenu[1:]
    
    

def reinitialise():
    with open(path,'r') as data:
        contenu=data.readlines()
    cpt=1
    contenu=contenu[1:]
    with open(path,'w') as data:
        while cpt!=22:
            if cpt==1:
                data.write("01\n")
            elif cpt==21:
                data.write("X")
            else:
                if contenu[0][0]=="F":
                    data.write(contenu[0][1:])
                else:
                    data.write(contenu[0])
                contenu=contenu[1:]
            cpt+=1
    with open(path[:-8]+"score.txt",'r') as data:
        score = data.readlines()
    
    with open(path[:-8]+"score.txt",'w') as data:
        while score !="":
            data.write(str(score[0][:-3])+"XX\n")
            score=score[1:]
    #print("fin réinitialisation")
            
#renvoie la liste des positions sur laquelle la voiture a été cliqué
def position(M,val):
    XY=[]
    if val != 0: #[0][0]:       
        for i in range(len(M)):
            for j in range (len(M[0])):
                if M[i][j] == val:
                    XY.append([i,j])
        return XY 

#gestion de la matrice du niveau, renvoie une matrice 
def deplacement(matrice,pos):
    #valeur=matrice[pos[0]][pos[1]]
    if pos[1]>=6 or pos[0]>=6 or matrice[pos[0]][pos[1]]==0:
        return matrice#,valeur

     #position

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









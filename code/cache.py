import os

path=os.getcwd()

path=path[:-4]
path+="data/data.txt"


def lecteur():
    with open(path,'r') as data:
        num=int(data.readline(2),base=10)
        for i in range(num-1):
            data.readline(200)
        return data.readline(200)

def enregistreur(matrice):
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





def deplacement(matrice,pos):
    if pos[1]>=6 or pos[0]>=6 or matrice[pos[0]][pos[1]]==0:
        return matrice
    
    def position(M,val):
        XY=[]
        if val != 0: #[0][0]:       
            for j in range(len(M)):
                for i in range (len(M[0])):
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
                print("=========")
                mouv = matrice[coordoClick[0]-1][coordoClick[1]] == 0
                
                matrice[coordoClick[0]-1][coordoClick[1]] =matrice[coordoClick[0]][coordoClick[1]]
                matrice[position[-1][0]][position[-1][1]] = 0
            except IndexError:
                return matrice
           
        elif (sens=="verti" and avant ==False):
            try :
                mouv = matrice[position[-2][0]][position[-1][1]] == 0
                
                matrice[position[-2][0]][position[-1][1]] = matrice[position[-1][0]][position[-1][1]]
                matrice[position[0][0]][position[0][1]] = 0
            except IndexError:
                return matrice
     
        elif (sens=="horiz" and avant ==True):
            try:
                mouv = matrice[coordoClick[0]][coordoClick[1]-1] == 0
                
                matrice[coordoClick[0]][coordoClick[1]-1] = matrice[position[0][0]][position[0][1]]
                matrice[position[-1][0]][position[-1][1]] = 0
                
            except IndexError:
                return matrice
            
        elif (sens=="horiz" and avant ==False):
            try:
                mouv = matrice[position[-1][0]][position[-1][1]+1] == 0
                
                matrice[position[-1][0]][position[-1][1]+1] = matrice[position[-1][0]][position[-1][1]]
                matrice[position[0][0]][position[0][1]] = 0
            except IndexError:
                return matrice
        return matrice

    a=position(matrice,matrice[pos[0]][pos[1]])
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
    return matrice
'''            
matrice=[[0,0,0, 4, 4,12],[0,0,0, 0, 3,12],[1,1,0, 0, 3,12],[0,0,9,11,11,11],[2,0,9, 0, 0, 0],[2,0,9,10,10,10]]
print(matrice)
pos=[0,1]
print(matrice[pos[0]][pos[1]])
print(deplacement(matrice,pos))
'''



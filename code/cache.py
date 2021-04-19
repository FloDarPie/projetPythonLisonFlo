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
            
matrice=[[0,0,0,4,4,12],
         [0,0,0,0,3,12],
         [1,1,0,0,3,12],
         [0,0,9,11,11,11],
         [2,0,9,0,0,0],
         [2,0,9,10,10,10]]
pos=[1,1]
print(matrice[pos[0]][pos[1]])



def deplacement(matrice,pos):
    if pos[1]>=6 or pos[0]>=6 or matrice[pos[0]][pos[1]]==0:
        return matrice
    
    def position(M,val):
        XY=[]
        if val != [0][0]:       
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
    
    def verif(sens,coordoClick,position):
        avant=False
        mouv = False
        if coordoClick== position[0]:
            avant = True
        
        if (sens=="verti" and avant ==True):
            try :
                mouv = (matrice[coordoClick[0]][coordoClick[1]-1] == 0)
            except IndexError:
                return mouv
            
        elif (sens=="verti" and avant ==False):
            try :
                mouv = matrice[position[len(position)-1][0]][position[len(position)-1][1]+1] ==0
            except IndexError:
                return mouv
            
        elif (sens=="horiz" and avant ==True):
            try:
                mouv = matrice[coordoClick[0]-1][coordoClick[1]] ==0
            except IndexError:
                return mouv
            
        elif (sens=="horiz" and avant ==False):
            try:
                mouv = matrice[position[len(position)][0]][position[len(position)-1][1]] ==0
            except IndexError:
                return mouv
        return mouv
        #fin
    
    a=position(matrice,matrice[pos[0]][pos[1]])
    b=sens(a)
    
    c=verif(b,pos,a)
    
    print(a)
    print(b)
    print(c)
    
    return "ok"
    
print(deplacement(matrice,pos))
print("fin")

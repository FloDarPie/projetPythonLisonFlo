
import numpy as np

#générer une matrice 6x6 qui est pleine de voiture

#6*6
 
L1 = [0,2,2,0,0,0]
L2 = [0,0,0,3,3,3]
L3 = [0,0,0,0,0,4]
L4 = [0,1,0,0,0,4]
L5 = [0,1,0,5,5,0]
L6 = [0,1,0,0,0,0]

matrix = np.array([L1,L2,L3,L4,L5,L6])

#récupérer la valeur de la case avec un click souris

click = matrix[3][1] #en attendant

#récupérer la position de la voiture entière
def position(M,val):
    XY=[]
    if val != [0][0]:       
        for i in range(len(M)):
            for j in range (len(M[0])):
                if M[i][j] == val:
                    XY.append([i,j])
        return XY

test = position(matrix,click)

print( test)    #[[3, 1], [4, 1], [5, 1]]

#déterminer le sens ==> vertical ou horizontal
def sens(position):
    if position[0][0]==position[1][0]:
        return "horiz"
    else:
        return "verti"

test2 = sens(position(matrix,click))
print ("sens",test2)    #verti

#vérifier qu'il y a de la place => vérifier que la case "devant" égale à 0

coordoClick = [5,1]

def verif(sens,coordoClick,position):
    avant=False
    mouv = False
    if coordoClick== position[0]:
        avant = True
    print("avant",avant)
    
    if (sens=="verti" and avant ==True):
        try :
            mouv = matrix[coordoClick[0]][coordoClick[1]-1] ==0
            return mouv
        except IndexError:
            pass
        
    elif (sens=="verti" and avant ==False):
        try :
            mouv = matrix[position[len(position)-1][0]][position[len(position)-1][1]+1] ==0
            return mouv
        except IndexError:
            
        
    elif (sens=="verti" and avant ==True):
        try:
            mouv = matrix[coordoClick[0]-1][coordoClick[1]] ==0
        except IndexError:
            return mouv
        
    elif (sens=="verti" and avant ==False):
        try:
            mouv = matrix[position[len(position)][0]][position[len(position)-1][1]] ==0
        except IndexError:
            return mouv
    else:
        pass
        
    return mouv
            


print("mouv",verif(test2,coordoClick,position(matrix,click)))

#effectuer le déplacement

from tkinter import *

def f(event):
    t=event.keysym
    print("Touche pressée :", t)


root = Tk()

root.bind("<Key>", f)

root.mainloop()

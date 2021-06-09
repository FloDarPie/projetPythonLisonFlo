from module_partie import Partie 
from module_vehicule import Vehicule
from module_fenetre_partie import FenetrePartie
from tkinter import*
from gestion_son import Musique
from random import randint
from copy import deepcopy
from time import time

#date 13/05 a 15h

def redondant(M:list,etats:list):
    return M in etats

def equivalent(dep:list, num : int, bouge : int):
    return (num,bouge) in dep 

def nouvelles_equivalences (dep : list, num : int, move : int, M : list, vehicules : list):
    if dep==[]:
        return [(num,move)]
    else :
        ndep=[]
        
        for n,d in dep:
            vehicule = vehicules[n-1]
            y1,x1=vehicule.coor()
            ver=vehicule.est_verticale()
            y2,x2=(y1+vehicule.longueur()-1,x1) if ver else (y1,x1+vehicule.longueur()-1)
            
            if d==-1:
                if ( (ver and y2!=5) or (not ver and x2!=5) ) and M[y2+ver][x2+(not ver)]==0:
                    ndep.append( (n, d) )
                    
            else :
                if ( (ver and y2!=0) or (not ver and x2!=0) ) and M[y1-ver][x1-(not ver)]==0:
                    ndep.append( (n, d) )
        
        return ndep + [(num, move)]

def Position_Depart(M:list, nbCoup:int, lim:int, nbVoit: int, etats: list, vehicules : list, dep : list, sol : list):
    if nbCoup>= lim and M[3][1]==1 and M[3][2]==1  : #On a une configuration intiale "suffisamment" mélangée
        print(nbCoup)
        return [M,nbCoup]
    else :
        #if nbCoup%10==0:
            #print(nbCoup, ":")
            #print("---")
            
        """#On cherche à déplacer la voiture 1 vers sa position de départ (se trouvant derrière lui)
        i = M[3].index(1)
        while i > 1 and M[3][i-1]==0 :
            M[3][i+1]=0
            M[3][i-1]=1
            i-=1"""
        
        for k in range(1,nbVoit+1) :
            vehicule=vehicules[k-1]
            y1,x1=vehicule.coor()
            ver=vehicule.est_verticale()
            y2,x2=(y1+vehicule.longueur()-1,x1) if ver else (y1,x1+vehicule.longueur()-1)
            
            vehicule.avancer()
            y,x=vehicule.coor()
            if (y,x)!=(y1,x1): #Gestion du bord
                #print("A")
                if M[y2+ver][x2+(not ver)]==0: #Gestion d'une collision
                    #print("B")
                    M[y1][x1]=0
                    M[y2+ver][x2+(not ver)]=k
                    if not (redondant(M,etats) or equivalent(dep, k, 1)):
                        #print("C")
                        ndep = nouvelles_equivalences(dep, k, 1, M, vehicules)
                        etats.append(deepcopy(M))
                        Mf=Position_Depart(M,nbCoup+1,lim,nbVoit,etats,vehicules, ndep, sol)
                        """for x in Mf[0]:
                            print(x)
                        print("--------------------------")"""
                        if Mf[1]>sol[1]:
                            sol[:]=[x for x in Mf]
                        elif Mf[1]==sol[1] and Mf[0][3][3:].count(0)<sol[0][3][3:].count(0):
                            sol[:]=[x for x in Mf]
                        
                    M[y2+ver][x2+(not ver)]=0
                    M[y1][x1]=k
                vehicule.reculer()
                
            vehicule.reculer()
            y,x=vehicule.coor()
            if (y,x)!=(y1,x1): #Gestion du bord
                #print("D")
                if M[y][x]==0: #Gestion d'une collision
                    #print("E")
                    M[y][x]=k
                    M[y2][x2]=0
                    if not (redondant(M,etats) or equivalent(dep, k, -1)):
                        #print("F")
                        ndep = nouvelles_equivalences(dep, k, -1, M, vehicules)
                        etats.append(deepcopy(M))
                        Mf=Position_Depart(M,nbCoup+1,lim,nbVoit,etats,vehicules, ndep, sol)
                        if Mf[1]>sol[1]:
                            sol[:]=[x for x in Mf]
                        elif Mf[1]==sol[1] and Mf[0][3][3:].count(0)<sol[0][3][3:].count(0):
                            sol[:]=[x for x in Mf]
                        
                    M[y2][x2]=k
                    M[y][x]=0
                vehicule.avancer()
            #print(nums)
    return sol


   
def creer_Partie(M:list):
    voitures=[]
    numero=[]
    N=6
    for y in range(N):
        for x in range(N):
            num=M[y][x]
            if num>0 and num not in numero:
                k=M[y].count(num)
                numero.append(num)
                if k==1:
                    voitures.append(Vehicule((y,x),"V",3 if y<N-2 and num==M[y+2][x] else 2,num))
                else :
                    voitures.append(Vehicule((y,x),"H",k,num if y!=3 else 1))
    T=sorted(list(voitures),key=Vehicule.num)

    return Position_Depart(M,0,10,max([max(L) for L in M]),[],T,[],[[[0 for x in range(6)] for y in range(6)], 0])             


M=[ [0,0,7,7,7,0],
    [0,0,0,6,6,0],
    [5,4,0,0,0,0],
    [5,4,3,1,1,2],
    [0,4,3,0,0,2],
    [0,0,8,8,0,0],
    ]

t=time()
A=creer_Partie(M)[0]
print(time()-t)

for x in A :
    print(x)

test=Tk()
Musique()
Musique.pause()

if A is not None :
    laPremierePartie=FenetrePartie(A,test)
    laPremierePartie.afficher()
else :
    print("pouet")

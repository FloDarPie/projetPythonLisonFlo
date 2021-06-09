from module_partie import Partie, Move
from module_vehicule import Vehicule
from module_fenetre_partie import FenetrePartie
from tkinter import*
from gestion_son import Musique
from random import randint
from copy import deepcopy
from time import time

#date 16/05 15h


def redondant(M:list,etats:list):
    return M in etats

def Position_Depart(M:list, nbCoup:int, nbVoit: int, etats: list, vehicules : list, sol : list, solpar : list):
    
    if sol != None and nbCoup>=len(sol): #Solution ayant plus de mouvement que la solution trouvé
        return sol
    #if nbCoup%10==0:
        #print(nbCoup, ":")
        #print("---")

    if est_solution(M)  : #On a trouvé une solution ayant moins de coup que précédement (ou on a trouvé la première)
        #print(nbCoup)
        return solpar
    

    """#On cherche à déplacer la voiture 1 vers sa position de départ (se trouvant derrière lui)
    i = M[3].index(1)
    while i > 1 and M[3][i-1]==0 :
        M[3][i+1]=0
        M[3][i-1]=1
        i-=1"""
    
    """for x in M:
        print(x)
    print("-----------------------------------------------------")"""
    
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
                if not redondant(M,etats):
                    #print("C")
                    
                    etats.append(deepcopy(M))
                    sol[:]=resoudre(M,nbCoup+1,nbVoit,etats,vehicules, sol, solpar+[Move(k,1)])
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
                if not redondant(M,etats) :
                    #print("F")
                   
                    etats.append(deepcopy(M))
                    sol[:]=resoudre(M,nbCoup+1,nbVoit,etats,vehicules, sol, solpar+[Move(k,-1)])   
                M[y2][x2]=k
                M[y][x]=0
            vehicule.avancer()
        #print(nums)
        
    
    return sol


   
def solution(M:list):
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

    S1 = resoudre(M,0,max([max(L) for L in M]),[],T,None, [])  

    S=[]

    i = 0

    while i < len(S1) :
        m=S1[i]
        k=1
        while i+1 < len(S1) and S1[i]==S1[i+1]:
            i+=1
            k+=1
        
        S.append(Move(m.mouvement()[0],k*m.mouvement()[1]))

        i+=1
    
    return S
           


M=[ [0,4,7,7,7,0],
    [0,4,0,6,6,0],
    [5,4,0,0,9,0],
    [5,1,1,0,9,2],
    [10,10,3,0,9,2],
    [0,0,3,8,8,0],
    ]


test=Tk()
Musique()
Musique.pause()

if M is not None and M != [[0 for x in range(6)] for y in range(6)]:
    laPremierePartie=FenetrePartie(M,test)
    laPremierePartie.afficher()

    for x in solution(M):
        print(x)
else :
    print("pouet")

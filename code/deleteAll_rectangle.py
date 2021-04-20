from tkinter import *
import random
from cache import *
import os


#voiture de 2 à 8 et camion de 9 à 13


def niveau():
    M=lecteur()
    niv=[]
    ligne=[]
    val=0
    while M != "":
        if len(ligne)==6:
            niv.append(ligne)
            ligne=[]
            
        chiffre=1
        if M[0]=="," or M[0]=="[" or M[0]=="]":
            M=M[1:]
        
        if int(M[0],base=10)>=0:
            chifre+=1
            val+=M[0]
        if M[1]=="," or M[1]=="]":
            ligne.append(val)
            val=0
            M=M[1:]
        print(val,ligne)
        return niv
    
    print(type([[0,2,3,3,4,4],[0,2,0,0,5,5],[1,1,0,0,11,6],[9,10,10,10,11,6],[9,0,0,0,11,7],[9,0,0,0,0,7]]))
    print(list(M))
M=niveau()

path=os.getcwd()
path=path[:-4]
chemin=path+"/data/couleurs.txt"
path+="/assets/"



#PARAMETRES
COTE=100

NB_COL=6
NB_LIG=6

LARG=NB_COL*COTE
HAUT=NB_LIG*COTE

AUTRE=LARG/6
DIM=LARG

fen=Tk()
fen .title("Parking")
canv=Canvas(fen, width=LARG, height=HAUT, background="gray")
canv.pack()

#ajouter image background
parking=PhotoImage(file=path+"images/parking_fond.png")

#sortie du parking
SORTIE=canv.create_line((LARG+5,2*(LARG/6)),(LARG+5,3*(LARG/6)), fill="red", width=12)

#affiche background par rapport à son centre
centre=(DIM/2,DIM/2)
canv.create_image(centre, image=parking)

comp=0
n=len(M)
n2=len(M[0])
x=color().rstrip("\n")


#récupérer la position de la voiture entière
def position(M,val):
    XY=[]
    if val != 0:       
        for j in range(len(M)):
            for i in range (len(M[0])):
                if M[j][i] == val:
                    XY.append([i,j])
        return XY

comp=0
n=len (M)
n2=len(M[0])

VOITUREB=0
RECT=0
RECT2=0

N=[]
#colors=['black', 'red', 'green', 'blue', 'cyan', 'yellow']
#coul=random.randrange(len(colors))

#placer les voitures/camions rectangulaires de la matrice
def affichage(M) :
    global n2,comp,RECT,RECT2,VOITUREB,x
    L={}
    for i in range(n):
        for j in range(n2):
            if M[i][j] !=0:
                if M[i][j]==1:
                    VOITUREB=canv.create_rectangle(j*AUTRE,i*AUTRE,j*AUTRE+AUTRE,i*AUTRE+AUTRE,fill="black")
                else:
                    XY=position(M,M[i][j])
                    try:
                        L[M[i][j]]==1
                    except:
                        L[M[i][j]]=1
                        RECT=canv.create_rectangle(AUTRE*XY[0][0],AUTRE*XY[0][1],AUTRE*((XY[-1][0])+1),AUTRE*((XY[-1][1])+1),fill=x)
                        RECT2=canv.create_rectangle(AUTRE*XY[0][0],AUTRE*XY[0][1],AUTRE*((XY[-1][0])+1),AUTRE*((XY[-1][1])+1))
                        

affichage(M)         

def genererFen():
    canv.create_image(centre, image=parking)
    canv.create_line((LARG+5,2*(LARG/6)),(LARG+5,3*(LARG/6)), fill="red", width=12)



def clic(event):
    global M,truc,RECT,RECT2,VOITUREB,centre,parking
    canv.delete("all")
    a=(event.x,event.y)
    M=deplacement(M,[int(a[1])//100,int(a[0])//100])
    genererFen()
    affichage(M)

'''

def clic(event):
    global posi,M,truc,RECT,RECT2,VOITUREB,centre,parking
    a=(event.x,event.y)
    posi=[int(a[1])//100,int(a[0])//100]
    L=deplacement(M,posi)
    new_posi=L[1].pop(posi)
    canv.move(a,new_posi)
    genererFen()
    affichage(L[0])
    truc.append(posi)
    print(truc)


'''
canv.bind("<Button-1>", clic)
#RECTANGLE : canv.create_rectangle(x,y,x1,y1,fill="magenta")
#ENLEVER RECTANGLE : 


fen.mainloop()

fen.protocol("WM_DELETE_WINDOW",fen.destroy())



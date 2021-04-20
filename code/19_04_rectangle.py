from tkinter import *
from cache import *
import os

#voiture de 2 à 8 et camion de 9 à 13
M=[[0,0,0,4,4,12]
,[0,0,0,0,3,12]
,[0,0,1,1,3,12]
,[0,0,9,11,11,11]
,[2,0,9,0,0,0]
,[2,0,9,10,10,10]]


path=os.getcwd()
print(path)
path=path[:-4]
path+="/assets/"

print(path)

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
canv.pack(padx=10, pady=10)

#sortie du parking
canv.create_line((LARG,2*(LARG/6)),(LARG,3*(LARG/6)), fill="red", width=12)

#ajouter image background
parking=PhotoImage(file=path+"images/parking_fond.png")

#affiche background par rapport à son centre
centre=(DIM/2,DIM/2)
canv.create_image(centre, image=parking)

comp=0
n=len (M)
n2=len(M[0])
#Placer la voiture qui sort

for i in range (n):
    L=M[i]
    n2=len (L)
    for j in range (n2):
        if L[j]==1 and comp==0:
            comp+=1
            voitureBouge=canv.create_rectangle(j*AUTRE,i*AUTRE,j*AUTRE+2*AUTRE,i*AUTRE+AUTRE,fill="magenta")



#récupérer la position de la voiture entière
def position(M,val):
    XY=[]
    if val != 0:       
        for j in range(len(M)):
            for i in range (len(M[0])):
                if M[j][i] == val:
                    XY.append([i,j])
        return XY


#placer les voitures/camions rectangulaires de la matrice
def affichage(M) :
    L={}
    for i in range(n):
        for j in range(n2):
            if M[i][j] !=0 and M[i][j]!=1:
                XY=position(M,M[i][j])
                try:
                    L[M[i][j]]==1
                except:
                    L[M[i][j]]=1
                    canv.create_rectangle(AUTRE*XY[0][0],AUTRE*XY[0][1],AUTRE*((XY[-1][0])+1),AUTRE*((XY[-1][1])+1),fill="red")
                    canv.create_rectangle(AUTRE*XY[0][0],AUTRE*XY[0][1],AUTRE*((XY[-1][0])+1),AUTRE*((XY[-1][1])+1))

affichage(M)         

truc=[]
posi=[]
def clic(event):
    global posi,M,truc
    a=(event.x,event.y)
    
    posi=[int(a[0])//100,int(a[1])//100]
    M=(deplacement(M,posi))
    affichage(M)
    truc.append(posi)
    print(truc)
canv.bind("<Button-1>", clic)



#RECTANGLE : canv.create_rectangle(x,y,x1,y1,fill="magenta")
#ENLEVER RECTANGLE : 


fen.mainloop()

fen.protocol("WM_DELETE_WINDOW",fen.destroy())



from tkinter import *
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
PAD=5
SIDE=COTE+2*PAD

NB_COL=6
NB_LIG=6

LARG=NB_COL*SIDE
HAUT=NB_LIG*SIDE

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


def excep(M,i,j):
    XY=position(M,M[i][j])
    #ajouter image
    voitures2=PhotoImage(file=path+"image_gif/6.gif")
    centre2=(400,00)
    canv.create_image(centre2, image=voitures2)
    if XY[0][0]==XY[1][0]:
        voitures=PhotoImage(file=path+"image_gif/7hor.gif")
        centre1=((AUTRE*XY[0][0]+AUTRE*((XY[-1][0])+1))/2,(AUTRE*XY[0][1]+AUTRE*((XY[-1][1])+1))/2)
        canv.create_image(centre1, image=voitures)
        print(((AUTRE*XY[0][0]+AUTRE*((XY[-1][0])+1))/2,(AUTRE*XY[0][1]+AUTRE*((XY[-1][1])+1))/2))
    else:
        voitures2=PhotoImage(file=path+"image_gif/4.gif")
        centre2=((AUTRE*XY[0][0]+AUTRE*((XY[-1][0])+1))/2,(AUTRE*XY[0][1]+AUTRE*((XY[-1][1])+1))/2)
        canv.create_image(centre2, image=voitures2)
        print("hello")

#placer les voitures/camions de la matrice
def affichage(M) :
    L={}
    for i in range(n):
        for j in range(n2):
            if M[i][j] !=0 and M[i][j]!=1:
                try:
                    L[M[i][j]]==1
                except:
                    L[M[i][j]]=[1,]
                    excep(M,i,j)
                    '''
                    canv.create_rectangle(AUTRE*XY[0][0],AUTRE*XY[0][1],AUTRE*((XY[-1][0])+1),AUTRE*((XY[-1][1])+1),fill="red")
                    canv.create_rectangle(AUTRE*XY[0][0],AUTRE*XY[0][1],AUTRE*((XY[-1][0])+1),AUTRE*((XY[-1][1])+1))
                    '''
    
affichage(M)


#RECTANGLE : canv.create_rectangle(x,y,x1,y1,fill="magenta")
#ENLEVER RECTANGLE : 

voitures2=PhotoImage(file=path+"images/images modif/5.gif")
centre2=(400,400)
canv.create_image(centre2, image=voitures2)

fen.mainloop()

fen.protocol("WM_DELETE_WINDOW",fen.destroy())



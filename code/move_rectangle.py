from tkinter import *
import tkinter.font as font
import random
from cache import *
import os


#voiture de 2 à 8 et camion de 9 à 13
M1=[[0,0,0,0,0,0]
,[0,0,0,0,0,0]
,[0,1,1,0,0,0]
,[0,0,0,0,0,0]
,[0,0,0,0,0,0]
,[0,0,0,0,0,0]]

path=os.getcwd()
path=path[:-4]
chemin=path+"/data/couleurs.txt"
path+="/assets/"

#PARAMETRES_FENETRE_TAILLE
COTE=100
NB_COL=6
NB_LIG=6

LARG=NB_COL*COTE
HAUT=NB_LIG*COTE

AUTRE=LARG/6
DIM=LARG

#PARAMETRES_FONCTIONS
comp=0
n=len (M1)
n2=len(M1[0])

VOITUREB=0
RECT=0
RECT2=0


text1="OBJECTIF : faites sortir la voiture de police du parking sans créer d'accidents."
text2="REGLES DU JEU : faites avancer ou reculer les véhicules afin de libérer la voie à la voiture de police. Essayez d'y parvenir en le moins de coup possible !"
text3="Si vous êtes bloqués, appuyez sur le solveur pour avoir la solution."
text4="Pour quitter le jeu, appuyez sur le bouton quitter."
text5="Attention ! Pour passer au niveau suivant, il faut terminer le niveau en cours."
text6="Bonne chance !"

textintro="Cliquer à l'avant de la voiture pour l'avancer et à l'arrière pour la reculer"

posi=[]
N=[]

#PARAMETRES_FENETRE
fen=Tk()
fen.title("Parking")
canv=Canvas(fen, width=LARG, height=HAUT)
canv.pack(side=LEFT)

#ajouter image background
parking=PhotoImage(file=path+"images/parking_fond.png")
logo=PhotoImage(file=path+"images/logo_rushHour2.png")
#affiche background par rapport à son centre
centre=(DIM/2,DIM/2)
canv.create_image(centre, image=parking)


#tentative de Flo pour rajouter le logo avant qu'il aille au dodo
canv2=Canvas(fen, width=LARG/2.5+50, height=HAUT/2.5)
canv2.pack()
joli=PhotoImage(file=path+"images/logo_rushHour_corner.png")
#affiche background par rapport à son centre
centre2=(DIM/4,DIM/4)
canv2.create_image(centre2, image=joli)

#sortie du parking
SORTIE=canv.create_line((LARG+5,2*(LARG/6)),(LARG+5,3*(LARG/6)), fill="red", width=12)

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
    global n2,comp,RECT,RECT2,VOITUREB
    x=color().rstrip("\n")
    L={}
    for i in range(n):
        for j in range(n2):
            if M[i][j] !=0:
                if M[i][j]==1:
                    VOITUREB=canv.create_rectangle(j*AUTRE,i*AUTRE,j*AUTRE+AUTRE,i*AUTRE+AUTRE,fill="black")
                    N.append(VOITUREB)
                else:
                    XY=position(M1,M1[i][j])
                    try:
                        L[M[i][j]]==1
                    except:
                        L[M[i][j]]=1
                        RECT=canv.create_rectangle(AUTRE*XY[0][0],AUTRE*XY[0][1],AUTRE*((XY[-1][0])+1),AUTRE*((XY[-1][1])+1),fill=x)
                        RECT2=canv.create_rectangle(AUTRE*XY[0][0],AUTRE*XY[0][1],AUTRE*((XY[-1][0])+1),AUTRE*((XY[-1][1])+1))
                        N.append(RECT)
                        N.append(RECT2)
def effacer(N):
    for i in N:
        canv.delete(i)


def victory(M):
    global canv
    if M[2][5]==1:
        canv.create_rectangle(0,0,LARG,HAUT,fill='green3')
        canv.create_text(LARG//2,HAUT//2,text="VICTOIRE !",fill='white',font="Arial 50 roman")
         

def clic(event):
    global posi,M1,N
    a=(event.x,event.y)
    effacer(N)
    posi=[int(a[1])//100,int(a[0])//100]
    M1=deplacement(M1,posi) 
    affichage(M1)
    victory(M1)

#GESTION DES BOUTONS
def recommencer():
    pass

def quitter():
    fen.destroy()

def solveur(): 
    global f,fen,logo
    POPUP = Toplevel()
    x=fen.winfo_x()
    y=fen.winfo_y()

    POPUP.geometry("+%d+%d" % (x+100,y+200))

    
    POPUP.title('Désolé...(ou pas)')
    POPUP.minsize(height=100,width=300)
    Button(POPUP, text='En cours de production...',activebackground='SteelBlue4',height=3,width=30,font=f,command=POPUP.destroy).pack(anchor=NW,padx=10, pady=10)
    POPUP.transient(fen)
    POPUP.grab_set()

    canvas=Canvas(POPUP,width=100,height=56)
    canvas.pack()
    canvas.create_image(50,28,image=logo)


    fen.wait_window(POPUP)


def fermer():
    pass
'''
class Bouton:
    def __init__(self,window,color,text,height,width,command):
        self.w=window
        self.c=color
        self.t=text
        self.h=height
        self.w=width
        self.co=command
        self.tricks=[]

    def add_trick(self, trick):
        self.tricks.append
'''


#LANCEMENT DES FONCTIONS
f=font.Font(size=15)


btn2=Button(fen,activebackground='IndianRed3', text="Quitter",height=3,width=15,command=quitter,font=f).pack(side=BOTTOM,padx=10, pady=10)

btn=Button(fen,activebackground='lightBlue1', text="Recommencer",height=3,width=15,command=recommencer,font=f).pack(side=BOTTOM,padx=10, pady=10)

btn3=Button(fen,activebackground='green', text="Solveur",height=3,width=15,command=solveur,font=f).pack(side=BOTTOM,padx=10, pady=10)

victory(M1)

affichage(M1) 

canv.bind("<Button-1>", clic)

fen.mainloop()

fen.protocol("WM_DELETE_WINDOW",fen.destroy())



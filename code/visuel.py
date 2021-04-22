from tkinter import *
import tkinter.font as font
import random
from cache import *
from os import getcwd
from copy import deepcopy


#voiture de 2 à 8 et camion de 9 à 13


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
    
    print(type([[0,2,3,3,4,4],[0,2,0,0,5,5],[1,1,0,0,11,6],[9,10,10,10,11,6],[9,0,0,0,11,7],[9,0,0,0,0,7]]))
    print(list(M))

matrice_niveau=niveau()
niveau=niveau()

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
n=len (matrice_niveau)
n2=len(matrice_niveau[0])

VOITUREB=0
RECT=0
RECT2=0

x=color().rstrip("\n")

posi=[]
liste_voiture=[]

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



#retirer les vieilles voitures -pas envie de faire un move
def effacer(N):
    for i in N:
        canv.delete(i)   
#placer les voitures/camions rectangulaires de la matrice
def affichage(M) :
    global n2,comp,RECT,RECT2,VOITUREB,x,liste_voiture
    L={}
    effacer(liste_voiture)
    for i in range(n):
        for j in range(n2):
            if M[i][j] !=0:
                if M[i][j]==1:
                    VOITUREB=canv.create_rectangle(j*AUTRE,i*AUTRE,j*AUTRE+AUTRE,i*AUTRE+AUTRE,fill="black")
                    liste_voiture.append(VOITUREB)
                else:
                    XY=position(M,M[i][j])
                    try:
                        L[M[i][j]]==1
                    except:
                        L[M[i][j]]=1
                        RECT=canv.create_rectangle(AUTRE*XY[0][0],AUTRE*XY[0][1],AUTRE*((XY[-1][0])+1),AUTRE*((XY[-1][1])+1),fill=x)
                        RECT2=canv.create_rectangle(AUTRE*XY[0][0],AUTRE*XY[0][1],AUTRE*((XY[-1][0])+1),AUTRE*((XY[-1][1])+1))
                        liste_voiture.append(RECT)
                        liste_voiture.append(RECT2)
   


def victory():
    global canv
    canv.create_rectangle(0,0,LARG,HAUT,fill='green3')
    canv.create_text(LARG//2,HAUT//2,text="VICTOIRE !",fill='white',font="Arial 50 roman")
    

def clic(event):
    global matrice_niveau,liste_voiture
    a=(event.x,event.y)
    matrice_niveau=deplacement(matrice_niveau,[int(a[1])//100,int(a[0])//100])
    affichage(matrice_niveau)
    enregistreur(matrice_niveau)
    a=victoire(matrice_niveau)
    if "vic"==a:
        #
        print("la fin")
    if a:
        victory()
        
#GESTION DES BOUTONS
def recommencer():
    global matrice_niveau
    affichage(niveau)
    matrice_niveau=deepcopy(niveau)

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

#LANCEMENT DES FONCTIONS
f=font.Font(size=15)

btn2=Button(fen,activebackground='IndianRed3', text="Quitter",height=3,width=15,command=quitter,font=f).pack(side=BOTTOM,padx=10, pady=10)

btn=Button(fen,activebackground='lightBlue1', text="Recommencer",height=3,width=15,command=recommencer,font=f).pack(side=BOTTOM,padx=10, pady=10)

btn3=Button(fen,activebackground='green', text="Solveur",height=3,width=15,command=solveur,font=f).pack(side=BOTTOM,padx=10, pady=10)

victoire(matrice_niveau)

affichage(matrice_niveau) 

canv.bind("<Button-1>", clic)


fen.mainloop()

fen.protocol("WM_DELETE_WINDOW",fen.destroy())



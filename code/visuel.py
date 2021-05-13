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
path2=path[:-4]+"/data"
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
n=len(matrice_niveau)
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
    global n2,comp,RECT,RECT2,VOITUREB,x,liste_voiture,matrice_niveau
    L={}
    effacer(liste_voiture)
    for i in range(n):
        for j in range(n2):
            if M[i][j]!=0:
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
   

class Pile:
    
	def __init__(self):
		self.valeurs = []

	def empiler(self, valeur):
		self.valeurs.append(valeur)

	def depiler(self):
		if self.valeurs:
			return self.valeurs.pop()

	def estVide(self):
		return self.valeurs == []

	def nombreDAssiettes(self):
		return len(self.valeurs)

	def lireSommet(self):
		return self.valeurs[-1]


def message_fin():
    global f,fen,logo
    POPUP = Toplevel()
    x=fen.winfo_x()
    y=fen.winfo_y()

    POPUP.geometry("+%d+%d" % (x,y))

    def termine():
        pass

    
    POPUP.title('Bien joué !')
    POPUP.minsize(height=100,width=300)
    Button(POPUP, text='Jouer à un niveau aléatoire',activebackground='Green',height=3,width=30,font=f,command=termine()).pack(anchor=NW,padx=10, pady=10)
    POPUP.transient(fen)
    POPUP.grab_set()

    canvas=Canvas(POPUP,width=100,height=56)
    canvas.pack()
    canvas.create_image(50,28,image=logo)


    fen.wait_window(POPUP)


def victory():
    global canv,matrice_niveau
    canv.delete("all")
    canv.create_rectangle(0,0,LARG,HAUT,fill='green3')
    canv.create_text(LARG//2,HAUT//2,text="VICTOIRE !",fill='white',font="Arial 50 roman")
    message_fin()
    

def clic(event):
    global matrice_niveau,liste_voiture,p
    a=(event.x,event.y)
    matrice_niveau=deplacement(matrice_niveau,[int(a[1])//100,int(a[0])//100])
    affichage(matrice_niveau)
    enregistreur(matrice_niveau)
    p.empiler(matrice_niveau)
    a=victoire(matrice_niveau)
    if "vic"==a:
        #mettre un POPUP avec les expliquations et faire apparaitre un bouton "aléatoire"
        print("la fin")
    if a:
        victory()
        
#GESTION DES BOUTONS
def recommencer():
    global matrice_niveau,x,niveau
    x=color().rstrip("\n")
    affichage(niveau)
    matrice_niveau=deepcopy(niveau)
    
def quitter():
    fen.destroy()

def annuler():
    global p,p2
    if not(p.estVide()):
        p.lireSommet()
        affichage(p.lireSommet())
        p2.empiler(p.lireSommet())
        p.depiler()
'''     
def annuler():
    if not(p.is_empty()):
        affichage(p.peek())
        p2.push(p.peek())
        p.pop()
'''
def retablir():
    global p,p2
    if not(p2.estVide()):
        affichage(p2.lireSommet())
        enregistreur(p2.lireSommet())
        p.empiler(p2.lireSommet())
        p2.depiler()

def numero():
    path2=os.getcwd()
    path2=path2[:-4]
    path2+="data/data.txt"
    with open(path2,'r') as data:
        num=int(data.readline(2),base=10)
        return num
    
def diff():
    global coul
    if numero()==1:
        coul="turquoise1"
        return "tuto"
    elif numero()>1 and numero()<6:
        coul="SeaGreen1"
        return "très facile"
    elif numero()<12:
        coul="green"
        return "facile"
    elif numero()<18:
        coul="orange"
        return "moyen"
    elif numero()<21:
        coul="red"
        return "difficile"

def grille():
    global comp
    root = Tk()
    frame = Frame(root)
    frame.grid()
    root.title("Choisis ton niveau")  
    root.minsize(LARG//2,HAUT//2)    


    grid = Frame(frame)  
    grid.grid(sticky=N+S+E+W, column=0, row=7, columnspan=2)

    comp=1
    for x in range(5):
        for y in range(4):
            btn = Button(grid,text=str(comp),height=5,width=10,command=choix_niveau(comp))
            comp+=1
            btn.grid(column=x, row=y)

    root.mainloop()

def tutoriel():
    POPUP = Toplevel()
    f=font.Font(size=15)
    x=fen.winfo_x()+100
    y=fen.winfo_y()+200

    POPUP.geometry("+%d+%d" % (x,y))
    POPUP.title('TUTORIEL')
    POPUP.minsize(height=100,width=300)
    texte=Label(POPUP, text = "BUT DU JEU : faire sortir, par la porte de droite, la voiture noire du parking.\nCOMMENT JOUER : cliquer sur l'avant de la voiture pour la faire avancer et sur l'arrière pour la faire reculer.\nFranchissez les 20 niveaux pour gagner ! Bonne chance !")
    texte.config(font =("Courier", 14))
    texte.pack()
    Button(POPUP, text="J'ai compris",background="white",activebackground='Green',height=3,width=30,font=f,command=POPUP.destroy).pack(padx=10, pady=10)
    POPUP.transient(fen)
    POPUP.grab_set()

    canvas=Canvas(POPUP,width=100,height=56)
    canvas.pack()

    fen.wait_window(POPUP)

'''
def nouv_niveau():
    POPUP.destroy
    path2=os.getcwd()
    path2=path2[:-4]
    path2+="data/data.txt"
    with open(path2,'r') as data:
        num=int(data.readline(2),base=10)
        return num+1
'''

def choix_niveau(comp):
    pass
'''
    path2=os.getcwd()
    path2=path2[:-4]
    path2+="data/data.txt"
    with open(path2,'r') as data:
        num=int(data.readline(2),base=10)
        num=comp
    root.destroy()
'''



#-------------LANCEMENT DES FONCTIONS-------------
f=font.Font(size=15)

p=Pile()
p2=Pile()
#INTEGRER LES IMAGES AUX BOUTONS ANNULER/RETABLIR
retour=PhotoImage(file=path+"images/retour.png")
retourImage=retour.subsample(1,1)
Button(fen,height=50,width=80,image=retourImage,command=annuler).pack(side=BOTTOM,padx=10,pady=10)

retour2=PhotoImage(file=path+"images/avancer.png")
retour2Image=retour2.subsample(1,1)
Button(fen,height=50,width=80,image=retour2Image,command=retablir).pack(side=BOTTOM,padx=10,pady=10)

#BOUTONS QUITTER/RECOMMENCER/NIVEAUX
Button(fen,activebackground='IndianRed3', text="Quitter",height=3,width=15,command=quitter,font=f).pack(side=BOTTOM,padx=10, pady=10)

Button(fen,activebackground='lightBlue1', text="Recommencer",height=3,width=15,command=recommencer,font=f).pack(side=BOTTOM,padx=10, pady=10)

Button(fen,activebackground='green', text="Niveaux",height=3,width=15,command=grille,font=f).pack(side=BOTTOM,padx=10, pady=10)

#TEXTE NIVEAU
texte=Label(fen, text = "Niveau : "+str(numero()))
texte2=Label(fen, text = "Difficulté : "+diff())
texte.config(font =("Courier", 14))
texte2.config(background=coul,font =("Courier", 14))
texte.pack()
texte2.pack()

tutoriel()

victoire(matrice_niveau)

affichage(matrice_niveau) 

canv.bind("<Button-1>", clic)


fen.mainloop()

fen.protocol("WM_DELETE_WINDOW",fen.destroy())



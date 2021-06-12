from tkinter import *
import tkinter as tk
from time import time,sleep

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
    


class Partie(tk.Tk):
    def __init__(self):
        #PARAMETRES_FENETRE_TAILLE
        tk.Tk.__init__(self)
        self.LARG=400
        self.HAUT=400

        self.M=[3,3,0,2,4,3,3,
        2,3,2,4,1,4,1,
        2,1,0,4,2,4,5,
        4,1,2,0,5,0,5,
        2,3,4,0,2,3,2,
        4,5,1,4,3,3,4,
        2,0,4,0,0,5,3]

        #PARAMETRES_FENETRE
        '''
        self.fen=Tk()
        self.fen.attributes('-fullscreen',True)
        self.fen.bind('<Escape>',lambda e: self.fen.destroy()) #Appuyer sur echap pour sortir
        self.fen.title("Flood it")
        '''
        self.pile=Pile()

        self.canv=tk.Canvas(self, width=self.LARG, height=self.HAUT)
        self.canv.pack(side=LEFT)

        self.color=["green","pink","red","orange","yellow","blue","purple"]

        self.btn1=tk.Button(self,activebackground='IndianRed3', text="Quitter",height=3,width=15,command=self.quitter).pack(side=BOTTOM,padx=10, pady=10)
        self.btn2=tk.Button(self,activebackground='lightBlue1', text="Recommencer",height=3,width=15,command=self.recommencer).pack(side=BOTTOM,padx=10, pady=10)
        
        self.couleur(self.M,7)

    def quitter(self):
        self.destroy()
    
    def recommencer(self):
        while len(self.pile)>1 :
            self.pile.depiler()
        #dessiner la matrice qu'il reste dans la liste

    def couleur(self,liste,taille):
        ok=0
        for i in range (taille):
            for j in range (taille):
                self.canv.create_rectangle((40*j,40*i),(40*j+40,40*i+40),fill=self.color[liste[ok]])
                ok=ok+1


    def coord(event,self):
        self.xc=event.x
        self.yc=event.y
        return self.xc,self.yc


    def init(self,M):
        #global RECT
        for i in range (len(M)):
            for j in range (len(M[0])):
                self.canv.create_rectangle((40*j,40*i),(40*j+40,40*i+40),fill=self.color[M[i][j]])

if __name__=="__main__":
    jeu=Partie()
    jeu.title("Flood it")
    jeu.mainloop()


#clic détecte couleur grace à la case
from tkinter import *
import tkinter as tk
from time import time,sleep

class Partie():
    def __init__(self,LARG=800,HAUT=800):
        #PARAMETRES_FENETRE_TAILLE

        self.LARG=LARG
        self.HAUT=HAUT

        self.M=[3,3,0,2,4,3,3,
        2,3,2,4,1,4,1,
        2,1,0,4,2,4,5,
        4,1,2,0,5,0,5,
        2,3,4,0,2,3,2,
        4,5,1,4,3,3,4,
        2,0,4,0,0,5,3]

        #PARAMETRES_FENETRE

        self.fen=Tk()
        self.fen.attributes('-fullscreen',True)
        self.fen.bind('<Escape>',lambda e: self.fen.destroy()) #Appuyer sur echap pour sortir
        self.fen.title("Flood it")
        self.canv=Canvas(self.fen, width=self.LARG, height=self.HAUT)
        self.canv.pack(side=LEFT)

        self.color=["green","pink","red","orange","yellow","blue","purple"]


    def quitter(self):
        self.fen.destroy()
    
    def recommencer(self):
        pass

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
    fen=Tk()
    jeu=Partie(fen)
    jeu.title("Flood it")
    jeu.fen.mainloop()


#clic détecte couleur grace à la case
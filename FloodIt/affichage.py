from tkinter import *
import tkinter as tk
from time import time,sleep

class Partie():
    def __init__(self):
        tk.Tk.__init__(self)
        self.btn1=tk.Button(self, text="Quitter",height=3,width=15,command=lambda: self.quitter()).place(padx=10,pady=10)
        self.btn2=tk.Button(self,text="Recommencer",height=3,width=15,command=lambda: self.recommencer()).place(padx=10,pady=10)

        #PARAMETRES_FENETRE_TAILLE

        difficulté="facile"
        def diffi():
            global TAILLE
            if difficulté=="facile":
                TAILLE=10
            elif difficulté=="moyen":
                TAILLE=12
            elif difficulté=="difficile":
                TAILLE=14

        self.diffi()
        self.LARG=TAILLE*40
        self.HAUT=TAILLE*40

        M=[
        [3,3,0,2,4,3,3],
        [2,3,2,4,1,4,1],
        [2,1,0,4,2,4,5],
        [4,1,2,0,5,0,5],
        [2,3,4,0,2,3,2],
        [4,5,1,4,3,3,4],
        [2,0,4,0,0,5,3]]

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




    def init(self,M):
        #global RECT
        for i in range (len(M)):
            for j in range (len(M[0])):
                self.canv.create_rectangle((40*j,40*i),(40*j+40,40*i+40),fill=self.color[M[i][j]])

if __name__=="__main__":
    jeu=Partie()
    jeu.title("Flood it")
    jeu.mainloop()

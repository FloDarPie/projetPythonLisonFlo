from tkinter import *
import tkinter as tk
from time import time,sleep



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

diffi()
LARG=TAILLE*40
HAUT=TAILLE*40

M=[
[3,3,0,2,4,3,3],
[2,3,2,4,1,4,1],
[2,1,0,4,2,4,5],
[4,1,2,0,5,0,5],
[2,3,4,0,2,3,2],
[4,5,1,4,3,3,4],
[2,0,4,0,0,5,3]]

#PARAMETRES_FENETRE

def fenetre():
    global fen,canv
    fen=Tk()
    fen.attributes('-fullscreen',True)
    boutons()
    fen.bind('<Escape>',lambda e: fen.destroy()) #Appuyer sur echap pour sortir
    fen.title("Flood it")
    canv=Canvas(fen, width=LARG, height=HAUT)
    canv.pack(side=LEFT)

color=["green","pink","red","orange","yellow","blue","purple"]


def quitter():
    fen.destroy()

def recommencer():
    print("recommencer")
    pass




def init(M):
    for i in range (len(M)):
        for j in range (len(M[0])):
            canv.create_rectangle((40*j,40*i),(40*j+40,40*i+40),fill=color[M[i][j]])


def boutons():
    Button(fen, text="Quitter",height=3,width=15,command=quitter).pack(padx=10,pady=10)
    Button(fen,text="Recommencer",height=3,width=15,command=recommencer).pack(padx=10,pady=10)


if __name__=="__main__":
    fenetre()
    init(M)
    fen.mainloop()

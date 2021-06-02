from tkinter import *
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
fen=Tk()
fen.title("Flood it")
canv=Canvas(fen, width=LARG, height=HAUT)
canv.pack(side=LEFT)

color=["green","pink","red","orange","yellow","blue","purple"]

def init(M):
    #global RECT
    for i in range (len(M)):
        for j in range (len(M[0])):
            RECT=canv.create_rectangle((40*j,40*i),(40*j+40,40*i+40),fill=color[M[i][j]])

init(M)

fen.mainloop()

from tkinter import *

LARG=600
HAUT=600
hauteurLigne=HAUT//3

COTE=LARG/6

fen=Tk()
canv=Canvas(fen, width=LARG, height=HAUT, background='red')
canv.pack()

def grille():
    for i in range (1,LARG//100):
        canv.create_line((i*100,0),(i*100,LARG), fill='white',width=5)
        canv.create_line((0,i*100),(LARG,i*100), fill='white',width=5)

grille()

def clic(event):
    X,Y=(event.x,event.y)
    col=X//COTE
    lig=Y//COTE
    print(lig,col)


canv.bind("<Button-1>", clic)

fen.mainloop()

fen.protocol("WM_DELETE_WINDOW", fen.destroy())
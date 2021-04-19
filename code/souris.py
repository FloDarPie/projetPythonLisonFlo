from tkinter import *
import os

LARG=600
HAUT=600

fen=Tk()
canv=Canvas(fen, width=LARG, height=HAUT, background='red')
canv.pack()

path=os.getcwd()
path=path[:-4]
path+="/assets/"
voiture=PhotoImage(file=path+"image_gif/5.gif")

id_image=0
def clic(event):
    global id_image #pour pouvoir modifier id_image
    canv.delete(id_image)
    centre=(event.x, event.y)
    id_image=canv.create_image(centre, image=voiture)


canv.bind("<Button-1>", clic)

fen.mainloop()

fen.protocol("WM_DELETE_WINDOW", fen.destroy())
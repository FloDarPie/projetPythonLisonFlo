from tkinter import *
import os


path=os.getcwd()
print(path)
path=path[:-4]
path+="/assets/"

print(path)
LARG=600
HAUT=600
DIM=LARG

fen=Tk()
canv=Canvas(fen, width=LARG, height=HAUT, background="gray")
canv.pack(padx=10, pady=10)

canv.create_line((LARG,2*(LARG/6)),(LARG,3*(LARG/6)), fill="red", width=9)

#convertir image
parking=PhotoImage(file=path+"images/parking_fond.png")

#affiche une image par rapport à son centre
centre=(DIM/2,DIM/2)
canv.create_image(centre, image=parking)

fen.mainloop()

fen.protocol("WM_DELETE_WINDOW",fen.destroy())
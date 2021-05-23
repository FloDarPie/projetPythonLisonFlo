from tkinter import *

#test git


PICT_SIZE=50
PAD=2
SIDE=PICT_SIZE+PAD

#format du quadrillages à en fonction des images
#format aire de jeu pour les premiers niveaux-> 500/500

NB_LINES=5
NB_COLS=5

WIDTH=SIDE*NB_COLS
HEIGHT=SIDE*NB_LINES
X0=Y0=SIDE//2

root=Tk()
cnv=Canvas(root, width=WIDTH, height=HEIGHT, bg='gray')
cnv.pack()

cover = PhotoImage(file="./Bleue.png")

# Placement des images
for line in range(NB_LINES):
    for col in range(NB_COLS):
        centre=(X0+col*SIDE, Y0+line*SIDE)
        cnv.create_image(centre, image=cover)


def quitter():
    root.destroy()

root.protocol("WM_DELETE_WINDOW", quitter)

root.mainloop()


fen.protocol("WM_DELETE_WINDOW", fen.destroy())


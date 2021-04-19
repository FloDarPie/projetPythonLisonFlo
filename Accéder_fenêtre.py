#générer la fenêtre du jeu
from tkinter import *

fenetre = Tk()

fenetre.title("Parking")
fenetre.config(bg = 'gray')

longueur=600
hauteur=600
hauteurLigne=hauteur//3

canv=Canvas(fenetre, bg="gray", height=hauteur, width=longueur)

color="white"
taille=600

#création lignes blanches
canv.create_line((taille,0),(taille,hauteurLigne), fill=color,width=taille)
#canv.create_line((i*100,hauteur-hauteurLigne),(i*100,longueur), fill=color,width=taille)


'''
#création lignes blanches
for i in range (1,longueur//100):
	canv.create_line((i*100,0),(i*100,hauteurLigne), fill=color,width=taille)
	canv.create_line((i*100,hauteur-hauteurLigne),(i*100,longueur), fill=color,width=taille)
'''

#création de la sortie de voiture
canv.create_line((5,200),(5,300), fill="red", width=7)

canv2=Canvas(fenetre,height=hauteur, width=longueur)

fenetre.mainloop()
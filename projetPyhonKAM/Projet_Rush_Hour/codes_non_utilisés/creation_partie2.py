from module_partie import Partie 
from module_vehicule import Vehicule
from module_fenetre_partie import FenetrePartie
from tkinter import*
from gestion_son import Musique
from random import randint
from copy import deepcopy
from time import time

#date 14/05 a 00h42

class Fenetre(FenetrePartie):
    
    def __init__(self,vehicules,master):
        
        super().__init__(vehicules,master)
        
        def on_closing():
            print("fin !")
            f=open("Niveau "+str(randint(1,100))+".txt","w")
            for x in self.matrice:
                f.write(" ".join([str(y) for y in x]))
                f.write("\n")
            f.close()
            self.root.destroy()
        
        self.root.protocol("WM_DELETE_WINDOW", on_closing)       

    '''Surcharge pour empecher le declenchement d'une victoire'''
    def estGagnee(self):
        return False


M=[ [0,4,7,7,7,0],
    [0,4,0,6,6,0],
    [5,4,0,0,9,0],
    [5,1,1,0,9,2],
    [10,10,3,0,9,2],
    [0,0,3,8,8,0],
    ]

test=Tk()
Musique()
Musique.pause()

laPremierePartie=Fenetre(M,test)
laPremierePartie.afficher()
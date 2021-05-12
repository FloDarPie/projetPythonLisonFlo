import tkinter as tk
import tkinter.font as font
import random
from cache import *
from os import getcwd
from copy import deepcopy


class Partie(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.size = 600
        

        
        #chemin pour les infos
        path=os.getcwd()
        path=path[:-4]
        self.pathCouleur = path+"data/couleurs.txt"
        self.pathAsset = path+"assets/"
        self.parking=tk.PhotoImage(file=self.pathAsset+"images/parking_fond.png")
        self.logo=tk.PhotoImage(file=self.pathAsset+"images/logo_rushHour2.png")
        self.logoAngle=tk.PhotoImage(file=self.pathAsset+"images/logo_rushHour_corner.png")
        self.bordureBas=tk.PhotoImage(file=self.pathAsset+"images/bas.png")
        self.bordureDroite=tk.PhotoImage(file=self.pathAsset+"images/droite.png")
        self.sortie=tk.PhotoImage(file=self.pathAsset+"images/sortie.png")

        self.color=color().rstrip("\n")
        self.fenetre()

    def fenetre(self):
        #création de l'espace de jeu et positionnement des boutons
        self.canv = tk.Canvas(self,bg="black",height=self.size+100,width=self.size+300)
        
        
        
        
        self.canv.create_image((self.size/2,self.size/2),image=self.parking)
        self.canv.create_image((self.size/2,600),image=self.bordureBas)#en bas
        self.canv.create_image((600,self.size/2),image=self.bordureDroite)#droite
        self.canv.create_image((755,87.5),image=self.logoAngle)
        self.canv.create_image((607,250), image=self.sortie)#sortie
        self.canv.grid(column=0, row=0, ipadx=5, pady=5, sticky=tk.E+tk.N)

        #taille police
        f=font.Font(size=15)
        
        #les boutons
        self.bouton_quitter = tk.Button(self, text="Quitter", activebackground='IndianRed3', height=3, width=15, command=self.quitter, font=f).place(x = 660, y = 200)
        self.bouton_niveau = tk.Button(self, text="Choix du niveau", activebackground='green', height=3, width=15, command=self.niveau, font=f).place(x=660, y = 350)
        self.bouton_recommencer = tk.Button(self, text="Recommencer", activebackground='lightBlue1', height=3, width=15, command=self.recommencer, font=f).place(x=660, y = 500)

    
    #s'enfuir de l'appli
    def quitter(self):
        self.quit()

    def recommencer(self,level):
        pass
    
    #reglage des niveaux
    def niveau(self):

        popup = tk.Toplevel()
        popup.resizable(False,False)
        f=font.Font(size=15)
        centre = 300
        popup.geometry("+%d+%d" % (centre,centre))
        popup.title('Sélection du niveau')
        
        popup.bouton_quitter = tk.Button(popup, text="Retour",activebackground='IndianRed3',height=3,width=15,command=popup.destroy,font=f).pack(side=tk.BOTTOM,padx=10, pady=10)
        
        #fonction de freeze qui marche pas
        #self.wait_window(popup)
 

        






if __name__ == "__main__":
    app = Partie()

    app.title("Rush Hour")
    app.resizable(False,False)
    app.mainloop()
    

    

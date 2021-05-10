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
        
        self.color=color().rstrip("\n")
        self.fenetre()

    def fenetre(self):
        #création de l'espace de jeu et positionnement des boutons
        self.canv = tk.Canvas(self,bg="black",height=self.size,width=self.size)
        
        
        
        
        self.canv.create_image((self.size/2,self.size/2),image=self.parking)
        #taille police
        f=font.Font(size=15)
        
        
        
        
        
        self.bouton_quitter = tk.Button(self, text="Quitter",activebackground='IndianRed3',height=3,width=15,command=self.quitter,font=f).pack(side=tk.BOTTOM,padx=10, pady=10)
        self.bouton_niveau = tk.Button(self, text="Choix du niveau",activebackground='green',height=3,width=15,command=self.niveau,font=f).pack(side=tk.RIGHT,padx=10, pady=10)
        self.canv.pack()
    
    #s'enfuir de l'appliQuitter
    def quitter(self):
        self.quit()

    def niveau(self):
        self.new_fenetre = tk.Toplevel()
        
        centre = 300
        new_fenetre.tk.geometry("+%d+%d" % (centre+100,centre+200))
        new_fenetre.title('Sélection du niveau')
        
        self.bouton_quitter = tk.Button(self, text="Retour",activebackground='IndianRed3',height=3,width=15,command=self.quitter,font=f).pack(side=tk.BOTTOM,padx=10, pady=10)
        self.wait_window(new_fenetre)
        '''
        POPUP = tk.Toplevel()
        x=tk.winfo_x()
        y=tk.winfo_y()

        POPUP.geometry("+%d+%d" % (x+100,y+200))

        
        POPUP.title('Choisis un niveau ')
        POPUP.minsize(height=100,width=300)
        tk.Button(POPUP, text='En cours de production...',activebackground='SteelBlue4',height=3,width=30,font=f,command=POPUP.destroy).pack(anchor=NW,padx=10, pady=10)
        POPUP.transient(self.size)
        POPUP.grab_set()

        canvas=tk.Canvas(POPUP,width=100,height=56)
        canvas.pack()
        canvas.create_image(50,28,image=self.logo)
        '''

        






if __name__ == "__main__":
    app = Partie()

    app.title("Rush Hour")
    app.resizable(False,False)
    app.mainloop()
    

    

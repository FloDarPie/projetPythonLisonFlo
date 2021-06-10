import tkinter as tk
import tkinter.font as font

from moteur import Moteur

class Affichage:
    def __init__(self,root=None):

        self.moteur = Moteur()
        
        self.root = root
        
        self.couleur = ["green","pink","red","orange","yellow","blue","purple"]
        
        self.root.attributes('-fullscreen',True)
        self.root.bind("<Escape>",self.quitterEchap)
        self.root.title("Flood It")
        #self.root.background("black")
        
        #prendre les infos de la fenêtre
        self.ecranLargeur = root.winfo_screenwidth()
        self.ecranHauteur = root.winfo_screenheight()
        print(self.ecranHauteur)
        
        self.canvas=tk.Canvas(root,width=self.ecranLargeur,height=self.ecranHauteur,borderwidth=0,bg="Black")
        
        self.canvas.grid(column=0, row=0, ipadx=0, ipady=0, sticky=tk.E+tk.N)
        
        self.titre = tk.PhotoImage(file="titre.png")
        self.canvas.create_image((self.ecranLargeur//2,120),image=self.titre) #fixer le titre au milieu de l'écran
        
        #affichage respectif
        self.afficheAutre()
        self.afficheJeu(self.moteur.matrice)
        
        
    def afficheJeu(self,matrice):
        '''
        ecranHauteur|ecranLargeur       ecranHauteur|ecranLargeur+800
        
        
                                (zone de jeu)
        
        
        ecranHauteur+800|ecranLargeur   ecranHauteur+800|ecranLargeur+800
        '''
        #zone de jeu 800*800
        angleDroitY = 237
        cote = int(800 / self.moteur.taille) # format de la fenêtre de jeu
        
        i = 0 #indice de la cellule de la matrice

        for ligne in range(self.moteur.taille):
            angleDroitX = self.ecranLargeur//2-400
            for cell in range(self.moteur.taille):
                self.canvas.create_rectangle((angleDroitX,angleDroitY), (angleDroitX+cote,angleDroitY+cote), fill = self.couleur[self.moteur.matrice[i]], width=0)
                angleDroitX+=cote
                i+=1
            angleDroitY+=cote
        
        
    def afficheAutre(self):
        #BOUTON QUITTER
        self.boutton_quitter=None
        self.root.protocol("WM_DELETE_WINDOW",self.quitter)

        self.boutton_quitter=tk.Button(self.canvas,borderwidth=0,bg="Red",activebackground="Blue",command=self.quitter,cursor="X_cursor").place(x=10,y=10)
    
    
    
    def quitterEchap(self,event):
        self.quitter()
    def quitter(self):
        self.root.destroy()

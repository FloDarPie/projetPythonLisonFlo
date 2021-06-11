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
        
        self.canvas=tk.Canvas(root,width=self.ecranLargeur,height=self.ecranHauteur,borderwidth=0,bg="Black")
        
        self.canvas.grid(column=0, row=0, ipadx=0, ipady=0, sticky=tk.E+tk.N)
        
        self.titre = tk.PhotoImage(file="titre.png")
        self.canvas.create_image((self.ecranLargeur//2,80),image=self.titre) #fixer le titre au milieu de l'écran
        
        #affichage respectif
        self.afficheAutre()
        self.afficheJeu(self.moteur.matrice)
        self.canvas.bind("<Button-1>",self.clic)
        
        
    def afficheJeu(self,matrice):
        '''
        depart | 157                        depart+X | 157
        
        
                                (zone de jeu)
        
        
        depart | 157 + X                    depart+X | 157+X
        
        
        depart = self.ecranLargeur//2-self.ecranHauteur*3/8
        
        X = self.ecranHauteur * 3/4
        '''
        #zone de jeu
        angleDroitY = 157
        self.cote = int(self.ecranHauteur * 3/4 / self.moteur.taille) # format de la fenêtre de jeu
        
        i = 0 #indice de la cellule de la matrice

        for ligne in range(self.moteur.taille):
            angleDroitX = self.ecranLargeur//2-self.ecranHauteur*3/8
            for cell in range(self.moteur.taille):
                self.canvas.create_rectangle((angleDroitX,angleDroitY), (angleDroitX+self.cote,angleDroitY+self.cote), fill = self.couleur[self.moteur.matrice[i]], width=0)
                angleDroitX+=self.cote
                i+=1
            angleDroitY+=self.cote
        
        
    def afficheAutre(self):
        '''
        #BOUTON QUITTER
        self.boutton_quitter=None
        self.root.protocol("WM_DELETE_WINDOW",self.quitter)

        self.boutton_quitter=tk.Button(self.canvas,borderwidth=0,bg="Red",activebackground="Blue",command=self.quitter,cursor="X_cursor").place(x=10,y=10)
        '''
        self.canvas.create_text(100,self.ecranHauteur//2+200, text="Press 'Echap' to quit", fill='white', font="Arial 14 roman")
        
        self.canvas.create_text(140,self.ecranHauteur//2+250, text="Click on case to select a color. \nYou begin on top left.", fill='white', font="Arial 14 roman")
        
    
    def clic(self,event):
        a = (event.x,event.y)
        
        X = int((a[0]-self.ecranLargeur//2-self.ecranHauteur*3/8) // self.cote)+self.moteur.taille
        Y = int((a[1]-157) // self.cote)
        
        if 0 <= X <= self.moteur.taille-1 and 0 <= Y <= self.moteur.taille-1:
            cell = X+Y*self.moteur.taille
            self.moteur.transform(self.moteur.matrice[cell])
            self.afficheJeu(self.moteur.matrice)
    
    def quitterEchap(self,event):
        self.quitter()
    def quitter(self):
        self.root.destroy()

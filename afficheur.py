import tkinter as tk
import tkinter.font as font

from moteur import Moteur

class Affichage:
    def __init__(self,root=None):

        self.moteur = Moteur()
        
        self.root = root
        
        self.couleur = ["green","pink","red","orange","yellow","blue","purple"]
        
        self.cpt_coup = 0
        
        self.memoire = self.moteur.matrice[:]
        
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
        
        #BOUTON Recommencer
        self.boutton_recommencer=None

        self.boutton_recommencer = tk.Button(self.canvas, borderwidth=0, bg="Black", activebackground="Black",text="Recommencer",font="Arial 25 roman", command=lambda:[self.afficheJeu(self.memoire),self.change()] ).place(x=10,y=10)
        
        self.info1 = self.canvas.create_text(100,self.ecranHauteur//2+200, text="Press 'Echap' to quit", fill='white', font="Arial 14 roman")
        
        self.info2 = self.canvas.create_text(140,self.ecranHauteur//2+250, text="Click on case to select a color. \nYou begin on top left.", fill='white', font="Arial 14 roman")
        
        self.affiche_coup = self.canvas.create_text(int(self.ecranLargeur*8/11)+20, int(self.ecranHauteur *10/11), text=str(self.cpt_coup), fill="white", font="Arial 42 roman")
        self.affiche_max_coup = self.canvas.create_text(int(self.ecranLargeur*8/11)+90, int(self.ecranHauteur *10/11), text="/22", fill="white", font="Arial 42 roman")
        
        self.victoire = None
        
        
    def change(self):
        self.moteur.initialisation()
        self.moteur.matrice=self.memoire[:]
        self.cpt_coup = 0
        
        
    def clic(self,event):
        a = (event.x,event.y)
        
        if self.victoire==None:
            
            self.canvas.delete(self.info1)
            self.canvas.delete(self.info2)
            
            X = int((a[0]-self.ecranLargeur//2-self.ecranHauteur*3/8) // self.cote)+self.moteur.taille
            Y = int((a[1]-157) // self.cote)
            
            if 0 <= X <= self.moteur.taille-1 and 0 <= Y <= self.moteur.taille-1:
                cell = X+Y*self.moteur.taille
                if self.moteur.matrice[cell]!=self.moteur.matrice[0]:
                    self.moteur.transform(self.moteur.matrice[cell])
                    self.afficheJeu(self.moteur.matrice)
                    
                    self.canvas.delete(self.affiche_coup)
                    self.cpt_coup+=1
                    self.affiche_coup = self.canvas.create_text(int(self.ecranLargeur*8/11)+20, int(self.ecranHauteur *10/11), text=str(self.cpt_coup), fill="white", font="Arial 42 roman")
            
            
            if self.controle_victoire():
                self.victoire = self.canvas.create_text(self.ecranLargeur//2,self.ecranHauteur//2, text= "Victoire !", fill="white", font="Arial 80 bold roman")
                
            elif self.cpt_coup>22:
                self.defaite = self.canvas.create_text(175 ,self.ecranHauteur//2, text="C'est raté !", fill= "white", font="Arial 50 bold roman")
            
        else:
            self.moteur.matrice = self.moteur.initialisation()
            self.afficheJeu(self.moteur.matrice)
            self.victoire = None
            self.cpt_coup=-1
    
    def controle_victoire(self):
        if self.cpt_coup>self.moteur.taille:
            verif = self.moteur.matrice[0]
            for j in self.moteur.matrice:
                if verif!=j:
                    return False
            return True
    
    
    def quitterEchap(self,event):
        self.quitter()
    def quitter(self):
        self.root.destroy()

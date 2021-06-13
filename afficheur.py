import tkinter as tk
import tkinter.font as font

from moteur import Moteur

class Affichage:
    def __init__(self,root=None):

        self.moteur = Moteur()
        
        self.root = root
        
        self.couleur = ["green","pink","red","orange","yellow","blue","purple"]
        
        self.cpt_coup = 0
        
        #prendre les infos de la fenêtre
        self.ecranLargeur = 1000
        self.ecranHauteur = 700
        
        #thème d'apparence
        self.cl_blanc= "#d9d2b8"
        self.cl_noir = "#1c1b17"
        
        #point d'angle droit haut de l'espace de jeu
        self.departY = self.ecranHauteur//5
        self.departX = int(self.ecranLargeur//2-self.ecranHauteur*3/8)
        
        self.memoire = self.moteur.matrice[:]
        
        self.root.bind("<Escape>",self.quitterEchap)
        self.root.title("Flood It - The Game")
        
        self.canvas=tk.Canvas(root,width=self.ecranLargeur,height=self.ecranHauteur,borderwidth=0, bg=self.cl_noir)
        
        self.canvas.grid(column=0, row=0, ipadx=0, ipady=0, sticky=tk.E+tk.N)
        
        self.titre = tk.PhotoImage(file="titre.png")
        self.canvas.create_image((self.ecranLargeur//2,80),image=self.titre) #fixer le titre au milieu de l'écran
        
        #affichage respectif
        self.afficheAutre()
        self.afficheJeu(self.moteur.matrice)
        self.canvas.bind("<Button-1>",self.clic)
        
        
    def afficheJeu(self,matrice):
        '''
        depart | ecranHauteur//5                        depart+X | ecranHauteur//5
        
        
                                (zone de jeu)
        
        
        depart | ecranHauteur//5 + X                    depart+X | ecranHauteur//5+X
        
        
        depart = self.ecranLargeur//2-self.ecranHauteur*3/8
        
        X = self.ecranHauteur * 3/4
        '''
        #zone de jeu
        angleDroitY = self.departY
        self.cote = int(self.ecranHauteur * 3/4 / self.moteur.taille) # format de la fenêtre de jeu
        
        i = 0 #indice de la cellule de la matrice
        
        for ligne in range(self.moteur.taille):
            angleDroitX = self.departX
            for cell in range(self.moteur.taille):
                self.canvas.create_rectangle((angleDroitX,angleDroitY), (angleDroitX+self.cote,angleDroitY+self.cote), fill = self.couleur[self.moteur.matrice[i]], width=0)
                angleDroitX+=self.cote
                i+=1
            angleDroitY+=self.cote
        
        
    def afficheAutre(self):
        
        #BOUTON Recommencer
        self.boutton_recommencer=None
        self.affiche_cpt = None
        self.boutton_recommencer = tk.Button(self.canvas, borderwidth=0, text="Recommencer",font="Arial 25 roman", command=lambda:[self.afficheJeu(self.memoire),self.change()] ).place(x=10,y=10)
        
        self.info2 = self.canvas.create_text(130,self.ecranHauteur//2+250, text="Click on case to select a color.\nYou begin on top left.", fill=self.cl_blanc, font="Arial 14 roman")
        
        
        
        self.affiche_coup()
        self.victoire = None
        
    def affiche_coup(self):
        self.canvas.delete(self.affiche_cpt)
        self.affiche_cpt = self.canvas.create_text(self.ecranLargeur-120, self.ecranHauteur-40 , text=str(self.cpt_coup), fill=self.cl_blanc, font="Arial 42 roman")
        self.affiche_max_coup = self.canvas.create_text(self.ecranLargeur-50, self.ecranHauteur -40,text="/22", fill=self.cl_blanc, font="Arial 42 roman")
        
        
        
        
    def change(self):
        self.moteur.initialisation()
        self.moteur.matrice=self.memoire[:]
        self.cpt_coup = 0
        
        
    def clic(self,event):
        
        self.canvas.delete(self.info2)
        
        if self.victoire==None: #pas encore la victoire
            
            x = (event.x - self.departX) // self.cote 
            y = (event.y - self.departY) // self.cote
            
            self.valide_coup(x,y)
            
            '''
            t = self.moteur.taille-1
            if 0 <= x <= t and 0 <= y <= t :
                cell = X+Y*self.moteur.taille
                if self.moteur.matrice[cell]!=self.moteur.matrice[0]:
                    self.moteur.transform(self.moteur.matrice[cell])
                    self.afficheJeu(self.moteur.matrice)
                    
                    self.canvas.delete(self.affiche_coup)
                    self.cpt_coup+=1
                    self.affiche_coup()
            '''
        else:
            self.relance()
    
    
    #controle si les cases cliqué sont ok et si il faut effectuer un changement
    def valide_coup(self,x,y):
        pass
    
    
    #balance une nouvelle partie
    def relance(self):
            self.moteur.matrice = self.moteur.initialisation()
            self.afficheJeu(self.moteur.matrice)
            self.victoire = None
            self.cpt_coup=-1
            
    
            
    def victory(self):
        if cpt_coup>19:
            if self.controle_victoire():
                self.victoire = self.canvas.create_text(self.ecranLargeur//2,self.ecranHauteur//2, text= "Victoire !", fill=self.cl_blanc, font="Arial 80 bold roman")
                
            elif self.cpt_coup>22:
                self.defaite = self.canvas.create_text(175 ,self.ecranHauteur//2, text="C'est raté !", fill= self.cl_blanc, font="Arial 50 bold roman")
            

    
    def controle_victoire(self):
        verif = self.moteur.matrice[0]
        for j in self.moteur.matrice:
            if verif != j:
                return False
        return True
    
    
    def quitterEchap(self,event):
        self.quitter()
    def quitter(self):
        self.root.destroy()

import tkinter as tk
import tkinter.font as font

from moteur import Moteur

#Dans ce jeu, il est possible de terminer la matrice même si le nombre maximum de coups est atteint
class Affichage:
    def __init__(self,root=None):

        self.moteur = Moteur()
        
        self.root = root
        
        self.couleur = ["green","pink","red","orange","yellow","blue","purple","lightblue","saddle brown"]
        self.font = "Arial 25 roman"

        #Paramètres menus déroulants
        self.listeTaille = ["2","3","4","5","6","7","8","9","10","11","12","13","14","20","40","50","80","100","150","200"]
        self.listeCouleurs = ["2","3","4","5","6","7","8","9"]

        self.menuIA = tk.StringVar(self.root)
        self.menuTaille = tk.StringVar(self.root)
        self.menuCouleur = tk.StringVar(self.root)


        #piles de backtracking
        self.pile_setup = [self.moteur.matrice[:], self.moteur.position.copy(), self.moteur.voisins[:]]
        self.pileRetour = [self.pile_setup]
        self.pileAvancer = []

        #pour relancer apres défaite
        self.ok = False

        #nb de coups en cours et nb de coups max
        self.cpt_coup = 0
        self.max_coup = 22

        #prendre les infos de la fenêtre
        self.ecranLargeur = 1000
        self.ecranHauteur = 700
        
        ######################################################################################
        ##################### LISTE DES POSITIONS DES ELEMENTS ###############################

        self.positionX_info = self.ecranLargeur-150
        self.positionY_info = 100

        self.positionX_victoire = self.ecranHauteur//2
        self.positionY_victoire = self.ecranHauteur//2

        self.positionX_echec = self.positionX_info
        self.positionY_echec = self.positionY_info

        self.posiCPTX = self.ecranLargeur-140
        self.posiCPTY = self.ecranHauteur-40

        self.pbrX = self.posiCPTX-125
        self.pbrY = self.posiCPTY-125

        self.nvpX = self.pbrX
        self.nvpY = self.pbrY - 100

        self.retX = self.nvpX
        self.retY = self.nvpY -100

        self.avX = self.retX+ 130
        self.avY = self.retY

        self.MeDX = self.pbrX
        self.MeDY = self.avY-100

        self.MeD2X = self.MeDX+130
        self.MeD2Y = self.MeDY

        self.departY=0
        self.departX=0
       
        ######################################################################################

        #memorisation de la matrice de depart
        self.memoire = self.moteur.matrice[:]
        
        self.root.bind("<Escape>",self.quitterEchap)
        self.root.title("Flood It - The Game")
        
        self.canvas=tk.Canvas(root,width=self.ecranLargeur,height=self.ecranHauteur,borderwidth=0)
        
        self.canvas.grid(column=0, row=0, ipadx=0, ipady=0, sticky=tk.E+tk.N)
        
        #affichage respectif
        self.afficheJeu()
        self.afficheAutre()
        self.canvas.bind("<Button-1>",self.clic)
        
        
    def afficheJeu(self):
        '''
        depart | 0                                        depart+X | 0
        
        
                                (zone de jeu)
        
        
        depart | X                                          depart+X | X
        
            
        X = self.ecranHauteur * 3/4
        '''
        #zone de jeu
        angleDroitY = self.departY
        self.cote = int(self.ecranHauteur/ self.moteur.taille) # format de la fenêtre de jeu
        
        i = 0 #indice de la cellule de la matrice
        
        for ligne in range(self.moteur.taille):
            angleDroitX = self.departX
            for cell in range(self.moteur.taille):
                self.canvas.create_rectangle((angleDroitX,angleDroitY), (angleDroitX+self.cote,angleDroitY+self.cote), fill = self.couleur[self.moteur.matrice[i]], width=0)
                angleDroitX+=self.cote
                i+=1
            angleDroitY+=self.cote
        
        
    def afficheAutre(self):
        self.affiche_cpt = None #on créé affiche_cpt pour pouvoir le supprimer

        #BOUTON Recommencer
        self.bouton_r = None
        self.bouton_r = tk.Button(self.canvas, borderwidth=0, text="Recommencer",bg='pink',font = self.font, command=self.reinitialiser).place(x=self.pbrX,y=self.pbrY)
        
        #BOUTON Nouvelle Partie
        self.bouton_NVP = None
        self.bouton_NVP = tk.Button(self.canvas, borderwidth=0, text="Nouvelle Partie",bg='pink',font=self.font, command=self.relance).place(x=self.nvpX,y=self.nvpY)
        
        #BOUTON Retour/Avance
        self.bouton_retour = None
        self.bouton_retour = tk.Button(self.canvas, borderwidth=0, text="Retour",bg='blue',font=self.font, command=self.retour).place(x=self.retX,y=self.retY)
        
        self.bouton_avance = None
        self.bouton_avance = tk.Button(self.canvas, borderwidth=0, text="Avance",bg='blue',font=self.font, command=self.avancer).place(x=self.avX,y=self.avY)
        

        self.info = self.canvas.create_text(self.positionX_info,self.positionY_info, text="Cliquez sur une case\npour sélectionner une couleur.\n\nVous commencez en \nhaut à gauche.\n\nAppuyez sur 'Echap' pour\nquitter", font="Arial 14 roman")        
        
        self.affiche_coup()
        #self.menuDeroulant()
        self.victoire = None
        self.defaite = None
        

    def menuDeroulant(self):
        #Menu deroulant taille/couleur
        ###########################
        
        self.tail = tk.StringVar(self.root)
        self.tail.set(int(self.listeTaille[12]))

        self.tailleMat=tk.OptionMenu(self.root,self.tail,self.listeTaille)
        self.tailleMat.config(font=('Arial',20))
        self.tailleMat.place(x=self.MeDX,y=self.MeDY)

        self.textTaille = tk.Label(text="Taille",bg='lightblue')
        self.textTaille.place(x=self.MeDX,y=self.MeDY-10)


        ###########################
       
        self.coul = tk.StringVar(self.root)
        self.coul.set(int(self.listeCouleurs[4]))

        self.couleur=tk.OptionMenu(self.root,self.coul,self.listeCouleurs)
        self.couleur.config(font=('Arial',20))
        self.couleur.place(x=self.MeD2X,y=self.MeD2Y)

        self.textCoul = tk.Label(text="Couleurs",bg='lightblue')
        self.textCoul.place(x=self.MeD2X,y=self.MeD2Y-10)

        #############################

    def affiche_coup(self):
        self.canvas.delete(self.affiche_cpt)
        self.affiche_cpt = self.canvas.create_text(self.posiCPTX,self.posiCPTY, text=str(self.cpt_coup)+"/"+str(self.max_coup), font="Arial 42 roman")
           
    #recommencer la partie en cours
    def reinitialiser(self):
        self.moteur.initialisation()
        self.moteur.matrice=self.memoire[:]
        self.miseAzero()


    #fixe les variables du jeu à zéro
    def miseAzero(self):

        self.canvas.delete(self.defaite)
        self.canvas.delete(self.victoire)
        self.defaite = None
        self.victoire = None
        self.ok=False
        self.afficheJeu()
        self.cpt_coup = 0
        self.affiche_coup()
        self.vide_pile()
        

    #lance une nouvelle partie
    def relance(self):
            self.moteur.matrice = self.moteur.initialisation()
            self.memoire = self.moteur.matrice[:]

            self.miseAzero()

            print(self.tail.get(), self.coul.get())



    def clic(self,event):
        
        self.canvas.delete(self.info)
        
        if not(self.ok): #pas encore la victoire
            
            #conversion des coordonnées en indices
            x = (event.x - self.departX) // self.cote 
            y = (event.y - self.departY) // self.cote
            
            self.valide_coup(x,y)
            
        else:
            self.relance()
    
    
    #controle si les cases cliqué sont ok et si il faut effectuer un changement
    def valide_coup(self,x,y):
        t = self.moteur.taille-1
        if 0 <= x <= t and 0 <= y <= t :
            cell = x+y*self.moteur.taille
            if self.moteur.matrice[cell]!=self.moteur.matrice[0]:
                self.moteur.transform(self.moteur.matrice[cell])
                self.pileRetour.append([self.moteur.matrice[:], self.moteur.position.copy(), self.moteur.voisins[:]])
                self.pileAvancer = []
                self.afficheJeu()
                
                self.canvas.delete(self.affiche_coup)
                self.cpt_coup+=1
                self.affiche_coup()
            self.victory()
                   
            
    def victory(self):
        boolean_victoire = self.controle_victoire()
        if self.cpt_coup==self.max_coup and not(boolean_victoire):
            self.defaite = self.canvas.create_text(self.positionX_echec,self.positionY_echec, text="Dommage !", font="Arial 40 bold roman")
        
        elif boolean_victoire :
            self.ok=True
            if self.defaite!= None:
                self.canvas.delete(self.defaite)
                self.defaite = self.canvas.create_text(self.positionX_echec,self.positionY_echec, text="Courage !", font="Arial 40 bold roman")
            else:
                self.victoire = self.canvas.create_text(self.positionX_victoire,self.positionY_victoire, text= "Victoire !",  font="Arial 80 bold roman")
            
    
    def controle_victoire(self):
        verif = self.moteur.matrice[0]
        for j in self.moteur.matrice:
            if verif != j:
                return False
        return True
    
    def vide_pile(self):
        self.pileRetour = [self.pile_setup]
        self.pileAvancer = []

    def retour(self):
        print(self.pileRetour)
        taillePile = len(self.pileRetour)
        self.ok = False
        self.victoire = None
        if taillePile > 1 :
            #stockage de la dernière matrice dans avancer
            self.pileAvancer.append(self.pileRetour[-1][:])
            #on la retire de la pile
            self.pileRetour.pop()
            #self.pileRetour = self.pileRetour[:-1]
            
            #la matrice courante deviens la nouvelle dernière de la pile
            self.moteur.matrice = self.pileRetour[-1][0][:]
            self.moteur.position = self.pileRetour[-1][1].copy()
            self.moteur.voisins = self.pileRetour[-1][2][:]
            
            #affichage
            self.afficheJeu()
            

    def avancer(self):
        if len(self.pileAvancer) > 0 :
            #stockage de la dernière matrice dans avancer
            self.pileRetour.append(self.pileAvancer[-1][:])
            
            #la matrice courante deviens la nouvelle dernière de la pile
            self.moteur.matrice = self.pileAvancer[-1][0][:]
            self.moteur.position = self.pileAvancer[-1][1].copy()
            self.moteur.voisins = self.pileAvancer[-1][2][:]
            
            #on la retire de la pile
            self.pileAvancer.pop()
            #self.pileAvancer = self.pileAvancer[:-1]
            
            self.afficheJeu()
            
            self.victory()


    def quitterEchap(self,event):
        self.quitter()

    def quitter(self):
        self.root.destroy()

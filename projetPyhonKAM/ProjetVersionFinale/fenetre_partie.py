from tkinter import *
from partie import Partie
from partie import Deplacement
from vehicule import Vehicule
from solveur import Solveur
from PIL import Image,ImageTk
from time import process_time
from gestion_son import Musique







class FenetrePartie(Partie):
    ''' La classe FenetrePartie  hérite de la classe Partie et représente
    graphiquement le plateau de jeu en lancant une fenetre Tkinter 
    Elle sera capable de gérer les évènements.
    '''

    def __init__(self,niveau,master,size=(800,600),position=None):
        
        #DETERMINATION DE LA MATRICE, LA SORTIE SELON LE NIVEAU DONNE
        (matrice,difficulte,sortie,nb_niveaux)=self.load_niveau(niveau)
        self.nb_niveaux=nb_niveaux 
        self.niveau=niveau # indice dans le fichier les_parties.txt
        self.sortie=sortie # G ou D pour droite ou gauche
        super().__init__(matrice,sortie)
        self.difficulte=difficulte
        #VARIABLES DE DEPLACEMENTS  COORD DANS LE CANEVAS
        self.vecteur_deplacement=(0,0)
        self.clic_origine=(0,0)
        self.coord_selected=(0,0) 
        self.selected=None
        #BOOLEANS
        self.souris_sur_tag=None
        self.pause=True
        self.a_commence=False
        self.est_redimensionnee=False
        #DICTIONNAIRES D'IMAGES et de BOUTONS(fonctions)
        self.images={}
        self.boutons= { 'bouton_son' : self.bouton_son , 'bouton_retour' : self.bouton_Retour ,
                      'bouton_recommencer' : self.bouton_recommencer, 'bouton_indice':self.bouton_indice,
                      'bouton_fleche_av': self.bouton_fleche_av , 'bouton_fleche_ar' : self.bouton_fleche_ar,
                      'bouton_pause' : self.bouton_pause}
        self.nb_voitures=4 #4 images de voitures dans le fichier
        self.nb_camions=3  #3 images de camion dans le fichier
        
        # TIMER
        self.chrono=0
        self.debut=process_time()
        self.timer_pause=0 
        self.timer_indice=0
        self.timer_victoire=0
        self.temps_indice=5   # temps avant de pouvoir utiliser  bouton_indice
        self.temps_recommencer=5 # Temps avant de pouvoir utiliser bouton_recommencer
                
        ## DIMENSIONS FENETRE
        self.width=size[0]
        self.height=size[1]
        self.bord_x=self.width//20
        self.bord_y=self.height//40
        self.case=int(self.width//8.4)       
        
        
        #LANCER FENETRE ET LIER SES EVENTS
        self.root=master
        #self.root.resizable(width=True,height=True)
        self.canvas=Canvas(self.root,width=self.width,height=self.height,bg="#f3dac3")
        self.canvas.pack(side="top",padx=0,pady=0)
        self.root.bind('<Button-1>',self.selection)
        self.root.bind('<B1-Motion>',self.updateDeplacement)
        self.root.bind('<ButtonRelease-1>',self.unselect)
        self.root.bind('<Motion>' , self.souris_sur )
        self.root.bind('<Configure>',self.resize)
        self.root.bind('<Key>',self.pressed)
        if position ==None:
            #On recentre
            self.root.geometry(f'{self.width}x{self.height}+{self.root.winfo_screenwidth()//2-self.width//2}+{self.root.winfo_screenheight()//2-self.height//2}')
        else:
            #On garde les parametres
            self.root.geometry(f'{self.width}x{self.height}+{position[0]}+{position[1]}')

        self.root.minsize(400,300)
        self.font='Segoe UI Light'
        self.load_images_Vehicules()
        self.load_images_Menu()
        

            
        
     
        
     
   
          
    #############################################################################################################################
    #############################################################################################################################
    #####                    EVENT HANDLERS                                                                                   ###
    #############################################################################################################################
    #############################################################################################################################
   

    def bouton_son(self):
        if  Musique.etat_musique == 0: 
            Musique.pause()
        else: 
            Musique.unpause()

    def bouton_indice(self):
        if not (self.pause) and not (self.est_gagnee) and int(self.chrono-self.timer_indice)>=self.temps_indice:

            Musique.playBruitage() 
            solver=Solveur(self.matrice,self.sortie)
            deplacements=solver.solver()
            deplacements.reverse()
            self.pile_deplacements_retour=deplacements
            self.timer_indice=self.chrono

            
        
    
    def bouton_pause(self):
        Musique.playBruitage() 
        
        if not(self.a_commence): # JOUER
            self.a_commence=True
        if not self.est_gagnee:   #PAUSE / CONTINUER
            self.pause=not(self.pause)
            self.draw()
        else:  #SUIVANT
            self.canvas.pack_forget()
            if self.niveau==self.nb_niveaux-1:
                self.niveau=-1
            self =FenetrePartie((self.niveau+1),self.root,(self.width,self.height),(self.root.winfo_x(),self.root.winfo_y()))
            self.afficher()
            

    
    def bouton_recommencer(self):
        if not(self.pause) and self.pile_deplacements and (not(self.est_gagnee) or (self.est_gagnee and self.timer_victoire>self.temps_recommencer)):
            Musique.playBruitage() 
            self.recommencer()
            #Mises a jour des timers
            self.debut+=self.timer_pause+self.timer_victoire
            self.timer_pause=self.chrono
            self.timer_victoire=0
            self.chrono=0
            self.timer_indice=0
            
        
    def bouton_Retour(self):
        from menu import FenetreMenuPrincipale
        Musique.playBruitage() 
        self.canvas.pack_forget()
        self=FenetreMenuPrincipale(self.root)
        self.aff_menu_principale()
        
    
    def bouton_fleche_av(self):
        if self.pile_deplacements_retour:
            Musique.playBruitage() 
            self.retour_avant()
            self.est_gagnee=self.estGagnee()
            if self.est_gagnee:
                Musique.playVictoire()
            self.draw()
            
        
    
    def bouton_fleche_ar(self):
        if self.pile_deplacements and not (self.est_gagnee):
            Musique.playBruitage() 
            self.retour_arriere()
            self.draw()
            self.pile_deplacements_retour=[]
            


    def selection(self,event):
        ''' si le click est dans la grille on met a jour l'id selected
        on met a jour clic_origine
        et on redessine car la couleur du vehicule selected change '''
        tag=self.canvas.find_closest(event.x,event.y)
        leTag=self.lireTag(tag)
        if len(leTag)>0:
            #Cas d'un vehicule selectionné
            if leTag[0]=="V" and not self.pause and not self.est_gagnee:
                self.clic_origine=(event.x,event.y)
                self.vecteur_deplacement=(0,0)
                v=self.vehicules[int(leTag[1:])]
                self.selected=v.id
                self.coord_selected=v.coord
            if leTag in self.boutons:
                self.boutons[leTag]()

            self.draw()


    
    def updateDeplacement(self,event):
        ''' lorsque la souris bouge avec le click  gauche activé :
            on met a jour le vecteur_deplacement
            et on redessine'''
        
        self.vecteur_deplacement=(event.x-self.clic_origine[0],event.y-self.clic_origine[1])
        self.draw()
        

    def unselect(self,event):
        '''lorsqu'on lache le click gauche de la souris :
                -on remet les attributs par defauts:
                vecteur_deplacement,selected
 
                -on met a jour la matrice selon le mouvement effectué

        '''
        if self.selected and self.coord_selected!=self.vehicules[self.selected].coord :
            self.updatePartie(self.vehicules[self.selected],self.coord_selected)
            self.est_gagnee=self.estGagnee()
            if self.est_gagnee:
                Musique.playVictoire()
                
            self.pile_deplacements_retour=[]
            
        self.vecteur_deplacement=(0,0)
        self.selected=None
        self.draw()



    
    
    def resize(self,event):
        '''redimensionne le canvas par rapport a la fenetre et met en mode pause
        et met a jour la variable est_redimmensionnee
        On ne load pas les images on attend la fin de l'evenevement configure et la reentrée de la souris
        sur le canvas.
        '''
        if event.width!=self.width : #Cas d'une configure qui n'est pas un déplacement de la fenetre
            self.pause=True
            self.est_redimensionnee=True
            W=self.root.winfo_width()
            H=self.root.winfo_height()
            self.width=W
            self.height=int(W*3/4)
            #Maibtien du ratio 4:3
            if self.height>H:
                self.height=H
                self.width=int(self.height*4/3)
            #mise a jour des variables de taille
            self.canvas.config(width=self.width,height=self.height)
            self.bord_x=self.width//20
            self.bord_y=self.height//40
            self.case=int(self.width//8.4)

            self.draw()



    
    def souris_sur(self,event):
        '''modifie les couleurs des widgets selon la position de la souris
        et appelle redimensionner selon la variable est_redimensionnee'''
        if self.est_redimensionnee:
            self.redimensionner()
        tag=self.canvas.find_closest(event.x,event.y)
        leTag=self.lireTag(tag)
        if len(leTag)>0:
            self.souris_sur_tag=leTag
        else:
            self.souris_sur_tag=None
        self.draw()

    def pressed(self,event):
        '''si  bouton espace appuyé on appelle bouton_pause'''
        if event.char == ' 'and not self.est_redimensionnee:
            if not self.est_gagnee and self.a_commence:   #PAUSE / CONTINUER
                self.pause=not(self.pause)
                self.draw()
        
        

        
    
   
    def update_chrono(self):
        '''timers calculés en fonction du début de la partie et des pauses eventuelles et 
        de la victoire ''' 
        if not self.est_gagnee and not(self.pause):
            now=self.chrono=process_time()-self.timer_pause-self.debut
        elif self.pause:
            self.timer_pause=process_time()-self.chrono-self.debut
        else:
            self.timer_victoire=process_time()-self.chrono-self.debut-self.timer_pause
        self.draw()
        self.root.after(10,self.update_chrono)

    
    def redimensionner(self):
        '''redimensionne la fenetre et toutes ses dimensions et recharge les images lorsque
        la souris rerentre dans le canvas'''
        self.est_redimensionnee=False
        self.update_chrono()
        W=self.root.winfo_width()
        H=self.root.winfo_height()
        self.width=W
        self.height=int(W*3/4)
        if self.height>H:
            self.height=H
            self.width=int(self.height*4/3)
        #Met a jour les variables de taille
        self.canvas.config(width=self.width,height=self.height)
        self.bord_x=self.width//20
        self.bord_y=self.height//40
        self.case=int(self.width/8.4)
        self.load_images_Vehicules()
        self.load_images_Menu()
        self.draw()
    
    def lireTag(self,id_tag):
        '''retourne le tag de l' id_tag_ sur le canvas'''
        return self.canvas.itemconfig(id_tag)['tags'][-1][:-8]


    #############################################################################################################################
    #############################################################################################################################
    #####                    METHODES LIEES AUX COORDONNEES VEHICULE ET PLATEAU                                               ###
    #############################################################################################################################
    #############################################################################################################################
    
    def coordCanvas_coordMatrice(self,x,y):
        ''' retourne les coordonnées (i,j) de la matrice selon les coordonnées
        (x,y) de la fenetre  '''
        (i,j)=((y-self.bord_y)//self.case,(x-self.bord_x)//self.case)
        return (i,j)

        
        
    #return le coin sup gauche,inf droit et couleur du rectangle representant la voiture
    def vehiculeIntoCoord(self,vehicule):
        ''' Retourne selon les coordonnées du vehicule dans la matrice et la taille self.case:
        A : les coordonnées du coin sup gauche dans la fenetre
        B : les coordonnées du in droit dans la fenetre  
                
        Pour ensuite créer le rectangle dans le canvas '''      
        (y,x)=vehicule.coord
        (xD,yD)=Vehicule.DIRECTIONS["Bas" if vehicule.orientation=="V" else "Droite"]
        (x,y)=(self.bord_x+x*self.case,self.bord_y+y*self.case)   
        return (x,y)
    
    #########################
    #TO DO 
    #Deplacer les rectangles au lieu de clear canvas et redessiner par desssus
    #########################
    def selectedIntoCoord(self):
        ''' Retourne les nouvelles coordonnées du véhicule selectionné selon le mouvement de la souris
        et gère les collisions '''
        vehicule=self.vehicules[self.selected]
        (aX,aY)= self.vehiculeIntoCoord(vehicule)
        vX,vY=self.vecteur_deplacement
        possible_deplacement=self.vehiculePossibleDeplacement(vehicule)
        if vehicule.orientation=="V":
            try_deplacement=self.coordCanvas_coordMatrice(aX,aY+vY)  # coord du mouvement d'arrivée dans la matrice
            if try_deplacement in possible_deplacement :
                aY+=vY
            elif possible_deplacement: 
                # prend le min ou le max des Deplacements possibles comme collision
                aY=self.bord_y+self.case*(max(possible_deplacement)[0]+1 if vY>=0 else min(possible_deplacement)[0]) 
                
        else:
            try_deplacement=self.coordCanvas_coordMatrice(aX+vX,aY)  # coord du mouvement d'arrivée dans la matrice
            if try_deplacement in possible_deplacement:
                aX+=vX
            elif possible_deplacement:
                # prend le min ou le max des Deplacements possibles comme collision
                aX=self.bord_x+self.case*(max(possible_deplacement)[1]+1 if vX>=0 else min(possible_deplacement)[1])
                
        #determine les coordonnées de la matrice pour lesquelles l'arriere du Vehicule est le plus proche
        self.coord_selected=( (aY-self.bord_y)//self.case + int((aY-self.bord_y)%self.case>self.case/2),(aX-self.bord_x)//self.case+int((aX-self.bord_x)%self.case>self.case/2))
        
        return (aX,aY)


    #############################################################################################################################
    #############################################################################################################################
    #####                    METHODES LIEES AUX DATA                                                                          ###
    #############################################################################################################################
    #############################################################################################################################
    
    def load_niveau(self,niveau):
        with open('assets/les_parties.txt','r') as f:
            les_parties=f.readlines()
        decoupe=les_parties[niveau].split()
        decoupe_int =  [ int(id) for id in decoupe[0].split(',')]
        matrice= [decoupe_int[ligne*6:(ligne+1)*6] for ligne in range(6)]
        difficulte=decoupe[1]
        sortie=decoupe[2]
        nb_niveaux=len(les_parties)
        return matrice,difficulte,sortie,nb_niveaux

    
    def load_images_Vehicules(self):
        '''Met a jour le dictionnaire d'images'''
        version_voiture=0
        version_camion=0
        for id in self.vehicules.keys():
            v=self.vehicules[id]
            width= self.case if v.orientation=="V" else self.case*v.lg
            height=self.case if v.orientation=="H" else self.case*v.lg
            
            if id!=1:
                #Image selon la type de vehicule
                lien=f'assets/vehicules/{v.orientation}{v.lg} N{1+(version_voiture if v.lg==2 else version_camion)}.png'
                img=ImageTk.PhotoImage(Image.open(lien).resize((width,height),Image.ANTIALIAS))
                self.images[str(id)]=img
                #sa version selectionnée
                lien=f'assets/vehicules/{v.orientation}{v.lg}S N{1+(version_voiture if v.lg==2 else version_camion)}.png'
                img=ImageTk.PhotoImage(Image.open(lien).resize((width,height),Image.ANTIALIAS))
                self.images[str(id)+"S"]=img
                #on modifie la prochaine version
                version_voiture=(version_voiture+int(v.lg==2))%self.nb_voitures
                version_camion=(version_camion+int(v.lg==3))%self.nb_camions
                
            elif id==1 :
                #Image vehicule principal
                img=ImageTk.PhotoImage(Image.open(f'assets/vehicules/P2{self.sortie}.png').resize((width,height),Image.ANTIALIAS))
                self.images[str(id)]=img
                 #sa version selectionnée
                img=ImageTk.PhotoImage(Image.open(f'assets/vehicules/P2S{self.sortie}.png').resize((width,height),Image.ANTIALIAS))
                self.images[str(id)+"S"]=img

        
    
    def load_images_Menu(self):
        '''met a jour le dictionnaire d'images'''
        def load_image(file,size):
            '''prend le nom d'un fichier image et sa taille voulue 
            et la load dans le dictionnaire Images version selectionnéee
             et non sélectionnée'''
            nom_image=file.split('/')[-1][:-4]
            #non selectionee
            img=ImageTk.PhotoImage(Image.open(file).resize(size),Image.ANTIALIAS)
            self.images[nom_image]=img
            #selectionee
            img=ImageTk.PhotoImage(Image.open(file[:-4]+'_S'+file[-4:]).resize((int(size[0]*1.03),int(size[1]*1.03))),Image.ANTIALIAS)
            self.images[nom_image+'_S']=img

        taille_icone=(self.width//15,self.height//12)
        taille_bouton=(self.width//6,self.height//11)
        
        load_image('assets/icon son/son0.png',taille_icone)
        load_image('assets/icon son/son2.png',taille_icone)
        load_image('assets/icon retour/ret.png',taille_icone)
        load_image('assets/icon fleche/fleche0.png',taille_icone)
        load_image('assets/icon fleche/fleche2.png',taille_icone)
        load_image('assets/menu/recommencer.png',taille_bouton)
        load_image('assets/menu/indice.png',taille_bouton)
        for i in range(4):
            load_image(f'assets/menu/pause{i}.png',taille_bouton)
        
        


        #images disabled boutons
        img=ImageTk.PhotoImage(Image.open('assets/icon fleche/fleche0_D.png').resize(taille_icone),Image.ANTIALIAS)
        self.images['fleche0_D']=img

        img=ImageTk.PhotoImage(Image.open('assets/icon fleche/fleche2_D.png').resize(taille_icone),Image.ANTIALIAS)
        self.images['fleche2_D']=img

        img=ImageTk.PhotoImage(Image.open('assets/menu/indice_D.png').resize(taille_bouton),Image.ANTIALIAS)
        self.images['indice_D']=img

        img=ImageTk.PhotoImage(Image.open('assets/menu/recommencer_D.png').resize(taille_bouton),Image.ANTIALIAS)
        self.images['recommencer_D']=img


    


    #############################################################################################################################
    #############################################################################################################################
    #####                    METHODES DE DRAW                                                                                 ###
    #############################################################################################################################
    #############################################################################################################################
    

    def draw(self):
        self.canvas.delete("all")
        self.drawGrille()
        self.drawInfo()
        if not(self.est_redimensionnee):
            self.drawVehicules()
            self.drawMenu()
        
    def drawVehicules(self):
        '''recupere les positions des images et  les affiche'''
        for vehicule in self.vehicules.values():
            if self.selected and vehicule.id==self.selected and self.vecteur_deplacement!=(0,0) :
                (x,y)=self.selectedIntoCoord()
            elif vehicule.id==1 and self.est_gagnee:
                arrivée=self.width-2*self.case if self.sortie=='D' else 0
                (x,y)=self.vehiculeIntoCoord(vehicule)
                if x<arrivée and self.sortie=='D':
                    x+=self.timer_victoire*120
                elif x>arrivée and self.sortie!='D':
                    x-=self.timer_victoire*120
                else:
                    x=self.width if self.sortie=='D' else -2*self.case
            else:
                (x,y)= self.vehiculeIntoCoord(vehicule) 

            self.canvas.create_image(x,y,image=self.images[str(vehicule.id)+("S" if self.selected and vehicule.id==self.selected else "")],anchor="nw",tags=f'V{vehicule.id}')
    
    
    def drawGrille(self):
        def coordIntoRect(i,j):
            '''retourne le coin sup gauche et inf droit d'une self.case de coordonnée (i,j) de la matrice'''
            (x,y)=(self.bord_x+j*self.case,self.bord_y+i*self.case)
            if self.pause:
                 color="grey26" if (i+j)%2==0 else "gray20"
            else:
                 color="mint cream" if (i+j)%2==0 else "azure3"
            return ((x,y),(x+self.case,y+self.case),color)

        def drawArrivée(e,couleur):
            '''affiche les bords de la grille et laisse un trou selon la position de la sortie
            e : int epaisseur du bord 
            couleur : string couleur du bord '''
            x=self.bord_x
            y=self.bord_y
            h=self.case*6
            yArrivee=self.vehicules[1].coord[0]
            #HAUT BAS
            self.canvas.create_rectangle(x-e,y-e,x+h+e,y,outline=couleur,fill=couleur)
            self.canvas.create_rectangle(x-e,h+y,x+h+e,h+y+e,outline=couleur,fill=couleur)
            #BORD GAUCHE ET DROITE
            if self.sortie=='D':
                self.canvas.create_rectangle(x-e,y-e,x,h+y+e,outline=couleur,fill=couleur)
                self.canvas.create_rectangle(x+h,y-e,x+h+e,yArrivee*self.case+y,outline=couleur,fill=couleur)
                self.canvas.create_rectangle(x+h,y+(yArrivee+1)*self.case,x+h+e,y+h+e,outline=couleur,fill=couleur)
            else:
                self.canvas.create_rectangle(x+h,y-e,x+h+e,h+y+e,outline=couleur,fill=couleur)
                self.canvas.create_rectangle(x-e,y-e,x,yArrivee*self.case+y,outline=couleur,fill=couleur)
                self.canvas.create_rectangle(x-e,y+(yArrivee+1)*self.case,x,y+h+e,outline=couleur,fill=couleur)
        rects=(coordIntoRect(i,j) for i in range(6) for j in range(6))
        
        for (A,B,C) in rects:
            self.canvas.create_rectangle(A,B,fill=C,outline=C)
        drawArrivée(6,"cadet blue")
    
    
       

    

    def drawMenu(self):
              
        def drawSon(x,y):
            surligner= self.souris_sur_tag and self.souris_sur_tag=='bouton_son'
            self.canvas.create_image(x,y,image=self.images[f'son{Musique.etat_musique}'+('' if not(surligner) else '_S')],anchor="nw",tags=f'bouton_son')
            
        def drawRetour(x,y):
            surligner= self.souris_sur_tag and self.souris_sur_tag=='bouton_retour'
            self.canvas.create_image(x,y,image=self.images[('ret' if not surligner else 'ret_S')],anchor="nw",tags=f'bouton_retour')
       
        def drawFlecheAvant(x,y):
            surligner= self.souris_sur_tag and self.souris_sur_tag=='bouton_fleche_av'
            disabled= len(self.pile_deplacements_retour)==0 or self.pause
            nom_image= 'fleche2'+('' if not(surligner or disabled) else ('_S' if not(disabled) else '_D'))
            self.canvas.create_image(x,y,image=self.images[nom_image],anchor="nw",tags='bouton_fleche_av')

        def drawFlecheArriere(x,y):
            surligner= self.souris_sur_tag and self.souris_sur_tag=='bouton_fleche_ar'
            disabled= len(self.pile_deplacements)==0 or self.pause or self.est_gagnee
            nom_image= 'fleche0'+('' if not(surligner or disabled) else ('_S' if not(disabled) else '_D'))
            self.canvas.create_image(x,y,image=self.images[nom_image],anchor="nw",tags='bouton_fleche_ar')

        def drawBoutonRecommencer(x,y):
            surligner=self.souris_sur_tag and self.souris_sur_tag=='bouton_recommencer'
            disabled=self.pause or not(self.pile_deplacements) or (self.est_gagnee and self.timer_victoire<self.temps_recommencer)
            if not(disabled):
                self.canvas.create_image(int(x-(0.02*(width_menu-bord_x_menu) if surligner else 0)),y,image=self.images['recommencer'+('' if not surligner else '_S')],anchor="nw",tags='bouton_recommencer')
            else:
                self.canvas.create_image(x,y,image=self.images['recommencer_D'],anchor="nw",tags='bouton_recommencer')
        
        def drawBoutonIndice(x,y):
            surligner=self.souris_sur_tag and self.souris_sur_tag=='bouton_indice'
            disabled=self.pause or self.estGagnee() or int(self.chrono-self.timer_indice)<self.temps_indice
            if not disabled:
                self.canvas.create_image(int(x-(0.02*(width_menu-bord_x_menu) if surligner else 0)),y+height_bouton,image=self.images['indice'+('' if not surligner else ('_S'))],anchor="nw",tags='bouton_indice')
            else:
                self.canvas.create_image(x,y+height_bouton,image=self.images['indice_D'],anchor="nw",tags='bouton_indice')
           
        def drawBoutonPause(x,y):
            surligner=self.souris_sur_tag and self.souris_sur_tag=='bouton_pause'
            num= 3 if not(self.a_commence) else  2 if self.est_gagnee else 1 if self.pause else 0 
            self.canvas.create_image(int(x-(0.02*(width_menu-bord_x_menu) if surligner else 0)),y+2*(height_bouton),image=self.images[f'pause{num}'+('_S' if surligner else '')],anchor="nw",tags='bouton_pause')


        #dimensions locales
        width_menu=1.3*self.case
        height_menu=3*self.case
        bord_x_menu=width_menu/9
        bord_y_menu=height_menu/20
        height_bouton=int(self.case/1.54)-bord_y_menu/2
        x=6*self.case+1.7*self.bord_x+bord_x_menu/2.4
        y=self.bord_y+bord_y_menu/1.3
        #contour    
        self.canvas.create_rectangle(6*self.case+1.7*self.bord_x,self.bord_y,7.5*self.case+1.7*self.bord_x,self.bord_y+3*self.case,fill='#9daab0',outline='#071860'  ,width=self.width//250)
        #Objets crées
        drawBoutonRecommencer(x,y)
        drawBoutonIndice(x,y)
        drawBoutonPause(x,y)
        drawSon(x+0.8*bord_x_menu,y+3.1*(height_bouton+bord_y_menu))  #ajustement lié au zones transparentes des images
        drawRetour(x+4.9*bord_x_menu,y+3.05*(height_bouton+bord_y_menu)) # ajustement lié au zones transparentes des images
        drawFlecheAvant(x+5*bord_x_menu,y+3*height_bouton)
        drawFlecheArriere(x+0.9*bord_x_menu,y+3*height_bouton)

        


    def drawInfo(self):
        '''permet d'afficher les 4 éléments et le cadre des info de la partie  '''

        def drawLevel(x,y):
            self.canvas.create_text(x,y,text="Difficulté",font=(self.font,self.case//6,'bold'),fill="black")
            self.canvas.create_text(x,y+ecart_texte,text=self.difficulte,font=(self.font,self.case//8,'bold'),fill="black")

        def drawStage(x,y):
            self.canvas.create_text(x,y,text="Niveau",font=(self.font,self.case//6,'bold'),fill="black")
            self.canvas.create_text(x,y+ecart_texte,text=str(self.niveau+1),font=(self.font,self.case//8,'bold'),fill="black")

        def drawDeplacement(x,y):
            self.canvas.create_text(x,y,text="Déplacements",font=(self.font,int(self.case/6.5),'bold'),fill="black")
            self.canvas.create_text(x,y+ecart_texte,text=str(len(self.pile_deplacements)),font=(self.font,self.case//8,'bold'),fill="black")

        def drawChrono(x,y):
            self.canvas.create_text(x,y,text="Temps",font=(self.font,self.case//6,'bold'),fill="black" )
            self.canvas.create_text(x,y+ecart_texte,text=f'{int(self.chrono//60)} mn {int(self.chrono%60)} s',font=(self.font,self.case//8,'bold'),fill="black" )
            
        #dimensions locales
        x=7.45*self.case
        y=self.bord_y+4.18*self.case
        ecart_texte=self.case/4
        ecart_info=self.case/2.1
        #contour
        self.canvas.create_rectangle(6*self.case+1.7*self.bord_x,self.bord_y+4*self.case,7.5*self.case+1.7*self.bord_x,
        self.bord_y+6*self.case,fill="#ffe27d",outline='#d49406' ,width=self.width//250)
        #Objets crées
        drawStage(x,y)
        drawLevel(x,y+ecart_info)
        drawDeplacement(x,y+2*ecart_info)
        drawChrono(x,y+3*ecart_info)

    
        



    





   
    
#############################################################################################################################
#############################################################################################################################
#####                    METHODES PRINCIPALE DE LA FENETRE                                                                ###
#############################################################################################################################
#############################################################################################################################
        
    '''mainloop de la fenetre Tkinter'''

    def afficher(self):
        self.draw()
        self.update_chrono()
    


    

    

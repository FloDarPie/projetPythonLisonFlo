import tkinter as tk
from PIL import Image, ImageTk
from gestion_son import Musique



###############################################################################################################
#              CLASSE DE LA FENETRE DE MENU PRINCIPALE : LORS DU LANCEMENT ET RETOUR AU MENU                  #
##############################################################################################################


class FenetreMenuPrincipale:
    
    def __init__(self, root=None,size=(800,600)):
        self.root = root
        self.canva=tk.Canvas(root,width=800,height=600,borderwidth=0,bg="#f1f2ee")
        self.bg=None
        
        self.root.title("Rush Before 19H")

        ### CENTRER LA FENETRE AU MILIEU DE L'ECRAN ###
        self.width=800
        self.height=600

        screen_width=root.winfo_screenwidth()
        screen_height=root.winfo_screenheight()
        x= (screen_width/2)-(self.width/2)
        y=(screen_height/2)-(self.height/2)
        self.root.geometry(f'{self.width}x{self.height}+{int(x)}+{int(y)}')
        self.root.minsize(800,600)

        ## On a fait le choix de garder un menu qui n'est qu'une fenêtre de 800x600 pour plus de praticité. 


       
        #### BOUTON "ACCEDER AU NIVEAUX DES NIVEAUX ET DIFFICULTE : Jouer" ##### 
        self.boutton_niveaux=None
        self.image_jouer=None

        JOUER_I = Image.open(r"assets/menu/JOUER.png")
        self.image_jouer = ImageTk.PhotoImage(JOUER_I, Image.ANTIALIAS)

        self.boutton_niveaux=tk.Button(self.canva, image=self.image_jouer,borderwidth=0, bg="#f1f2ee",command=self.ouvrir_choix_niv)


        #### BOUTON "COMMENT JOUER" ##### 
        self.boutton_regles=None
        self.image_regles=None

        REGLES = Image.open(r"assets/menu/REGLES.png")
        self.image_regles = ImageTk.PhotoImage(REGLES, Image.ANTIALIAS)

        self.boutton_regles=tk.Button(self.canva, image=self.image_regles,borderwidth=0,bg="#f1f2ee",
                  command=self.ouvrir_regles,cursor="question_arrow")


        ### BOUTON QUITTER LE JEU ###

        self.boutton_quitter=None
        self.root.protocol("WM_DELETE_WINDOW",self.quitter)

        QUITTER_I = Image.open(r"assets/menu/QUITTER.png")
        self.image_quitter = ImageTk.PhotoImage(QUITTER_I, Image.ANTIALIAS)

        self.boutton_quitter=tk.Button(self.canva, image=self.image_quitter,borderwidth=0,bg="#f1f2ee",activebackground="#f1f2ee",
            command=self.quitter,cursor="X_cursor")
        
        #Mise en place du fond sur la fenêtre : 
        self.ouvrir_fond()


        #Creation des boutons sur la fenêtre : 

        self.canva.create_window(400,300,window=self.boutton_niveaux,anchor="center")
        self.canva.create_window(400,380,window=self.boutton_regles,anchor="center")
        self.canva.create_window(400,460,window=self.boutton_quitter,anchor="center")

        ### GESTION DU SON SUR LA FENETRE : ###
        Musique.creation_bouton(self.canva)
        
        self.canva.pack()
        
        #Initialisation de l'icon du jeu sur la fenêtre : 
        self.root.iconphoto(False, tk.PhotoImage(file='assets/icon fenetre/ICON V2.png'))

    def ouvrir_fond(self):
        lien = r"assets/menu bg/menu_principal.png"
        self.bg = ImageTk.PhotoImage(Image.open(lien).resize((800,600),Image.ANTIALIAS))
        self.canva.create_image(0,0,image=self.bg,anchor="nw")
        

    def aff_menu_principale(self):
        self.canva.pack()

    def ouvrir_regles(self):
        self.menu_regles = MenuRegles(master=self.root, app=self)
        self.canva.pack_forget()
        self.menu_regles.lancer_regles()

    def ouvrir_choix_niv(self):
        self.menu_niveaux = MenuNiveaux(master=self.root, app=self)
        self.canva.pack_forget()
        self.menu_niveaux.lancer_niv()

    def quitter(self):
        self.root.destroy()


###############################################################################################################
#                   CLASSE DE LA PAGE GUIDANT LE JOUEUR SUR LES REGLES ET LES COMMANDES                     #
##############################################################################################################
class MenuRegles:
    def __init__(self, master=None, app=None):
        self.master = master
        self.app = app
        self.canva = tk.Canvas(self.master,borderwidth=0,width=800,height=600)
        self.bg=None


        #### BOUTON RETOUR AU MENU PRINCIPAL ###

        self.boutton_retour=None 
        self.image_retour=None 

        RETOUR= Image.open(r"assets/menu/RETOUR_S.png")
        self.image_retour= ImageTk.PhotoImage(RETOUR, Image.ANTIALIAS)
        self.boutton_retour=tk.Button(self.master, image=self.image_retour, borderwidth=0, command=self.retour_menu,activebackground="#f1f2ee")


        self.background()

        #Creation des boutons retour et de la gestion du son : 

        self.canva.create_window(400,515,window=self.boutton_retour,anchor="center")

        Musique.creation_bouton(self.canva)

        self.canva.pack()


    def background(self):
        lien = r"assets/menu bg/bg_regles.png"
        self.bg = ImageTk.PhotoImage(Image.open(lien).resize((800,600),Image.ANTIALIAS))
        self.canva.create_image(0,0,image=self.bg,anchor="nw")

    def lancer_regles(self):
        self.canva.pack()

    def retour_menu(self):
        self.canva.pack_forget()
        self=FenetreMenuPrincipale(self.master)
        self.aff_menu_principale()



###############################################################################################################
#                   CLASSE DE LA PAGE DE CHOIX DES NIVEAUX ET DIFFICULTE DU JEU                             #
##############################################################################################################
class MenuNiveaux:
    def __init__(self, master=None, app=None):
        self.master = master
        self.app = app
        self.canva = tk.Canvas(self.master,borderwidth=0,width=800,height=600)
        self.bg=None

        ## Importation des images de flèches de sélections de niveaux : ### 
        fleche_gaucheN=Image.open(r"assets/icon fleche/menu/fleche0.png")
        fleche_gaucheS=Image.open(r"assets/icon fleche/menu/fleche0_S.png")
        fleche_gaucheD=Image.open(r"assets/icon fleche/menu/fleche0_D.png")

        fleche_droiteN=Image.open(r"assets/icon fleche/menu/fleche2.png")
        fleche_droiteS=Image.open(r"assets/icon fleche/menu/fleche2_S.png")
        fleche_droiteD=Image.open(r"assets/icon fleche/menu/fleche2_D.png")

        self.image_gaucheN=ImageTk.PhotoImage(fleche_gaucheN,Image.ANTIALIAS)
        self.image_gaucheS=ImageTk.PhotoImage(fleche_gaucheS,Image.ANTIALIAS)
        self.image_gaucheD=ImageTk.PhotoImage(fleche_gaucheD,Image.ANTIALIAS)

        self.image_droiteN=ImageTk.PhotoImage(fleche_droiteN,Image.ANTIALIAS)
        self.image_droiteS=ImageTk.PhotoImage(fleche_droiteS,Image.ANTIALIAS)
        self.image_droiteD=ImageTk.PhotoImage(fleche_droiteD,Image.ANTIALIAS)



        ### BOUTON DE CHOIX DE DIFFICULTE ###

        #Importation images du texte de difficulté : 

        diff1=Image.open(r"assets/icon niveaux/facile.png")
        self.facile=ImageTk.PhotoImage(diff1,Image.ANTIALIAS)

        diff2=Image.open(r"assets/icon niveaux/normal.png")
        self.normal=ImageTk.PhotoImage(diff2,Image.ANTIALIAS)

        diff3=Image.open(r"assets/icon niveaux/difficile.png")
        self.difficile=ImageTk.PhotoImage(diff3,Image.ANTIALIAS)


        #Creation du Label affichant la difficulté au joueur : 
        self.aff_difficulte=tk.Label(self.master,text="Facile",image=self.facile,bg="#f1f2ee")
    
        #Fonctions liées aux events de selection et clique sur les flèches de selection de difficultés : 

        def bouton_diff_av(event=None):
            if(self.aff_difficulte['text']=="Normal"):
                self.aff_difficulte['text']="Facile"
                self.aff_difficulte['image']=self.facile
                self.canva.itemconfig(self.boutton_avant,image=self.image_gaucheD)

            elif(self.aff_difficulte['text']=="Difficile"):
                self.aff_difficulte['text']="Normal"
                self.aff_difficulte['image']=self.normal
                self.canva.itemconfig(self.boutton_arr,image=self.image_droiteN)
    

        def bouton_diff_av_S(event=None):
            if(self.aff_difficulte['text']!="Facile"):
                self.canva.itemconfig(self.boutton_avant,image=self.image_gaucheS)

        def bouton_diff_av_Unfocus(event=None):
            if(self.aff_difficulte['text']!="Facile"):
                self.canva.itemconfig(self.boutton_avant,image=self.image_gaucheN)
            

        def bouton_diff_arr(event=None):
            if(self.aff_difficulte['text']=="Normal"):
                self.aff_difficulte['text']="Difficile"
                self.aff_difficulte['image']=self.difficile
                self.canva.itemconfig(self.boutton_arr,image=self.image_droiteD)
    
            elif(self.aff_difficulte['text']=="Facile"):
                self.aff_difficulte['text']="Normal"
                self.aff_difficulte['image']=self.normal
                self.canva.itemconfig(self.boutton_avant,image=self.image_gaucheN)

        def bouton_diff_arr_S(event=None):
            if(self.aff_difficulte['text']!="Difficile"):
                self.canva.itemconfig(self.boutton_arr,image=self.image_droiteS)

        def bouton_diff_arr_Unfocus(event=None):
            if(self.aff_difficulte['text']!="Difficile"):
                self.canva.itemconfig(self.boutton_arr,image=self.image_droiteN)




        ### BOUTONS DE SELECTION DE NIVEAUX ###

        #Importation des images et créations de la grille de boutons de niveaux : 

        B1= Image.open(r"assets/icon niveaux/B1.png")
        self.BP1= ImageTk.PhotoImage(B1.resize((38,38)), Image.ANTIALIAS)
        niveau_un=tk.Button(self.master,image=self.BP1, borderwidth=0,command= lambda: self.load_niveau(1))
        self.canva.create_window(345,330,window=niveau_un,anchor="center")

        B2= Image.open(r"assets/icon niveaux/B2.png")
        self.BP2= ImageTk.PhotoImage(B2.resize((38,38)), Image.ANTIALIAS)
        niveau_deux=tk.Button(self.master,image=self.BP2, borderwidth=0,command= lambda: self.load_niveau(2))
        self.canva.create_window(395,330,window=niveau_deux,anchor="center")

        B3= Image.open(r"assets/icon niveaux/B3.png")
        self.BP3= ImageTk.PhotoImage(B3.resize((38,38)), Image.ANTIALIAS)
        niveau_trois=tk.Button(self.master,image=self.BP3, borderwidth=0,command= lambda: self.load_niveau(3))
        self.canva.create_window(445,330,window=niveau_trois,anchor="center")

        B4= Image.open(r"assets/icon niveaux/B4.png")
        self.BP4= ImageTk.PhotoImage(B4.resize((38,38)), Image.ANTIALIAS)
        niveau_quatre=tk.Button(self.master,image=self.BP4, borderwidth=0,command= lambda: self.load_niveau(4))
        self.canva.create_window(345,400,window=niveau_quatre,anchor="center")

        B5= Image.open(r"assets/icon niveaux/B5.png")
        self.BP5= ImageTk.PhotoImage(B5.resize((38,38)), Image.ANTIALIAS)
        niveau_cinq=tk.Button(self.master,image=self.BP5, borderwidth=0,command= lambda: self.load_niveau(5))
        self.canva.create_window(395,400,window=niveau_cinq,anchor="center")

        B6= Image.open(r"assets/icon niveaux/B6.png")
        self.BP6= ImageTk.PhotoImage(B6.resize((38,38)), Image.ANTIALIAS)
        niveau_six=tk.Button(self.master,image=self.BP6, borderwidth=0,command= lambda: self.load_niveau(6))
        self.canva.create_window(445,400,window=niveau_six,anchor="center")

        B7= Image.open(r"assets/icon niveaux/B7.png")
        self.BP7= ImageTk.PhotoImage(B7.resize((38,38)), Image.ANTIALIAS)
        niveau_sept=tk.Button(self.master,image=self.BP7, borderwidth=0,command= lambda: self.load_niveau(7))
        self.canva.create_window(345,470,window=niveau_sept,anchor="center")

        B8= Image.open(r"assets/icon niveaux/B8.png")
        self.BP8= ImageTk.PhotoImage(B8.resize((38,38)), Image.ANTIALIAS)
        niveau_huit=tk.Button(self.master,image=self.BP8, borderwidth=0,command= lambda: self.load_niveau(8))
        self.canva.create_window(395,470,window=niveau_huit,anchor="center") 

        B9= Image.open(r"assets/icon niveaux/B9.png")
        self.BP9= ImageTk.PhotoImage(B9.resize((38,38)), Image.ANTIALIAS)
        niveau_neuf=tk.Button(self.master,image=self.BP9, borderwidth=0,command= lambda: self.load_niveau(9))
        self.canva.create_window(445,470,window=niveau_neuf,anchor="center")   


        #### BOUTON RETOUR AU MENU PRINCIPAL ###

        self.boutton_retour=None 
        self.image_retour=None 

        RETOUR= Image.open(r"assets/menu/RETOUR.png")
        self.image_retour= ImageTk.PhotoImage(RETOUR, Image.ANTIALIAS)
        self.boutton_retour=tk.Button(self.master, image=self.image_retour, borderwidth=0, command=self.retour_menu,activebackground="#A2CCE7",bg="#A2CCE7")


       
        self.background()

        #Creation des boutons interactifs # 

        self.canva.create_window(670,550,window=self.boutton_retour,anchor="center")

        self.canva.create_window(395,250,window=self.aff_difficulte,anchor="center")

        #Creation des boutons de flèches de difficultés avec gestion des events : 
        self.boutton_avant = self.canva.create_image(320,250,image=self.image_gaucheD,anchor="center")
        self.canva.tag_bind(self.boutton_avant,'<1>', bouton_diff_av)
        self.canva.tag_bind(self.boutton_avant,'<Motion>', bouton_diff_av_S)
        self.canva.tag_bind(self.boutton_avant,'<Leave>', bouton_diff_av_Unfocus)

        self.boutton_arr = self.canva.create_image(470,250,image=self.image_droiteN,anchor="center")
        self.canva.tag_bind(self.boutton_arr,'<1>', bouton_diff_arr)
        self.canva.tag_bind(self.boutton_arr,'<Motion>', bouton_diff_arr_S)
        self.canva.tag_bind(self.boutton_arr,'<Leave>', bouton_diff_arr_Unfocus)

        Musique.creation_bouton(self.canva)
       
        

        self.canva.pack()


    #Fonction qui charge un niveau lors de la selection avec boutons sur le menu : 
    def load_niveau(self,niveau):
        from partie import Partie 
        from vehicule import Vehicule
        from fenetre_partie import FenetrePartie 
        
        if(self.aff_difficulte['text']=="Normal"):
            level=8+niveau
        elif(self.aff_difficulte['text']=="Difficile"):
            level=17+niveau 
        else: 
            level=niveau-1

        self.canva.pack_forget()
        premierePartie=FenetrePartie(level,self.master)
        premierePartie.afficher()


    def background(self):
        lien = r"assets/menu bg/choix_diff.png"
        self.bcg = ImageTk.PhotoImage(Image.open(lien).resize((800,600),Image.ANTIALIAS))
        self.canva.create_image(0,0,image=self.bcg,anchor="nw")


    def lancer_niv(self):
        self.canva.pack()

    def retour_menu(self):
        self.canva.pack_forget()
        self=FenetreMenuPrincipale(self.master)
        self.aff_menu_principale()




if __name__ == '__main__':
    root = tk.Tk()
    app = FenetreMenuPrincipale(root)
    root.mainloop()
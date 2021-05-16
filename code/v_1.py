import tkinter as tk
import tkinter.font as font
import random
from cache import *
from os import getcwd
from time import time
from copy import deepcopy


class Partie(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.size = 600
              
        #paramètre utilisé pour la gestion des voitures=================================
        self.comp=0
        self.n=6
        #self.n2=len(6)

        self.VOITUREB=0
        self.RECT=0
        self.RECT2=0

        self.x=color().rstrip("\n")

        self.posi=[]
        self.liste_voiture=[]
        
        #paramètre utilisé pour autre===================================================
        self.compteur_coup=0
        self.x=color().rstrip("\n")
        
        self.pile_retour = []
        self.pile_avancer = []
        
        self.temps=00.00
        self.controleur_temps=False
        
        self.compteur_cacher = 0
        
        #chemin pour les infos==========================================================
        path=os.getcwd()
        path=path[:-4]
        self.pathCouleur = path+"data/couleurs.txt"
        self.pathAsset = path+"assets/"
        self.parking=tk.PhotoImage(file=self.pathAsset+"images/parking_fond.png")
        self.logo=tk.PhotoImage(file=self.pathAsset+"images/logo_rushHour.png")
        self.logoAngle=tk.PhotoImage(file=self.pathAsset+"images/logo_rushHour_corner.png")
        self.logo_niveau=tk.PhotoImage(file=self.pathAsset+"images/logo_rushHour2.png")
        self.bordureBas=tk.PhotoImage(file=self.pathAsset+"images/bas.png")
        self.bordureDroite=tk.PhotoImage(file=self.pathAsset+"images/droite.png")
        self.sortie=tk.PhotoImage(file=self.pathAsset+"images/sortie.png")
        
        self.retour=tk.PhotoImage(file=self.pathAsset+"images/retour.png")
        self.avance=tk.PhotoImage(file=self.pathAsset+"images/avancer.png")

        self.iconphoto(True,tk.PhotoImage(file=self.pathAsset+"images/icone.png"))

        #self.la_fin()
        #lancement du jeu
        self.menu()
        #self.fenetre()
        #self.choix_niveau()
        
    #le démarrage du jeu
    def menu(self):      
        #taille police
        f=font.Font(size=20)
        
        self.canvas = tk.Canvas(self,bg="black",height=self.size+100,width=self.size+300)
        self.canvas.create_image((450,250),image=self.logo)
        
        #réinitialise
        self.bouton_reinitialise = tk.Button(self, text="Réinitialiser", activebackground='sienna2', height=1, width=15, command=self.renitialiser, font=f).place(x = 330, y = 580)
        #quitte le jeu
        self.bouton_quitter = tk.Button(self, text="Quitter", activebackground='IndianRed3', height=1, width=15, command=self.quitter, font=f).place(x = 330, y = 640)
        #lance le jeu
        self.bouton_jouer = tk.Button(self, text="Jouer", activebackground='SeaGreen1', height=3, width=15, command=lambda:[ self.fenetre(), self.canvas.delete()], font=f).place(x = 330, y = 400)

        self.canvas.grid(column=0, row=0, ipadx=5, ipady=5, sticky=tk.E+tk.N)
        
        
        
    #le jeu en lui même
    def fenetre(self):
        #instanciation du niveau en cours
        self.niveau = niveau()
        self.niveau_courant = deepcopy(self.niveau)
        self.information = information_niveau()
        
        self.pile_retour.append(deepcopy(self.niveau))
        
        #création de l'espace de jeu et positionnement des boutons
        self.canv = tk.Canvas(self,bg="black",height=self.size+100,width=self.size+300)
              
        self.canv.create_image((self.size/2,self.size/2),image=self.parking)
        self.canv.create_image((self.size/2,600+5),image=self.bordureBas)#en bas
        self.canv.create_image((600+5,self.size/2),image=self.bordureDroite)#droite
        self.canv.create_image((755,87.5),image=self.logoAngle)
        self.canv.create_image((607,250), image=self.sortie)#sortie
        
        #taille police
        f=font.Font(size=15)
        if self.information[4]!="21":
            self.canv.create_rectangle(605,605,930,720,fill=self.information[2])
            self.message = tk.Button(self, text="NIVEAU " + self.information[4] + " : " + self.information[3] + "\nMeilleur score possible :  "+self.information[0]+"\n\nScore du joueur : "+self.information[1], justify=tk.LEFT, bd = 0, font=8, bg = self.information[2], activebackground = self.information[2], highlightthickness = 0,command= self.cache, fg = "black").place(x = 610, y = 606) #on appelle ça une arnaque :)
            self.canv.create_rectangle(295,625,490,690,fill=self.information[2])
            
            
            
        else:
            self.canv.create_rectangle(605,605,930,720,fill="cornflowerblue")
            self.message = tk.Button(self, text="NIVEAU -ALÉATOIRE-" + "\nMeilleur score possible : XXXXX"+"\n\n Temps écoulé : "+str(self.temps), justify=tk.LEFT, bd = 0, font=8, bg = "cornflowerblue", activebackground = "cornflowerblue", highlightthickness = 0, fg = "black").place(x = 610, y = 606)
            self.canv.create_rectangle(295,625,490,690,fill="cornflowerblue")
            self.controleur_temps=True
            
            
        if self.atteindre_la_fin():
            
            #les boutons
            self.bouton_retour_menu = tk.Button(self, text="Quitter", activebackground='IndianRed3', height=3, width=15, command=self.retour_menu, font=f).place(x = 660, y = 178)
            
            self.bouton_niveau = tk.Button(self, text="Choix du niveau", activebackground='green', height=3, width=15, command=self.choix_niveau, font=f).place(x=660, y = 286)
            
            self.bouton_retour_menu = tk.Button(self, text="Aléatoire", activebackground='cornflowerblue', height=3, width=15, command=self.fenetre, font=f).place(x = 660, y = 392)
            
            self.bouton_recommencer = tk.Button(self, text="Recommencer", activebackground='steelblue', height=3, width=15, command=self.recommencer, font=f).place(x=660, y = 500)
        else:
            
            #les boutons
            self.bouton_retour_menu = tk.Button(self, text="Quitter", activebackground='IndianRed3', height=3, width=15, command=self.retour_menu, font=f).place(x = 660, y = 200)
            
            self.bouton_niveau = tk.Button(self, text="Choix du niveau", activebackground='green', height=3, width=15, command=self.choix_niveau, font=f).place(x=660, y = 350)
            
            self.bouton_recommencer = tk.Button(self, text="Recommencer", activebackground='steelblue', height=3, width=15, command=self.recommencer, font=f).place(x=660, y = 500)
            
            
            #self.timer()
           
            
        self.canv.create_text(380,643,text="Nombre de coups :",fill='black',font="Arial 14 roman")
        self.nombre_coup = self.canv.create_text(388,668,text=str(self.compteur_coup),fill=self.x,font="Arial 26 roman bold")
        
        self.canv.grid(column=0, row=0, ipadx=5, ipady=5, sticky=tk.E+tk.N)

        
        #retourImage=self.retour.subsample(1,1) #aucune idée de à quo ça sert
        self.bouton_retour = tk.Button(self, height=50, width=80, image=self.retour, command=self.arriere, font=f).place(x=200, y = 630)
        
        #avanceImage=self.avance.subsample(1,1)
        self.bouton_avancer = tk.Button(self, height=50, width=80, image=self.avance, command=self.avant, font=f).place(x=500, y = 630)
        
        self.bouton_solveur = tk.Button(self, text="Solveur", activebackground='goldenrod2', height=2, width=10, command=self.solveur, font=5).place(x=10, y = 627)
        #############################################################################################
        
        if self.information[4] == "1":
            self.tutoriel()
        
        self.affichage(self.niveau)
        self.canv.bind("<Button-1>",self.clic)
    '''    
    def timer(self):
        while self.controleur_temps:
            self.temps = time()
            self.canv.delete(self.message)
            self.message = self.message = tk.Button(self, text="NIVEAU 21 : ALÉATOIRE" + "\nMeilleur score possible : XXXXX"+"\n\n Temps écoulés : "+str(self.temps), justify=tk.LEFT, bd = 0, font=8, bg = "cornflowerblue", activebackground = "cornflowerblue", highlightthickness = 0, fg = "black").place(x = 610, y = 608)
     
    def change_temps(self):
         
         self.controleur_temps = not self.controleur_temps
    '''
    def atteindre_la_fin(self):
        return fin_atteinte()
    
    
    
    #s'enfuir de l'appli
    def quitter(self):
        self.quit()
    #retour menu
    def retour_menu(self):
        self.menu()

    #lance une partie //mettre le niveau courant en paramètre ?
    def jouer(self):
        self.fenetre()
    
    #relance le niveau
    def recommencer(self):
        self.x=color().rstrip("\n")
        self.affichage(self.niveau_courant)
        self.niveau=deepcopy(self.niveau_courant)
        self.compteur_coup=0
        self.temps=0.0
        self.update_nb_coup()
        
        self.pile_avancer = []
        self.pile_retour = [deepcopy(self.niveau_courant)]
        
        #print("recommencer")

    def avant(self):
        if len(self.pile_avancer) > 0 :
            self.pile_retour.append(deepcopy(self.niveau))
            self.niveau=deepcopy(self.pile_avancer[-1])
            self.pile_avancer=deepcopy(self.pile_avancer[:-1])
            self.affichage(self.niveau)
            
            self.compteur_coup+=1
            self.update_nb_coup()
    
    def arriere(self):
        if len(self.pile_retour) > 1 :
            self.pile_avancer.append(deepcopy(self.niveau))
            self.niveau=deepcopy(self.pile_retour[-1])
            self.pile_retour=deepcopy(self.pile_retour[:-1])
            self.affichage(self.niveau)
            
            self.compteur_coup+=1
            self.update_nb_coup()
    
    def solveur(self):
        popup = tk.Toplevel()
        popup.resizable(False,False)
        f=font.Font(size=15)
        centre = 150
        popup.geometry("+%d+%d" % (centre,centre))
        popup.title('Solveur')
        don = tk.PhotoImage(file=self.pathAsset+"images/don.png")
        canvas=tk.Canvas(popup,width=650, height=350, bg = "black")
        canvas.grid(column=0, row=0, ipadx=0, ipady=0, sticky=tk.E+tk.N)
        canvas.create_image(325,150,image=don)
        canvas.create_text(325,30,text="Participe toi aussi au développement du jeu :", justify = tk.CENTER, fill='white', font="Arial 20 roman bold")
        tk.Button(popup, text="Payer pour activer le solveur", activebackground='IndianRed3', height=2, width=25, command=popup.destroy, font=f).place(x = 170, y = 270)
        self.wait_window(popup)
    
    #remet la progression à zéro
    def renitialiser(self):
        popup = tk.Toplevel()
        popup.resizable(False,False)
        f=font.Font(size=15)
        centre = 150
        popup.geometry("+%d+%d" % (centre,centre))
        popup.title('Réinitialisation')
        
        popup.bouton_raviser = tk.Button(popup, text="Je me ravise",activebackground='SpringGreen3',height=3,width=15,command=popup.destroy,font=f).pack(side=tk.BOTTOM,padx=10, pady=10)
        
        popup.bouton_valide = tk.Button(popup, text="Je remet le jeu à zéro", activebackground='firebrick1', height=5, width=30, command=lambda:[popup.destroy(),reinitialise()], font=f).pack(side=tk.TOP,padx=10, pady=10)
        
        #fonction de freeze qui marche pas       
        self.wait_window(popup)
              
            
    #changer le pointeur du fichier data + relance fenetre
    def change_niveau(self,numero):
        change_niveau(numero)
        self.fenetre()
        
    #reglage des niveaux
    def choix_niveau(self):
        popup = tk.Toplevel()
        popup.resizable(False,False)
        f=font.Font(size=15)
        centre = 150
        popup.geometry("+%d+%d" % (centre,centre))
        popup.title('Choix du niveau')
        
        canvas=tk.Canvas(popup,width=600, height=600)
              
        canvas.grid(column=0, row=0, ipadx=5, ipady=5, sticky=tk.E+tk.N)
        
        popup.bouton_quitter = tk.Button(popup, text="Retour",activebackground='LightSalmon2',height=3,width=15,command=popup.destroy,font=f).place(x = 210, y =520)
        '''
        pos_x = [10, 160, 310, 460]
        pos_y = [10, 110, 210, 310, 410]
        val = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        for i in range(20):
            information = information_niveau_precis(i+1)
            ligne = lecture_ligne(i)
            if ligne[0]=="F":
                tk.Button(popup, text="Niveau : "+str(i+1), bg = "darkgoldenrod", activebackground=information[2], height = 2, width=10, command=lambda:[popup.destroy(),  change_niveau(val[i]), print("Niveau ", val[i]), self.fenetre()], font=f).place(x =  pos_x[i%4], y= pos_y[i//4])
            else:
                tk.Button(popup, text="Niveau : "+str(i+1), bg = "black", activebackground="black", height = 2, width=10, font=f).place(x= pos_x[i%4], y= pos_y[i//4])
        '''
        information = information_niveau_precis(1)
        ligne = lecture_ligne(1)

        if ligne[0]=="F":
            tk.Button(popup, text="Niveau : "+str(1), bg = "darkgoldenrod", activebackground=information[2], height = 2, width=10, command=lambda:[popup.destroy(),  change_niveau(1), self.fenetre()], font=f).place(x =  10, y= 10)
        else:
            tk.Button(popup, text="Niveau : "+str(1), bg = "black", activebackground="black", height = 2, width=10, font=f).place(x= 10, y= 10)
            
        information = information_niveau_precis(2)
        ligne = lecture_ligne(2)

        if ligne[0]=="F":
            tk.Button(popup, text="Niveau : "+str(2), bg = "darkgoldenrod", activebackground=information[2], height = 2, width=10, command=lambda:[popup.destroy(),  change_niveau(2), self.fenetre()], font=f).place(x =  160, y= 10)
        else:
            tk.Button(popup, text="Niveau : "+str(2), bg = "black", activebackground="black", height = 2, width=10, font=f).place(x= 160, y= 10)
            
        information = information_niveau_precis(3)
        ligne = lecture_ligne(3)

        if ligne[0]=="F":
            tk.Button(popup, text="Niveau : "+str(3), bg = "darkgoldenrod", activebackground=information[2], height = 2, width=10, command=lambda:[popup.destroy(),  change_niveau(3), self.fenetre()], font=f).place(x =  310, y= 10)
        else:
            tk.Button(popup, text="Niveau : "+str(3), bg = "black", activebackground="black", height = 2, width=10, font=f).place(x= 310, y= 10)

        information = information_niveau_precis(4)
        ligne = lecture_ligne(4)

        if ligne[0]=="F":
            tk.Button(popup, text="Niveau : "+str(4), bg = "darkgoldenrod", activebackground=information[2], height = 2, width=10, command=lambda:[popup.destroy(),  change_niveau(4), self.fenetre()], font=f).place(x =  460, y= 10)
        else:
            tk.Button(popup, text="Niveau : "+str(4), bg = "black", activebackground="black", height = 2, width=10, font=f).place(x= 460, y= 10)

        information = information_niveau_precis(5)
        ligne = lecture_ligne(5)

        if ligne[0]=="F":
            tk.Button(popup, text="Niveau : "+str(5), bg = "darkgoldenrod", activebackground=information[2], height = 2, width=10, command=lambda:[popup.destroy(),  change_niveau(5), self.fenetre()], font=f).place(x =  10, y= 110)
        else:
            tk.Button(popup, text="Niveau : "+str(5), bg = "black", activebackground="black", height = 2, width=10, font=f).place(x= 10, y= 110)

        information = information_niveau_precis(6)
        ligne = lecture_ligne(6)

        if ligne[0]=="F":
            tk.Button(popup, text="Niveau : "+str(6), bg = "darkgoldenrod", activebackground=information[2], height = 2, width=10, command=lambda:[popup.destroy(),  change_niveau(6), self.fenetre()], font=f).place(x =  160, y= 110)
        else:
            tk.Button(popup, text="Niveau : "+str(6), bg = "black", activebackground="black", height = 2, width=10, font=f ).place(x= 160, y= 110)
          
        information = information_niveau_precis(7)
        ligne = lecture_ligne(7)

        if ligne[0]=="F":
            tk.Button(popup, text="Niveau : "+str(7), bg = "darkgoldenrod", activebackground=information[2], height = 2, width=10, command=lambda:[popup.destroy(),  change_niveau(7), self.fenetre()], font=f).place(x =  310, y= 110)
        else:
            tk.Button(popup, text="Niveau : "+str(7), bg = "black", activebackground="black", height = 2, width=10, font=f).place(x= 310, y= 110)
          
        information = information_niveau_precis(8)
        ligne = lecture_ligne(8)

        if ligne[0]=="F":
            tk.Button(popup, text="Niveau : "+str(8), bg = "darkgoldenrod", activebackground=information[2], height = 2, width=10, command=lambda:[popup.destroy(),  change_niveau(8), self.fenetre()], font=f).place(x =  460, y= 110)
        else:
            tk.Button(popup, text="Niveau : "+str(8), bg = "black", activebackground="black", height = 2, width=10, font=f).place(x= 460, y= 110)
          
        information = information_niveau_precis(9)
        ligne = lecture_ligne(9)

        if ligne[0]=="F":
            tk.Button(popup, text="Niveau : "+str(9), bg = "darkgoldenrod", activebackground=information[2], height = 2, width=10, command=lambda:[popup.destroy(),  change_niveau(9), self.fenetre()], font=f).place(x =  10, y= 210)
        else:
            tk.Button(popup, text="Niveau : "+str(9), bg = "black", activebackground="black", height = 2, width=10, font=f).place(x= 10, y= 210)
                    
        information = information_niveau_precis(10)
        ligne = lecture_ligne(10)

        if ligne[0]=="F":
            tk.Button(popup, text="Niveau : "+str(10), bg = "darkgoldenrod", activebackground=information[2], height = 2, width=10, command=lambda:[popup.destroy(),  change_niveau(10), self.fenetre()], font=f).place(x =  160, y= 210)
        else:
            tk.Button(popup, text="Niveau : "+str(10), bg = "black", activebackground="black", height = 2, width=10, font=f).place(x= 160, y= 210)
                    
        information = information_niveau_precis(11)
        ligne = lecture_ligne(11)

        if ligne[0]=="F":
            tk.Button(popup, text="Niveau : "+str(11), bg = "darkgoldenrod", activebackground=information[2], height = 2, width=10, command=lambda:[popup.destroy(),  change_niveau(11), self.fenetre()], font=f).place(x =  310, y= 210)
        else:
            tk.Button(popup, text="Niveau : "+str(11), bg = "black", activebackground="black", height = 2, width=10, font=f).place(x= 310, y= 210)
                    
        information = information_niveau_precis(12)
        ligne = lecture_ligne(12)

        if ligne[0]=="F":
            tk.Button(popup, text="Niveau : "+str(12), bg = "darkgoldenrod", activebackground=information[2], height = 2, width=10, command=lambda:[popup.destroy(),  change_niveau(12), self.fenetre()], font=f).place(x =  460, y= 210)
        else:
            tk.Button(popup, text="Niveau : "+str(12), bg = "black", activebackground="black", height = 2, width=10, font=f).place(x= 460, y= 210)
                    
        information = information_niveau_precis(13)
        ligne = lecture_ligne(13)

        if ligne[0]=="F":
            tk.Button(popup, text="Niveau : "+str(13), bg = "darkgoldenrod", activebackground=information[2], height = 2, width=10, command=lambda:[popup.destroy(),  change_niveau(13), self.fenetre()], font=f).place(x =  10, y= 310)
        else:
            tk.Button(popup, text="Niveau : "+str(13), bg = "black", activebackground="black", height = 2, width=10, font=f).place(x= 10, y= 310)
                    
        information = information_niveau_precis(14)
        ligne = lecture_ligne(14)

        if ligne[0]=="F":
            tk.Button(popup, text="Niveau : "+str(14), bg = "darkgoldenrod", activebackground=information[2], height = 2, width=10, command=lambda:[popup.destroy(),  change_niveau(14), self.fenetre()], font=f).place(x =  160 , y= 310 )
        else:
            tk.Button(popup, text="Niveau : "+str(14), bg = "black", activebackground="black", height = 2, width=10, font=f).place(x= 160 , y= 310 )
                    
        information = information_niveau_precis(15)
        ligne = lecture_ligne(15)

        if ligne[0]=="F":
            tk.Button(popup, text="Niveau : "+str(15), bg = "darkgoldenrod", activebackground=information[2], height = 2, width=10, command=lambda:[popup.destroy(),  change_niveau(15), self.fenetre()], font=f).place(x =  310 , y= 310 )
        else:
            tk.Button(popup, text="Niveau : "+str(15), bg = "black", activebackground="black", height = 2, width=10, font=f).place(x= 310 , y= 310 )
                
        information = information_niveau_precis(16)
        ligne = lecture_ligne(16)

        if ligne[0]=="F":
            tk.Button(popup, text="Niveau : "+str(16), bg = "darkgoldenrod", activebackground=information[2], height = 2, width=10, command=lambda:[popup.destroy(),  change_niveau(16), self.fenetre()], font=f).place(x =  460 , y= 310 )
        else:
            tk.Button(popup, text="Niveau : "+str(16), bg = "black", activebackground="black", height = 2, width=10, font=f).place(x= 460 , y= 310 )
            
        information = information_niveau_precis(17)
        ligne = lecture_ligne(17)

        if ligne[0]=="F":
            tk.Button(popup, text="Niveau : "+str(17), bg = "darkgoldenrod", activebackground=information[2], height = 2, width=10, command=lambda:[popup.destroy(),  change_niveau(17), self.fenetre()], font=f).place(x =  10 , y= 410 )
        else:
            tk.Button(popup, text="Niveau : "+str(17), bg = "black", activebackground="black", height = 2, width=10, font=f).place(x= 10 , y= 410 )
            
        information = information_niveau_precis(18)
        ligne = lecture_ligne(18)

        if ligne[0]=="F":
            tk.Button(popup, text="Niveau : "+str(18), bg = "darkgoldenrod", activebackground=information[2], height = 2, width=10, command=lambda:[popup.destroy(),  change_niveau(18), self.fenetre()], font=f).place(x =  160 , y= 410 )
        else:
            tk.Button(popup, text="Niveau : "+str(18), bg = "black", activebackground="black", height = 2, width=10, font=f).place(x= 160 , y= 410 )
            
        information = information_niveau_precis(19)
        ligne = lecture_ligne(19)

        if ligne[0]=="F":
            tk.Button(popup, text="Niveau : "+str(19), bg = "darkgoldenrod", activebackground=information[2], height = 2, width=10, command=lambda:[popup.destroy(),  change_niveau(19), self.fenetre()], font=f).place(x =  310 , y= 410 )
        else:
            tk.Button(popup, text="Niveau : "+str(19), bg = "black", activebackground="black", height = 2, width=10, font=f).place(x= 310 , y= 410 )
            
        information = information_niveau_precis(20)
        ligne = lecture_ligne(20)
        
        if ligne[0]=="F":
            tk.Button(popup, text="Niveau : "+str(20), bg = "darkgoldenrod", activebackground=information[2], height = 2, width=10, command=lambda:[popup.destroy(),  change_niveau(20), self.fenetre()], font=f).place(x =  460 , y= 410 )
        else:
            tk.Button(popup, text="Niveau : "+str(20), bg = "black", activebackground="black", height = 2, width=10, font=f).place(x= 460 , y= 410 )

        
        
        canvas.create_image((100,560),image=self.logo_niveau)
        canvas.create_image((500,560),image=self.logo_niveau)
        #fonction de freeze qui marche pas       
        self.wait_window(popup)        
        
        
    def tutoriel(self):
        popup = tk.Toplevel()
        popup.resizable(False,False)
        f=font.Font(size=15)
        centre = 150
        popup.geometry("+%d+%d" % (centre,centre))
        popup.title('Choix du niveau')
        tuto1 = tk.PhotoImage(file=self.pathAsset+"images/tuto1.png")
        canvas=tk.Canvas(popup,width=400, height=370, bg = "black")
        canvas.create_image(210,120, image=tuto1)
        canvas.grid(column=0, row=0, ipadx=5, ipady=5, sticky=tk.E+tk.N)
        canvas.create_text(200,265,text="BUT DU JEU :\nfaire sortir la voiture noire du parking.", fill='white', font="Arial 12 roman bold", justify = tk.CENTER)
        popup.bouton_suivre = tk.Button(popup, text="J'ai compris", activebackground='mintcream', height=2, width=12, command=lambda:[popup.destroy(), self.tutoriel2()], font=f).place(x = 240, y =300)
        tk.Button(popup, text="Passe moi ça",activebackground='lavender',height=2,width=12,command=popup.destroy,font=f).place(x = 10, y =300)
        self.wait_window(popup)
    
    def tutoriel2(self):
        popup = tk.Toplevel()
        popup.resizable(False,False)
        f=font.Font(size=15)
        centre = 150
        popup.geometry("+%d+%d" % (centre,centre))
        popup.title('Choix du niveau')
        tuto2 = tk.PhotoImage(file=self.pathAsset+"images/tuto2.png")
        canvas=tk.Canvas(popup,width=400, height=370, bg = "black")
        canvas.create_image(210,120, image=tuto2)
        canvas.grid(column=0, row=0, ipadx=5, ipady=5, sticky=tk.E+tk.N)
        canvas.create_text(200,265,text="Clique sur une extrémité des véhicules pour\nles déplacer en avant/arrière.",fill='white',font="Arial 12 roman bold", justify=tk.CENTER)
        popup.bouton_suivre = tk.Button(popup, text="Ok", activebackground='mintcream', height=2, width=12, command=lambda:[popup.destroy(), self.tutoriel3()], font=f).place(x = 240, y =300)
        tk.Button(popup, text="Je veux jouer",activebackground='lavender',height=2,width=12,command=popup.destroy,font=f).place(x = 10, y =300)
        self.wait_window(popup)
        
    def tutoriel3(self):
        popup = tk.Toplevel()
        popup.resizable(False,False)
        f=font.Font(size=15)
        centre = 150
        popup.geometry("+%d+%d" % (centre,centre))
        popup.title('Choix du niveau')
        
        canvas=tk.Canvas(popup,width=400, height=370, bg = "black")
        tuto3 = tk.PhotoImage(file=self.pathAsset+"images/tuto3.png")
        canvas.create_image(210,120, image=tuto3)
        canvas.grid(column=0, row=0, ipadx=5, ipady=5, sticky=tk.E+tk.N)
        canvas.create_text(200,265,text="Tu peux activer l'aide à tous moments. \nN'hésite pas à l'utiliser :) !", justify = tk.CENTER, fill='white', font="Arial 12 roman bold")
        tk.Button(popup, text="C'est parti !",activebackground='mintcream',height=2,width=12,command=popup.destroy,font=f).place(x = 120, y =300)
        self.wait_window(popup)
        
    def affichage(self,matrice) :
        def effacer(N):
            for i in N:
                self.canv.delete(i) 
        
        AUTRE=100
        L={}
        effacer(self.liste_voiture)
        for i in range(self.n):
            for j in range(self.n):
                if matrice[i][j]!=0:
                    if matrice[i][j]==1:
                        VOITUREB=self.canv.create_rectangle(j*AUTRE,i*AUTRE,j*AUTRE+AUTRE,i*AUTRE+AUTRE,fill="black")
                        self.liste_voiture.append(VOITUREB)
                    else:
                        XY=position(matrice,matrice[i][j])
                        try:
                            L[matrice[i][j]]==1
                        except:
                            L[matrice[i][j]]=1
                            
                            '''ancien cassé
                            RECT=self.canv.create_rectangle(AUTRE*XY[0][0], AUTRE*XY[0][1], AUTRE*((XY[-1][0])+1), AUTRE*((XY[-1][1])+1),fill=self.x)
                            RECT2=self.canv.create_rectangle(AUTRE*XY[0][0], AUTRE*XY[0][1], AUTRE*((XY[-1][0])+1), AUTRE*((XY[-1][1])+1)) #contour noir
                            '''
                            RECT=self.canv.create_rectangle(AUTRE*XY[0][1], AUTRE*XY[0][0], AUTRE*((XY[-1][1])+1),AUTRE*((XY[-1][0])+1),fill=self.x)
                            RECT2=self.canv.create_rectangle(AUTRE*XY[0][1], AUTRE*XY[0][0], AUTRE*((XY[-1][1])+1),AUTRE*((XY[-1][0])+1)) #contour noir
                            self.liste_voiture.append(RECT)
                            self.liste_voiture.append(RECT2)

    def cache(self):
        self.compteur_cacher+=1
        if self.compteur_cacher==8:
                
            popup = tk.Toplevel()
            popup.resizable(False,False)
            f=font.Font(size=15)
            centre = 150
            popup.geometry("+%d+%d" % (centre,centre))
            popup.title('Heeuu')
            chat = tk.PhotoImage(file=self.pathAsset+"images/cacher.png")
            canvas=tk.Canvas(popup,width=500, height=460, bg = "black")
            canvas.grid(column=0, row=0, ipadx=0, ipady=0, sticky=tk.E+tk.N)
            canvas.create_image(240,200,image=chat)
            
            tk.Button(popup, text="Ho Ho Ho", activebackground='IndianRed3', height=2, width=15, command=popup.destroy, font=f).place(x = 150, y = 400)
            
            self.compteur_cacher=0
            
            self.wait_window(popup)
            
            
        
    
    def update_nb_coup(self):
        self.canv.delete(self.nombre_coup)
        self.nombre_coup = self.canv.create_text(388,668,text=str(self.compteur_coup),fill=self.x,font="Arial 26 roman bold")
        self.canv.grid(column=0, row=0, ipadx=5, ipady=5, sticky=tk.E+tk.N)

    def clic(self,event):
        a=(event.x,event.y)
        
        #gestion retour avancer
        self.pile_retour.append(deepcopy(self.niveau))
        self.pile_avancer = []
        
        self.niveau=deplacement(self.niveau,[int(a[1])//100,int(a[0])//100])
        
        #permet d'éviter les problèmes de spam-cliques
        if self.niveau!=self.pile_retour[-1]:
            self.compteur_coup+=1
            self.update_nb_coup()
        else:
            self.pile_retour=deepcopy(self.pile_retour[:-1])
        
        self.affichage(self.niveau)
        enregistreur(self.niveau)
        a=victoire(self.niveau)
        
        
        if "vic"==a:
            #mettre un POPUP avec les expliquations et faire apparaitre un bouton "aléatoire"
            self.la_fin()
            ecrire_fin()
        if a:
            #print("validation victoire")
            self.victory()
            
    
    def victory(self):
        #print("victoire en cours")
        self.panneau_victoire = self.canv.create_rectangle(0,0,600,600,fill='green3')
        self.text_victoire = self.canv.create_text(300,300,text="VICTOIRE !",fill='white',font="Arial 50 roman")
        
        self.text_victoire = self.canv.create_text(300,450,text=" cliquer pour continuer...",fill='white',font="Arial 28 roman")
        
        enregistre_score(self.information[4],self.compteur_coup)
        self.compteur_coup=0
        self.pile_retour=[]
        self.pile_avancer=[]
        
        self.canv.bind("<Button-1>",self.clic_victoire)
        
    def clic_victoire(self,event):
        #print("clic de victoire")
        self.canv.delete(self.panneau_victoire)
        self.canv.delete(self.text_victoire)
        self.fenetre()
        
    def la_fin(self):
        popup = tk.Toplevel()
        popup.resizable(False,False)
        f=font.Font(size=15)
        centre = 150
        popup.geometry("+%d+%d" % (centre,centre))
        popup.title('Bien joué !')
        
        canvas=tk.Canvas(popup,width=820, height=620, bg = "black")
        fin = tk.PhotoImage(file=self.pathAsset+"images/la_fin.png")
        canvas.create_image(410,230, image=fin)
        canvas.grid(column=0, row=0, ipadx=0, ipady=0, sticky=tk.E+tk.N)
        canvas.create_text(410,500,text="Désormais les niveaux sont piochés aléatoirement\nBonne chance.", justify = tk.CENTER, fill='white', font="Arial 25 roman bold")
        tk.Button(popup, text="Goooo !!",activebackground='aquamarine',height=2,width=12,command=popup.destroy,font=f).place(x = 335, y =545)
        self.wait_window(popup)
    
    
    
if __name__ == "__main__":
    app = Partie()
    app.title("Rush Hour")
    app.resizable(False,False)
    
    app.mainloop()
    

    

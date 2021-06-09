from pygame import mixer
from PIL import Image, ImageTk
import tkinter as tk

 
class Musique:
    '''3 sons en variables statiques qui seront les mêmes pour toutes les fenetres'''
    etat_musique=0
    musique=None
    bouton=None
    victoire=None
    #Pour les fenetres
    bouton_son=None
    canvas=None

    #Importation des images du bouton de gestion du son : 

    son_n_u = Image.open(r"assets/icon son/menu/son0.png")
    son_s_u = Image.open(r"assets/icon son/menu/son0_S.png")
    son_n_p = Image.open(r"assets/icon son/menu/son2.png")
    son_s_p = Image.open(r"assets/icon son/menu/son2_S.png")

   
    def __init__(self):
        #  mixer.pre_init( requence , size , channels, buffer) pour eviter du delay dans le programme 
        mixer.pre_init(44100, -16, 2, 2048)  
        mixer.init()
        Musique.musique=mixer.Sound("assets/sons/musique.wav") 
        Musique.bouton=mixer.Sound("assets/sons/son_bouton.wav") 
        Musique.victoire=mixer.Sound("assets/sons/son_victoire.wav") 
        with open("settings.txt",'r') as f:
            lignes=f.readlines()
        volume_musique=float(lignes[0].split()[1])
        volume_bouton=float(lignes[1].split()[1])
        volume_victoire=float(lignes[2].split()[1])
        Musique.musique.set_volume(volume_musique)
        Musique.bouton.set_volume(volume_bouton)
        Musique.victoire.set_volume(volume_victoire)
        Musique.musique.play(-1,0,8000)

                                    #boucle , 8 sec to fade in
 
         #Lancement de la musique au lancement du jeu: 
        

        Musique.son_normal_unpause=ImageTk.PhotoImage(Musique.son_n_u, Image.ANTIALIAS )
        Musique.son_selec_unpause=ImageTk.PhotoImage(Musique.son_s_u, Image.ANTIALIAS )

        Musique.son_normal_pause=ImageTk.PhotoImage(Musique.son_n_p, Image.ANTIALIAS )
        Musique.son_selec_pause=ImageTk.PhotoImage(Musique.son_s_p, Image.ANTIALIAS )

    #Methodes liées à la gestion des events cliquer, selection, et deselection du bouton de gestion de la musique:  
    @staticmethod
    def bouton_son(event):
        if Musique.etat_musique ==0:
            Musique.pause()
            Musique.canvas.itemconfig(Musique.boutton_son,image=Musique.son_normal_pause)
        else: 
            Musique.unpause()
            Musique.canvas.itemconfig(Musique.boutton_son,image=Musique.son_normal_unpause)
    @staticmethod
    def bouton_son_focus(event):
        if Musique.etat_musique ==0:
            Musique.canvas.itemconfig(Musique.boutton_son,image=Musique.son_selec_unpause)
        else:
            Musique.canvas.itemconfig(Musique.boutton_son,image=Musique.son_selec_pause)

    @staticmethod
    def bouton_son_unfocus(event):
        if Musique.etat_musique ==0:
            Musique.canvas.itemconfig(Musique.boutton_son,image=Musique.son_normal_unpause)
        else:
            Musique.canvas.itemconfig(Musique.boutton_son,image=Musique.son_normal_pause)

    #Creation du bouton son interactif pour les fenêtres de menu :
    @staticmethod
    def creation_bouton(canvas):
        Musique.canvas=canvas
        if Musique.etat_musique==0:
            Musique.boutton_son = Musique.canvas.create_image(760,30,image=Musique.son_normal_unpause,anchor="center")
        else :
            Musique.boutton_son = Musique.canvas.create_image(760,30,image=Musique.son_normal_pause,anchor="center")

        canvas.tag_bind(Musique.boutton_son,'<1>',  Musique.bouton_son)
        canvas.tag_bind(Musique.boutton_son,'<Motion>', Musique.bouton_son_focus)
        canvas.tag_bind(Musique.boutton_son,'<Leave>', Musique.bouton_son_unfocus)





    @staticmethod
    def pause():
        mixer.pause()
        Musique.etat_musique=2

    @staticmethod
    def unpause():
        mixer.unpause()
        Musique.etat_musique=0

    @staticmethod
    def playBruitage():
         Musique.bouton.play(0)
        

    @staticmethod
    def playVictoire():
        Musique.victoire.play(0)
        
    @staticmethod
    def stop():
        mixer.quit()




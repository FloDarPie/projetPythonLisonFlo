import tkinter as tk
import tkinter.font as font

from moteur import Moteur

class Affichage:
    def __init__(self,root=None):

        
        self.root = root

        self.root.attributes('-fullscreen',True)
        self.root.bind("<Escape>",self.confirmer_quit())
        self.root.title("Flood It")
        #self.root.background("black")
        
        
        self.canvas=tk.Canvas(root,width=800,height=800,borderwidth=0,bg="Yellow")
        self.cote = 800
        
        #prendre les infos de la fenêtre
        screen_width=root.winfo_screenwidth()
        screen_height=root.winfo_screenheight()        
        
        x= (screen_width/2)-(self.cote/2)
        self.root.geometry(f'{self.cote}x{self.cote}+{int(x)}+{int(x)}')
        self.root.minsize(800,800)
        
        #BOUTON QUITTER
        self.boutton_quitter=None
        self.root.protocol("WM_DELETE_WINDOW",self.quitter)

        self.boutton_quitter=tk.Button(self.canvas,borderwidth=0,bg="Red",activebackground="Blue",
            command=self.quitter,cursor="X_cursor")
 
    def confirmer_quit(self):
        print("quit")
        pass
    def quitter(self):
        self.root.destroy()

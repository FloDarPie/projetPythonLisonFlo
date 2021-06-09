import tkinter as tk
import tkinter.font as font

from moteur import Moteur

class Affichage:
    def __init__(self,root=None):

        
        self.root = root

        self.root.attributes('-fullscreen',True)
        self.root.bind("<Up>",self.confirmer_quit())
        self.root.title("Flood It")
        self.root.background("black")
        
        
        
    def confirmer_quit(self):
        print("quit")
        pass

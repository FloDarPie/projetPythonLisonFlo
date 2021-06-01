#liste des import
from random import randrange,seed
taille=4
nb_couleur=0

class Moteur(self,taille,nb_couleur):
    
    def __init__(self,taille,nb_couleur):
        self.t = taille
        self.nbc = nb_couleur
        self.matrice = []
        
    #création d'une partie
    #
    #taille du plateau
    #nombre de couleur
    #
    def creation(self):
        for i in range(self.t):
            ligne=[]
            for j in range(self.t):
                ligne.append(randrange(self.nbc))
            self.matrice.append(ligne)
        return matrice
        
    



if __name__ == '__main__':
    test = Moteur(14,6)
    print(test.creation())

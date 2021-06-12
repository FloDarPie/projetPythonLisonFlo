from moteur import Moteur


class Intell_artifi(Moteur):
    def __init__(self,matrice,position,voisins,taille,nbc):
        #tableau pour enregistrer les matrices vers la solution
        self.reponse = []
        self.matrice = matrice
        self.position = position
        self.voisins = voisins
        self.taille = taille
        self.nbc = nbc
        
        self.etat = dict()
        
        
        
        
   
if __name__=="__main__":
    
    m = Moteur()
    ia = Intell_artifi(m.matrice,m.position,m.voisins,m.taille,m.nbc)
    ia.montre()
    print("fin")
    

from moteur import Moteur

from random import seed

#seed(0)

class Intell_artifi(Moteur):
    '''
    Respecte la stratégie de comparaison des voisins pour choisir le plus approprié
    '''
    def __init__(self,matrice,position,voisins,taille,nbc):
        
        #infos du moteur
        self.matrice = matrice
        self.position = position
        self.voisins = voisins
        self.taille = taille
        self.nbc = nbc
        
        #taille max pour la bibliothèque des positions
        self.longueur = self.taille*self.taille
        
        #tableau pour enregistrer les matrices vers la solution
        self.reponse = [matrice]



class Disco(Moteur):
    '''
    Respecte la stratégie barbare du chacun son tour
    '''
    def __init__(self,matrice,position,voisins,taille,nbc):
        
        #infos du moteur
        self.matrice = matrice
        self.position = position
        self.voisins = voisins
        self.taille = taille
        self.nbc = nbc
        
        #taille max pour la bibliothèque des positions
        self.longueur = self.taille*self.taille
        
        #tableau pour enregistrer les matrices vers la solution
        self.reponse = [self.matrice[:]]
    
    def la_danse(self):
        
        i = 0
        
        self.transform(self.matrice[0])
        self.reponse.append(self.matrice[:])
        print("fifi")
        while len(self.position) != self.longueur:
            self.transform(i%self.nbc)
            self.reponse.append(self.matrice[:])
            i+=1
        print(self.reponse[-1])
     
        

        
if __name__=="__main__":
    
    m = Moteur()
    ia = Intell_artifi(m.matrice,m.position,m.voisins,m.taille,m.nbc)

    ia.montre()
    
    dsi = Disco(m.matrice,m.position,m.voisins,m.taille,m.nbc)
    print(dsi.reponse)
    dsi.la_danse()
    print("fin")
    

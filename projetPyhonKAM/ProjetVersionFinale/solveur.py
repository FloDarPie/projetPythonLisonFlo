from partie import Partie 
from vehicule import Vehicule
from heapq import heappush, heappop
from copy import deepcopy
    
 
class Solveur:
    '''Pour solver la partie on prend la matrice de la partie actuelle
    on stocke dans une file a priorité les parties differentes issues de Partie.deplacements_possibles()
    comparées par le nombre de deplacements pour y arriver et selon nombre de deplacements qui sont possibles ensuite
    la premiere partie gagnante rencontrée sera forcement une solution optimale
    On utilise un set de clé de partie pour ne pas retomber sur des configurations identiques'''
    
    def __init__(self,matrice,sortie):
        self.partie=Partie(matrice,sortie)
        self.parties_a_tester=[]
        heappush(self.parties_a_tester,deepcopy(self.partie))
        self.parties_testees=set(self.partie.get_clé())
        
        

    def solver(self):
        if self.parties_a_tester[0].estGagnee():
            return []
        while self.parties_a_tester:
            next_partie=heappop(self.parties_a_tester)
            for d in next_partie.deplacements_possibles():
                next_partie.deplacer(d)
                if next_partie.estGagnee():
                    return next_partie.pile_deplacements
                    # return next_partie.pile_deplacements[:len(next_partie.pile_deplacements)//5+1]   option reduire nb indices                                                    # car faut pas tricher
                clé= next_partie.get_clé()
                if clé not in self.parties_testees:
                    self.parties_testees.add(clé)
                    heappush(self.parties_a_tester,deepcopy(next_partie))
                next_partie.retour_arriere()
        return []


    
            





    

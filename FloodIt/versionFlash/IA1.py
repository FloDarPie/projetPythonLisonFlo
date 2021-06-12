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
        
        liste=[]
        for i in range(nbc):
            liste.append(i)
        self.inialisation_dic(liste)
        
        self.nombre_coup = 0
        
    #construction dico
    def inialisation_dic(self,liste):
        for k in liste:
            self.etat[k] = 0
            
            
    def observation(self,liste):
        matrice_memorise = self.matrice[:]
        for i in liste:
            self.transform(i)
            self.etat[i]+=len(self.voisins)
            self.matrice=matrice_memorise[:]
    
    def compare(self):
        grosse_key = [[0,0]]
        for key in self.etat:
            if self.etat[key] > grosse_key[0][1]:
                grosse_key=[[key,self.etat[key]]]
            elif self.etat[key] == grosse_key[0][1]:
                grosse_key.append([key,self.etat[key]])
        if len(grosse_key)!=1:
            self.observation(grosse_key[i][0] for i in range(len(grosse_key)))
            self.compare()
        print(grosse_key)
        
    
        

        
if __name__=="__main__":
    
    m = Moteur()
    ia = Intell_artifi(m.matrice,m.position,m.voisins,m.taille,m.nbc)
    ia.observation(i for i in range(ia.nbc))
    ia.compare()
    ia.montre()
    print("fin")
    

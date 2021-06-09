#liste des import
from random import randrange,seed

seed(0) #à supprimer

class Moteur(object):
    
    def __init__(self):
        self.taille = 5
        self.nbc = 6
        
        self.position = {0}
        self.voisins = [0]
        
        self.matrice = self.initialisation()
    
    
    
    #modificateurs
    def modif_taille(self,t):
        self.taille=t

    def modif_nombreCouleur(self,c):
        self.nbc=c
    
    
    
    #fonction de démarrage
    def initialisation(self):
        matrice=[]
        for i in range(self.taille*self.taille):
            matrice.append(randrange(0,self.nbc))
        return matrice
    
    #fonction de conversion
    def transform(self,couleur):
        self.generation()
        for i in self.position:
            self.matrice[i]= couleur
             
    #fonction d'affichage____ à supprimer
    def montre(self):
        m=self.matrice[:]
        i=0
        while m!=[]:
            print(m[0],end=" ")
            m=m[1:]
            i+=1
            if i%self.taille == 0:
                print()

    #on regarde si la cellule à encore besoin d'être mémorisé pour étudier les générations
    #on regarde si les cellules sont connus
    def controleVoisin(self,cell):
        l = self.taille*self.taille
        
        #contrôle droite
        if cell != l-1:
            a = cell+1 in self.position
        else:
            a = True
            
        #contrôle gauche
        if cell!=0:
            b = cell-1 in self.position
        else:
            b = True
        
        #contrôle bas
        if cell< l-self.taille:
            c = cell+self.taille in self.position
        else:
            c = True
            
        #contrôle haut
        if cell> self.taille-1:
            d = cell-self.taille in self.position
        else:
            d = True
            
        return a and b and c and d

    #prend une cellule, regarde ses voisins et renvoie une liste des cellules identiques
    def observe(self,cell,liste):
        try : #check droite 
            #print("check droite",matrice[cell] == matrice[cell+1] and cell+1 not in liste)
            if self.matrice[cell] == self.matrice[cell+1] and cell+1 not in liste and cell%self.taille!=self.nbc-1:
                liste.append(cell+1)
                a = self.observe(cell+1,self.matrice,liste[:])
                for k in a:
                    liste.append(k)
        except:
            pass
        
        try : #check gauche
            #print("check gauche",matrice[cell] == matrice[cell-1] and cell-1 not in liste)
            if self.matrice[cell] == self.matrice[cell-1] and cell-1 not in liste and cell%self.taille!=0:
                liste.append(cell-1)
                a = self.observe(cell-1,self.matrice,liste[:])
                for k in a:
                    liste.append(k)
        except:
            pass
        
        try : #check bas
            #print("check bas",matrice[cell] == matrice[cell+taille] and cell+taille not in liste)
            if self.matrice[cell] == self.matrice[cell+self.taille] and cell+self.taille not in liste:
                liste.append(cell+self.taille)
                a = self.observe(cell+self.taille,self.matrice,liste[:])
                for k in a:
                    liste.append(k)
        except:
            pass
        
        try : #check haut
            #print("check haut",matrice[cell] == matrice[cell-taille] and cell-taille not in liste)
            if self.matrice[cell] == self.matrice[cell-self.taille] and cell-self.taille not in liste and cell>self.taille:
                liste.append(cell-self.taille)
                #a = self.observe(cell-self.taille,self.matrice,liste[:])
                for k in a:
                    liste.append(k)
        except:
            pass

        return liste
    
    #construit la nouvelle génération
    #renvoie les nouveaux voisins et ajoute des positions
    def generation(self):
        nouveau_voisins=self.voisins[:]
        
        for cell in self.voisins:
            liste = self.observe(cell, [cell])
            if liste != [] :
                
                for nouveau in liste:
                    if nouveau not in self.voisins:
                        self.voisins.append(nouveau)

                    if nouveau not in self.position:
                        self.position.add(nouveau)
                
            #module de voisinage
            if self.controleVoisin(cell):
                nouveau_voisins=nouveau_voisins[1:]
            
        self.voisins[len(nouveau_voisins)-1:]    
    
if __name__ == '__main__':
    test = Moteur()
    
    test.transform(test.matrice[0])
    
    test.transform(2)
    test.transform(0)
    test.transform(4)
    test.transform(2)
    test.transform(4)
    print(test.position,test.voisins)
    test.montre()
    
    
    print("4 4 4 4 4 3 3 2 3 2 4 1 4 1 4 1 4 4 4 4 5 4 1 2 0 5 0 5 4 3 4 0 4 3 2 4 5 1 4 3 3 4 4 4 4 0 0 5 3 5 5 5 0 4 3 2 1 5 4 5 0 1 4 1 1 1 4 3 0 0 2 4 3 0 2 4 2 5 0 4 2 4 1 4 4 4 2 3 0 4 3 2 4 1 2 1 1 1 0 4 5 2 3 0 0 5 1 1 0 0 5 4 5 3 5 4 2 4 1 1 5 4 3 4 2 3 3 5 5 5 2 0 2 4 0 3 4 5 2 1 1 0 5 2 0 5 1 2 1 2 3 0 0 1 5 1 0 4 5 4 4 5 0 0 0 5 1 4 4 0 3 0 2 0 0 4 0 1 1 5 0 3 1 5 0 5 0 4 3 4 0 2 0 1 0 5"=="4 4 4 4 4 3 3 2 3 2 4 1 4 1 4 1 4 4 4 4 5 4 1 2 0 5 0 5 4 3 4 0 4 3 2 4 5 1 4 3 3 4 4 4 4 0 0 5 3 5 5 5 0 4 3 2 1 5 4 5 0 1 4 1 1 1 4 3 0 0 2 4 3 0 2 4 2 5 0 4 2 4 1 4 4 4 2 3 0 4 3 2 4 1 2 1 1 1 0 4 5 2 3 0 0 5 1 1 0 0 5 4 5 3 5 4 2 4 1 1 5 4 3 4 2 3 3 5 5 5 2 0 2 4 0 3 4 5 2 1 1 0 5 2 0 5 1 2 1 2 3 0 0 1 5 1 0 4 5 4 4 5 0 0 0 5 1 4 4 0 3 0 2 0 0 4 0 1 1 5 0 3 1 5 0 5 0 4 3 4 0 2 0 1 0 5")
    

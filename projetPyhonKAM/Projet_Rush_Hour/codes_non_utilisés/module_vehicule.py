

class Vehicule:
    ''' La classe Vehicule représente les objets que nous allons manipuler
    sur le plateau de taille 6x6
        Attributs :
            int id : identifiant
            int coord : représente l'arrière du véhicule qui permet de 
                        determiner les autres coordonnees dans la matrice.
            string orientation : V pour vertical et H pour horizontal
            int lg : un véhicule de longueur 2 cases ou 3 cases. '''

    #Date 04/24

    ID=2 #Attribut de classe 
    DIRECTIONS= {"Bas":(0,1), "Haut" : (0,-1),"Droite":(1,0),"Gauche":(-1,0)}
    
    def __init__(self,coord,orientation,lg,id=None):
        assert orientation=="V" or orientation=="H" , f'Orientation {orientation} incorrecte'
        assert lg==2 or lg==3 , f'Longueur véhicule {lg} incorrecte'
        if id==None: 
            if coord==(3,1):
                self.id=1
            else:
                self.id=Vehicule.ID
                Vehicule.ID+=1  # incrémentation 
        else:
            self.id=id  
        i,j=coord
        assert 0<=i+(lg-1 if orientation!="H" else 0)<=5 and 0<=j+(lg-1 if orientation=="H" else 0)<=5 , f'Coord vehicule {i,j} {orientation} {lg} incorrect'
        self.coord=coord  
        self.orientation=orientation
        self.lg=lg
        
    def num(self):
        return self.id       
        
    def coor(self):
        return self.coord
        
    def avancer(self):
        y,x=self.coord
        self.coord=(min(5-self.lg+1,y+1),x) if  self.orientation=="V" else (y,min(5-self.lg+1,x+1)) 
        
    def reculer(self):
        y,x=self.coord
        self.coord=(max(0,y-1),x) if  self.orientation=="V" else (y,max(0,x-1)) 
        
    def est_verticale(self):
        return self.orientation=="V"
        
    def longueur(self):
        return self.lg


    def __str__(self):
        answer= f"Le vehicule n°{self.id} de longueur {self.lg} ou l' arriere est "
        answer+=f"placé en {self.coord} et d'une orientation {self.orientation} "
        return answer
    
    def __eq__(self,other):
        ''' la fonction __eq__ vérifie si les deux objets sont des véhicules et ont la même id '''
        return isinstance(other,Vehicule) and self.id==other.id

        

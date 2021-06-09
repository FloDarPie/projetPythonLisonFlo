from vehicule import Vehicule 


class Deplacement:
    '''represente le mouvement de l'arriere d'un vehicule selon les coord de la tete,
    la direction et sa longueur'''
    def __init__(self,coord,direction,lg):
        self.coord=coord
        self.direction=direction
        self.lg=lg

    def __str__(self):
        return f'deplacement de {(self.coord[1],self.coord[0])} de direction : {self.direction} et de longueur {self.lg}'


class Partie:

    '''La classe Partie représente la partie jouee actuellement 
    Attributs:
        int[6][6] matrice : représente la matrice 6x6 ou seront stockés les ID des véhicules
                           l'ID = 0 représente une case vide.
        {} int : Vehicule} : représente une map  id -> Vehicule pour accéder plus facilement
                            au véhicule de la case selectionnéé

        [Deplacement] pile_deplacements represente la liste des Deplacements de la partie
        [Deplacement] pile_deplacements_retour liste de Deplacements stocké pour resoudre la partie
        String Sortie G pour gauche D pour Droite
       
       '''
              
    def __init__(self,vehicules,sortie='D'):
        ''' initialise une Partie à l'aide d'une liste de d'objets Véhicule 
            
            Le premier véhicule de la liste donc l'ID: 1 sera toujours le véhicule
            du joueur.

            Chaque Véhicule sera considéré comme orienté :
                 vers la droite si horizontal
                 vers le bas si vertical
                 car on parcourt la matrice de haut en bas et de gauche à droite '''
        
        
         
       #Cas vehicules : liste de vehicules
        if  isinstance(vehicules[0],Vehicule):
            self.vehicules = { v.id : v for v in vehicules}
            self.matrice=self.init_matrice(vehicules)
        #Cas vehicules : matrice 6x6    
        else:
            self.vehicules=self.init_vehicules(vehicules)
            self.matrice=vehicules
        self.sortie=sortie
        self.est_gagnee=self.estGagnee()
        self.pile_deplacements=[]
        self.pile_deplacements_retour=[]
        
        
       
      


    def __str__(self):
         return '\n'.join( str(self.matrice[i]) for i in range(6))
       

    def __eq__(self,other):
        '''Return true ssi ils ont la meme matrice'''
        return isinstance(other,Partie) and self.clé==other.clé

    def __lt__(self,other):
        '''comparaison de deux partie pour pouvoir les ranger dans une file a priorité pour le solveur'''
        d1= len(self.pile_deplacements)
        d2= len(other.pile_deplacements)
        c1=self.caseDeplacées()
        c2=other.caseDeplacées()

        '''Return vrai pour le plus petit nombre de cases déplacées ou si il est plus grand mais le nombre de deplacements est plus petit ou egal'''
        return  c1<c2 or c1>c2 and d1<=d2


    def init_matrice(self,vehicules):
        matrice=[ [0]*6 for _ in range(6)]
        for vehicule in self.vehicules.values():
            (y,x)=vehicule.coord # y : ligne  x : colonne
            (xD,yD)=Vehicule.DIRECTIONS["Bas" if vehicule.orientation=="V" else "Droite"]
            for i in range(vehicule.lg):
                matrice[y+i*yD][x+i*xD]=vehicule.id
        return matrice

    def init_vehicules(self,L):                                      #algorithme donnée par Kevin adapté                       
        """Entrée : une matrice correspondant à une partie Valide
        Cette matrice contient des nombres ou le caractère X pour les
        obstacles.
        Sortie : Une liste de vehicules"""
        vehicules={}
        N=6
        for y in range(N):
            for x in range(N):
                id=L[y][x]
                if id>0 and id not in vehicules:
                    k=L[y].count(id)
                    if k==1:
                        vehicules[id]=Vehicule((y,x),"V",3 if y<N-2 and id==L[y+2][x] else 2,id)
                    else :
                        vehicules[id]=Vehicule((y,x),"H",k,id)
                    
        return vehicules

        
    def recommencer(self):
        '''on retourne en arriere jusqu'a ce que la pile_deplacements soit vide.'''
        while self.pile_deplacements:
            self.retour_arriere()
        self.pile_deplacements_retour=[]
        self.est_gagnee=self.estGagnee()

    
    def estGagnee(self):
        '''retourne Vrai si le vehicule dont l'ID = 1 n'a plus d'ostacle selon la sortie'''
        (i,j)=self.vehicules[1].coord
        if self.sortie=="D":
            while (j+2<6) and self.matrice[i][j+2]==0:
                j+=1
            return j+2==6
        else:
            while (j-1>=0) and self.matrice[i][j-1]==0:
                j-=1
            return j==0
        
    
    


    def caseDeplacées(self):
        ''' retourne le nombre de case de tous les deplacements reunis'''
        return sum(d.lg for d in self.pile_deplacements)


        
    def vehiculePossibleDeplacement(self,vehicule):
        ''' retourne la liste des coordonnées l'arriere du Vehicule dans la matrice telle que 
        le Vehicule puisse se déplacer sans collision et selon son orientation (Pour FenetrePartie)'''
        (y,x)=vehicule.coord
        vehicule_possible_deplacement=[]
        if vehicule.orientation=="H":
            x_queue=x
            x_tete=x+vehicule.lg-1
            while x_queue-1 >=0 and self.matrice[y][x_queue-1]==0:   # on peut se déplacer vers une case a droite
                x_queue-=1
                vehicule_possible_deplacement.append((y,x_queue))
            while x_tete+1 <=5 and self.matrice[y][x_tete+1]==0:    # on peut se déplacer vers une case a gauche
                x_tete+=1
                vehicule_possible_deplacement.append((y,x_tete-vehicule.lg))
                
        else: # deplacement vertical 
            y_queue=y
            y_tete=y+vehicule.lg-1
            while y_queue-1 >=0 and self.matrice[y_queue-1][x]==0:  # on peut monter d'une case
                y_queue-=1
                vehicule_possible_deplacement.append((y_queue,x))
            while y_tete+1 <=5 and self.matrice[y_tete+1][x]==0:   # on peut décendre d'une case 
                y_tete+=1
                vehicule_possible_deplacement.append((y_tete-vehicule.lg,x))
        return vehicule_possible_deplacement
                
   
    #########################
    def get_clé(self):
        '''transforme la matrice de la partie en string comparer une onfiguration unique'''
        return "".join(str(self.matrice[i][j]) for i in range(6) for j in range(6))

    def updatePartie(self,vehicule,coord):
        ''' Modifie la matrice en prenant en compte les nouvelles coord de Vehicule'
        en identifiant le Déplacement a faire'''
        (y,x)=vehicule.coord
        (y_new,x_new)=coord
        if y==y_new:
            direction,lg=("Droite",x_new-x) if (x<x_new) else ("Gauche",x-x_new)
        else:
            direction,lg=("Bas",y_new-y) if (y<y_new) else ("Haut",y-y_new)
        le_deplacement=Deplacement(vehicule.coord,direction,lg)
        
        self.deplacer(le_deplacement)



    def retour_arriere(self):
        '''prend le deplacement de la pile_deplacement et le transforme en deplacement dans le sens
        contraire'''
        deplacement=self.pile_deplacements.pop()
        (y,x),direction,lg=deplacement.coord,deplacement.direction,deplacement.lg
        
        if direction=="Haut":
            d=Deplacement((y-lg,x),"Bas",lg)
        elif direction=="Bas":
            d=Deplacement((y+lg,x),"Haut",lg)
        elif direction=="Droite":
            d=Deplacement((y,x+lg),"Gauche",lg)
        else:
           d=Deplacement((y,x-lg),"Droite",lg)
        self.deplacer(d)
        self.pile_deplacements.pop() # on enleve le deplacement de self.deplacer()

    def retour_avant(self):
        deplacement=self.pile_deplacements_retour.pop()
        self.deplacer(deplacement)
        
        
           

    def deplacements_possibles(self):
        '''Renvoie la liste de tous les deplacements possibles pour la partie a l'instant t'''
        answer=[]
        for vehicule in self.vehicules.values():
            (yV,xV)=vehicule.coord
            #Vertical
            if vehicule.orientation=="V":
                lg=1
                #  cordonnée dans la matrice  et la case est vide au dessus/dessous
                while yV-lg>=0 and self.matrice[yV-lg][xV]==0:  #HAUT
                    answer.append(Deplacement((yV,xV),"Haut",lg))
                    lg+=1
                lg=1
                while yV+vehicule.lg+lg-1<6 and self.matrice[yV+vehicule.lg+lg-1][xV]==0: #BAS
                    answer.append(Deplacement((yV,xV),"Bas",lg))
                    lg+=1
            #Horizontal
            else:
                #  cordonnée dans la matrice  et la case est vide a gauche/droite
                lg=1
                while xV-lg>=0 and self.matrice[yV][xV-lg]==0:  #GAUCHE
                    answer.append(Deplacement((yV,xV),"Gauche",lg))
                    lg+=1
                lg=1
                while xV+vehicule.lg+lg-1<6 and self.matrice[yV][xV+vehicule.lg+lg-1]==0: #DROITE
                    answer.append(Deplacement((yV,xV),"Droite",lg))
                    lg+=1

        return answer

    



    def deplacer(self,deplacement):
        '''modifie la matrice et les coordonnées du vehicule impliqué du deplacement et rajoute le déplacement
        a la pile_deplacement puis on met a jour la clé ( utilisé par le solveur )'''
        (y,x)=deplacement.coord
        vehicule=self.vehicules[self.matrice[y][x]] #on récupère le véhicule que l'on veut déplacer.
        (dX,dY)=Vehicule.DIRECTIONS[deplacement.direction]
        (xD,yD)=Vehicule.DIRECTIONS["Bas" if vehicule.orientation=="V" else "Droite"]
        
        for i in range(vehicule.lg): # on clean
            self.matrice[y+i*yD][x+i*xD]=0
        for i in range(vehicule.lg): # remet le vehicule selon le deplacement
            self.matrice[y+i*yD+dY*deplacement.lg][x+i*xD+dX*deplacement.lg]=vehicule.id # on vides les cases
        vehicule.coord=(y+dY*deplacement.lg,x+dX*deplacement.lg)
        self.pile_deplacements.append(deplacement)
        
        
           





            




from partie import Partie 
from random import randint, choice
from copy import deepcopy
from solveur import Solveur
from vehicule import Vehicule 
from time import process_time


class Generateur: 

	# Difficulutés : plage de valeurs de mouvements :
	FACILE=list(range(6,12))
	NORMALE=list(range(12,19))
	DIFFICILE=list(range(19,51))
	DIRECTION=["D","G"]

	def __init__(self ):
		self.sortie=choice(Generateur.DIRECTION)
		self.coordY_VP=randint(2,3)
		self.coordX_VP=randint(1,3)
		self.vehicules=[Vehicule((self.coordY_VP, self.coordX_VP),"H",2,1)]
		self.partie=Partie(self.vehicules,self.sortie)
		Vehicule.ID=2 


	def difficultee(self,nb_moves):
		if nb_moves in Generateur.FACILE:
			return "*"
		elif nb_moves in Generateur.NORMALE:
			return "**"
		elif  nb_moves in Generateur.DIFFICILE:
			return "***"
		else:
			"Inconnu"

	def ajout_vehicule (self,vehicule):
		'''ajoute le vehicule crée par creer vehicule et met a jour partie et vehicules'''
		self.vehicules.append(vehicule)
		self.partie=Partie(self.vehicules,self.sortie)
		
			

	def creer_vehicule(self):
		'''choisit un vehicule au hasard parmis les vehiculesPossibles 
		et le creer en equilibrant le nombre de vhicule horizontal et verticals'''
		o=self.vehicules[-1].orientation
		b=o
		i=0
		while b==o and i<100:
			a,b,c=choice(self.vehiculesPossibles())
			i+=1
		return Vehicule(a,b,c)


	def creer_partie(self, nb_voit):
		'''retourne une partie resolue avec nb_voit'''
		while(len(self.vehicules)<nb_voit):
			voiture=self.creer_vehicule()
			self.ajout_vehicule(voiture)
			#si on ne peut plus ajouter de voiture avec cette configuration  on recommence
			if not self.vehiculesPossibles() and len(self.vehicules)<nb_voit:
				self=Generateur()
				
		self.partie=Partie(self.vehicules,self.sortie)
		return self.partie
		

		

	def vehiculesPossibles(self):
		'''retourne tous les vehicules possibles que l'on peut ajouter a la partie telle que la partie soit encore gagnee
		sans solveur'''
		vehicules_possibles=[]
		for i in range(6):
			for j in range(6):
				if i+1<6 and (self.partie.matrice[i][j]==0 and self.partie.matrice[i+1][j]==0 and (i!=self.coordY_VP and i+1!=self.coordY_VP)):
					vehicules_possibles.append(((i,j),"V",2))
				if i+2<6 and (self.partie.matrice[i][j]==0 and self.partie.matrice[i+1][j]==0 and self.partie.matrice[i+2][j]==0 and i!=self.coordY_VP and i+1!=self.coordY_VP and i+2!=self.coordY_VP):
					vehicules_possibles.append(((i,j),"V",3))
				if j+1<6 and (self.partie.matrice[i][j]==0 and self.partie.matrice[i][j+1]==0 and (i!=self.coordY_VP or i==self.coordY_VP and (self.sortie=="D" and j+1<self.coordX_VP or self.sortie=="G" and j>self.coordX_VP+1))):
					vehicules_possibles.append(((i,j),"H",2))
				if j+2<6 and self.partie.matrice[i][j]==0 and self.partie.matrice[i][j+1]==0 and self.partie.matrice[i][j+2]==0 and (i!=self.coordY_VP or i==self.coordY_VP and(self.sortie=="D" and j+2<self.coordX_VP or self.sortie=="G" and j>self.coordX_VP+1)):
					vehicules_possibles.append(((i,j),"H",3))
		return vehicules_possibles


		
	def melanger_partie(self,nb_moves):
		'''retourne vrai si la partie mélangée est solvable en nb_moves
		et met a jours self.partie faux sinon'''
		parties_testees=set()
		parties_a_tester=[self.partie]
		nb=0
		while parties_a_tester and nb<nb_moves:
			next_partie=parties_a_tester.pop()
			for d in next_partie.deplacements_possibles():
				next_partie.deplacer(d)
				clé=next_partie.get_clé()
				if clé not in parties_testees:
					solver=Solveur(next_partie.matrice,self.sortie)
					nb_to_solve=len(solver.solver())
					if nb_to_solve >=nb:
						if nb_to_solve==nb_moves:
							self.partie=deepcopy(next_partie)
							return True
						else:
							parties_a_tester.append(deepcopy(next_partie))
							nb=nb_to_solve
					parties_testees.add(clé)
				next_partie.retour_arriere()
		return False
	
    


if __name__ == '__main__':
	'''CREATION DE PARTIES SELON LE NOMBRE DE VOITURES ET DE DEPLACEMENTS'''
	nb=0
	les_parties=""
	init=process_time()
	while nb<1:
		flag=False
		while not(flag):
			nb_voit,nb_moves=randint(9,12),randint(9,15)
			G=Generateur()
			G.creer_partie(nb_voit)
			print(f'Test ajout :\nnb_voitures :{nb_voit} , nb_moves : {nb_moves}')
			flag =G.melanger_partie(nb_moves)
			if not flag:
				print("Echec")

			
		les_parties+=",".join(str(G.partie.matrice[i][j]) for i in range(6) for j in range(6))+f' {G.difficultee(nb_moves)} {G.sortie}\n'
		nb+=1
		print(f'Partie ajoutée avec succes ! \n{G.partie}  nb_voitures : {nb_voit} et nb_moves : {nb_moves}"')
		print(f'{nb} parties crées en {round(process_time()-init,2)} sec.')
	
	with open("assets/les_parties_a_ajouter.txt","w") as f:
		f.write(les_parties)
		
	



	


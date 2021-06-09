
#date 04/03 

class Voiture:
	num=2
	
	def __init__(self, coord : tuple, ori: str, taille : int, objectif : bool = False):
		assert len(coord)==2 and 0<=coord[0]<6 and 0<=coord[1]<6 and taille in [2,3] and ori in ["V","H"]
		if objectif :
			this.nb=1
			assert ori=="H"
		else:
			num+=1
			this.nb=num
			
		this.coord=coord
		this.taille=taille
		
	def __str__(self):
		L= [[ this.nb if (x,y)==coord else 0 for x in range(6)] for y in range(6)]
		L[x+(this.ori=="H")][y+(this.ori=="V")]=this.nb
		if this.taille>2:
			L[x+(this.ori=="H")*2][y+(this.ori=="V")*2]=this.nb
		s=""
		for x in L:
			s+=str(x)+"\n"
		return s



def to_Voiture(L:list):
	
	"""Entrée : une matrice correspondant à une partie Valide
	Cette matrice contient des nombres ou le caractère X pour les
	obstacles.
	Sortie : Une liste de Voitures"""
	
	voitures=[]
	numbers_found=[0,'X'] 
	N=len(L)
	for y in range(N):
		for x in range(len(L[y])):
			n=L[y][x]
			if n not in numbers_found:
				numbers_found.append(n)
				k=L[y].count(n)
				if k==1:
					voitures.append(Voiture((x,y),"V",3 if y<N-2 and n==L[y+2][x] else 2)
				else :
					voitures.append(Voiture((x,y),"H",k,n==1)
	return voitures
	


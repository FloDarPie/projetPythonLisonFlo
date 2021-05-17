from cache import *
from copy import deepcopy

M=[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,1,1,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]

graph = {}

visitées = [] #Matrices visitées
queue = []  #file en cours

class ArbreBinaire:
    def __init__(self, valeur):
        self.valeur = valeur
        self.enfant_gauche = None
        self.enfant_droit = None

    def insert_gauche(self, valeur):
        if self.enfant_gauche == None:
            self.enfant_gauche = ArbreBinaire(valeur)
        else:
            new_node = ArbreBinaire(valeur)
            new_node.enfant_gauche = self.enfant_gauche
            self.enfant_gauche = new_node

    def insert_droit(self, valeur):
        if self.enfant_droit == None:
            self.enfant_droit = ArbreBinaire(valeur)
        else:
            new_node = ArbreBinaire(valeur)
            new_node.enfant_droit = self.enfant_droit
            self.enfant_droit = new_node

    def get_valeur(self):
        return self.valeur

    def get_gauche(self):
        return self.enfant_gauche

    def get_droit(self):
        return self.enfant_droit

class Noeud:
    def __init__(self,data):
        self.data=data
        self.gauche=None
        self.droite=None
        self.parent=None

    def __str__(self):
        return str(self.data)

    def inserer(self,data):
        if data<self.data:
            if self.gauche is None:
                self.gauche=Noeud(data)
                self.gauche.parent=self
            else:
                self.gauche.inserer(data)
        elif data >self.data:
            if self.droite is None:
                self.droite=Noeud(data)
                self.droite.parent=self
            else:
                self.droite.inserer(data)
        
    def get(self,data):
        if data<self.data:
            if self.gauche:
                return self.gauche.get(data)
            return self


def trouver_fils(M):
    global comp
    comp=0
    L=[]
    comp+=1
    for i in range (6):
        for j in range(6):
            A=deplacement(deepcopy(M),[i,j])
            if A not in L and A!=M:
                L.append(A)
    try:
        for x in L:
            racine.insert_gauche(x)
    except:
        pass
    return L


def remplir(M):   
    while M[2][5]!=1:
        for x in trouver_fils(M):
            print("haha",M)
            return remplir(x)
    print("victoire",M)
        

def bfs(visitées, graph, père):
    visitées.append(père)
    queue.append(père)

    while queue:
        s = queue.pop(0)
        trouver_fils(s)
        #print(graph)
        for fils in graph[str(s)]:
            if fils not in visitées:
                visitées.append(fils)
                queue.append(fils)
    return s,graph

def remontée2(M,s,graph):
    chemin=[s]
    liste_clef=graph.keys()
    print(liste_clef)
    papa=[]
    del graph[str(s)]
    while s!=str(M):
        for x in liste_clef:
            liste_val=graph.get(x)
            #print(liste_val)
            if s in liste_val:
                papa.append(deepcopy(x))
                #print(papa)

        #del graph[papa]
        chemin.append(papa)
        #s=deepcopy(papa)
        s=papa
    print("fin")
    return chemin

def frofro(s,graph):
    chemin=[s]
    for cle,valeur in graph.items():
        if s in valeur:
            print("haha")
            chemin.append(cle)
    return deepcopy(cle),graph,chemin



def remontée(M,s,graph):
    while s!=M:
        s,graph=frofro(s,graph)
        return remontée(M,s,graph)
    return chemin

graph2={'[[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]': 
[[[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]],
 [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]], 
'[[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]': 
[[[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [1, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]],
 [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]], 
'[[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]':
 [[[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]],
  [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]], 
'[[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [1, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]':
 [[[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]], 
 '[[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]': 
 [[[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]]}


racine=ArbreBinaire('M')
s,graph=bfs(visitées,graph,M)
print(remontée(M,s,graph))
        


#bfs(visitées, graph, 'A')

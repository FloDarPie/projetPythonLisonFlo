from cache import *
from copy import deepcopy

M=[[0,0,0,0,0,0],[0,0,10,0,0,0],[1,1,10,0,0,0],[0,0,10,0,0,0],[2,0,0,0,0,0],[2,0,9,9,9,0]]

graph = {}

visitées = [] #Matrices visitées
queue = []  #file en cours


def trouver_fils(M,graph):
    L=[]
    for i in range (6):
        for j in range(6):
            A=deplacement(deepcopy(M),[i,j])
            if A not in L and A!=M:
                L.append(A)
    try:
        graph[str(M)]=L
    except:
        pass
    return graph


def bfs(visitées, graph, père):
    chemin =[]
    visitées.append(père)
    queue.append(père)

    while queue:
        s = queue.pop(0)
        graph = trouver_fils(s,graph)
        #print(graph)

        for fils in graph[str(s)]:
            if fils not in visitées:
                visitées.append(fils)
                queue.append(fils)
    return s,graph

def pere(s,graph):
    print(s)
    del graph[str(s)]
    
    liste_papa = graph.keys()
    for pere,liste in graph.items():
        if s in liste:
            s = pere
    return s,graph

def chemin(M,s,graph):
    remonte = []
    while s!=M :
        remonte.append(s)
        print(remonte)
        s,graph = pere(s,graph)
    return remonte

    
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





'''
def remontée(originel,final,dico):
    liste_clef = [final]

    
    
    while originel != final:
        trace = [list(k)  for (k, val) in dico.items() for i in val if str(i) == str(final)] #code emprunté
        final = trace[0]
        liste_clef.append(trace)
    return liste_clef
    
    

def remontée(M,s,graph):
    chemin=[s]
    
    del graph[str(s)]
    liste_clef=list(graph.keys())
    print(type(chemin[-1]),type(M),type(liste_clef[0]))
    while chemin[-1]!= M:

        for x in liste_clef:
            liste_val=graph.get(x)
            
            for j in liste_val: #j type list
                print(s,j)
                if s == str(j):
                    
                    s=deepcopy(x)
                    print(type(s))
                    chemin.append(s)
                    
            del graph[x]
            print("\nsortie boucle 2\n")
        liste_clef=list(graph.keys())

        print("\nsortie boucle 1\n")
    #print(chemin)
    #bidouillage parce ça marche pas bien au dessus
    while str(chemin[-1])!=str(M):
        chemin=chemin[:-1]

    return chemin
'''


s,graph=bfs(visitées,graph,M)
print(s)
print(chemin(M,s,graph))


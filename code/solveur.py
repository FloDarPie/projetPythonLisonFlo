from cache import *
from copy import deepcopy

M=[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,1,1,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]

graph = {}

visitées = [] #Matrices visitées
queue = []  #file en cours


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
        graph[str(M)]=L
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

def remontée(M,s,graph):
    chemin=[s]
    liste_clef=graph.keys()
    del graph[str(s)]
    while s!=M:
        for x in liste_clef:
            liste_val=graph.get(x)
            if s in liste_val:
                papa=deepcopy(x)
                print(papa)

        #del graph[papa]
        chemin.append(papa)
        s=deepcopy(papa)
        print(s)
    print("fin")
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


s,graph=bfs(visitées,graph,M)
print(remontée(M,s,graph))
        


#bfs(visitées, graph, 'A')

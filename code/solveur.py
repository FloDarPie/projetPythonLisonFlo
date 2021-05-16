from cache import *

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
            L.append(deplacement(M,[i,j]))
    graph['M'+str(comp)]=L
    return L

def remplir(M):   
    while M[2][5]!=1:
        print(trouver_fils(M))
        for x in trouver_fils(M):
            print("haha",M)
            return remplir(x)
    print("victoire",M)
        

def bfs(visitées, graph, père):
  visitées.append(père)
  queue.append(père)

  while queue:
    s = queue.pop(0) 
    print (s, end = " ") 

    for fils in graph[s]:
      if fils not in visitées:
        visitées.append(fils)
        queue.append(fils)

#bfs(visitées, graph, 'A')
remplir(M)

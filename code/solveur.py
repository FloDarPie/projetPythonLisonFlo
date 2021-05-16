from cache import *

M=[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,1,1,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]

graph = {}

visited = []
queue = []

comp=0
def remplir(M):
    global comp
    L=[]
    comp+=1
    for i in range (6):
        for j in range(6):
            L.append(deplacement(M,[i,j]))
    graph['M'+str(comp)]=L
    for x in L:
        return remplir(x)
        

def bfs(visited, graph, node):
  visited.append(node)
  queue.append(node)

  while queue:
    s = queue.pop(0) 
    print (s, end = " ") 

    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

# Driver Code
#bfs(visited, graph, 'A')
remplir(M)

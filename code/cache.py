import os

path=os.getcwd()

path=path[:-4]
path+="data/data.txt"


def lecteur():
    with open(path,'r') as data:
        num=int(data.readline(2),base=10)
        for i in range(num-1):
            data.readline(200)
        return data.readline(200)

matrice=[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]

def enregistreur(matrice):
    contenu=""
    with open(path,'r') as data:
        contenu=data.read()
    print(contenu)
    contenu=contenu[2000:]
    contenu+=str(matrice)
    with open(path,'w') as data:
        data.write(contenu)
    
enregistreur(matrice)

print("fin")

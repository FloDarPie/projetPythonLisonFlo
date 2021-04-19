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

matrice=[[1,1,1]]

def enregistreur(matrice):
    contenu=""
    compteur=0
    balise=1
    with open(path,'r') as data:
        contenu=data.readlines()
    num_lines = sum(1 for line in open(path))
    print(contenu)
    contenu=contenu[:num_lines-1]
    print(contenu)
    contenu+=matrice
    print(contenu)
    with open(path,'w') as data:
        while num_lines!=0:

            if num_lines==1:
                data.write(str(contenu))
            else:
                data.write(str(contenu[0]))
            contenu=contenu[1:]
            num_lines-=1
            
            
enregistreur(matrice)

print("fin")

import os

path=os.getcwd()

path=path[:-4]
path+="data/data.txt"


for ligne in open(path):
    print(ligne)

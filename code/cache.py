import os

path=os.getcwd()

path=path[:-4]
path+="data/data.txt"


def niveau():
    with open(path,'r') as data:
        num=int(data.readline(2),base=10)
        for i in range(num-1):
            data.readline(200)
        return data.readline(200)
        

print("fin")

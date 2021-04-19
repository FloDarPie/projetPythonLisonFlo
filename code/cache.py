import os

path=os.getcwd()

path=path[:-4]
path+="data/data.txt"

print("début")
print(path)
with open(path,'r') as data:
    num=data.readline(1)
    print(num)
    print("________")
    for i in range(2,37):
        try:
            a=int(num,base=i)
            print(i,a,data.read(a))
        except:
            pass

print("fin")

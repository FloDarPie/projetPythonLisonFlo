L = [
[0,2,2,0,0,0]
[0,0,0,3,3,3]
[0,0,0,0,0,4]
[0,1,0,0,0,4]
[0,1,0,5,5,0]
[0,1,0,0,0,0]]

def position(M,val):
    XY=[]
    if val != [0][0]:       
        for i in range(len(M)):
            for j in range (len(M[0])):
                if M[i][j] == val:
                    XY.append([i,j])
        return XY

canv2.grid()
canv.grid()
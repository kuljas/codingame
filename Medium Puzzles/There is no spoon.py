import sys
import math

def ispis(pozicija,matrix):
    h=len(matrix)
    w=len(matrix[0])
    (i,j)=pozicija
    dole='-1 -1'
    desno='-1 -1'
    if (j+1<w):
        for x in range(j+1,w):
            if (matrix[i][x]=="0"):
                desno=str(x)+' '+str(i)
                break
    if (i+1<h):
        for y in range(i+1,h):
            if (matrix[y][j]=="0"):
                dole=str(j)+' '+str(y)
                break
    ispisi=str(j)+' '+str(i)+' '+desno+' '+dole
    return ispisi

def provera(matrix):
    h=len(matrix)
    w=len(matrix[0])
    for i in range(h):
        for j in range(w):
            if (matrix[i][j]=="0"):
                print(ispis((i,j),matrix))
            else:
                continue

# Don't let the machines win. You are humanity's last hope...

width = int(input())  # the number of cells on the X axis
height = int(input())  # the number of cells on the Y axis
matrix=[]

for i in range(height):
    line = input()  # width characters, each either 0 or .
    matrix.append([l for l in line])
    
# Write an action using print

provera(matrix)


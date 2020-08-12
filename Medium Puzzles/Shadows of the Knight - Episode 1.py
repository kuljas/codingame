import sys
import math

def tabla(string):
    glc=gl
    dlc=dl
    if (string=="U"):
        glc=[x0,glc[1]]
        dlc=[x0,y0]
    elif(string=="UR"):
        glc=[x0,glc[1]]
        dlc=[dlc[0],y0]
    elif(string=="R"):
        glc=[x0,y0]
        dlc=[dlc[0],y0]
    elif(string=="DR"):
        glc=[x0,y0]
    elif(string=="D"):
        glc=[x0,y0]
        dlc=[x0,dlc[1]]
    elif(string=="DL"):
        glc=[glc[0],y0]
        dlc=[x0,dlc[1]]
    elif(string=="L"):
        glc=[glc[0],y0]
        dlc=[x0,y0]
    elif(string=="UL"):
        dlc=[x0,y0]
    return glc, dlc



def skok(string):
    x=x0
    y=y0
    dlc=dl
    glc=gl
    w=dlc[0]-glc[0]
    h=dlc[1]-glc[1]
    if (string[0]=="U"):
        y=y-max(1,(h+1)//2)
    if (string[0]=="D"):
        y=y+max(1,(h+1)//2)
    if (len(string)>1 and string[1]=="R"):
        x=max(0,x+max(w//2,1))
    if (len(string)>1 and string[1]=="L"):
        x=max(0,x-max(1,w//2))
    if (string=="R"):
        x=max(0,x+max(1,w//2))
    if (string=="L"):
        x=max(0,x-max(1,w//2))
    print(str(x)+" "+str(y))
    return x, y


we, he = [int(i) for i in input().split()]
n = int(input()) 
x0, y0 = [int(i) for i in input().split()]

dl=[we,he]
gl=[0,0]
# game loop
while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)
    gl,dl=tabla(bomb_dir)
    x0,y0=skok(bomb_dir)
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    



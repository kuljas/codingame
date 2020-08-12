import sys
import math

def slovo(i,l):
    if i in dictionary:
        a=dictionary[i]*l
    else:
        a=26*l
    b=a+l
    return row[a:b]
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
dictionary = {"A":0, "B":1, "C":2, "D":3, "E":4, "F":5, "G":6, "H":7, "I":8, "J":9, "K":10, "L":11, "M":12, "N":13, "O":14, "P":15, "Q":16, "R":17, "S":18, "T":19, "U":20, "V":21, "W":22, "X":23, "Y":24, "Z":25, "?":26 }


l = int(input())
h = int(input())
t = input()
for i in range(h):
    row = input()
    if len(t)>1:
        for j in range(len(t)-1):
            print(slovo(t[j].upper(),l),end="")
        print(slovo(t[j+1].upper(),l))
    else:
        print(slovo(t.upper(),l))
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def my_round(number):
    (number_dec,w) = math.modf(number)
    if (1-number_dec<0.0001):
        return w+1
    else:
        return math.floor(number)

def provera(rastojanje,trajanje,brzina):
    rastojanje=rastojanje/1000
    trajanje=trajanje/3600
    vreme=rastojanje/brzina
    if (my_round(vreme/trajanje)%2==0):
        return True
    else:
        return False

def provera_svi(lista,brzina):
    bul=True
    for (rastojanje,trajanje) in lista:
        if (provera(rastojanje,trajanje,brzina)==False):
            bul=False
            break
    return bul

def max_brzina(lista,brzina):
    i=brzina
    maks=0
    while i>0:
        if provera_svi(lista,i):
            maks=i
            break
        i-=1
    return maks




speed = int(input())
lista=[]
light_count = int(input())
for i in range(light_count):
    distance, duration = [int(j) for j in input().split()]
    lista.append((distance,duration))


# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(max_brzina(lista,speed))


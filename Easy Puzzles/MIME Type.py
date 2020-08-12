import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
dic={}
n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.
for i in range(n):
    ext, mt = input().split()
    dic.update({ext.lower() : mt})
for i in range(q):
    fname = input()  # One file name per line.
    if (fname.count('.')>=1):
        print(dic.get(fname[fname.rfind(".")+1:].lower(),"UNKNOWN"))
    else:
        print("UNKNOWN")

# For each of the Q filenames, display on a line the corresponding MIME type. If there is no corresponding type, then display UNKNOWN.



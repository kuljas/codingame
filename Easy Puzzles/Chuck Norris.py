message = input()
print(' '.join(list(map(lambda x:['00 '+'0'*len(x),'0 '+'0'*len(x)][x[0]=='1'], ''.join(format(ord(x),'b').zfill(7) for x in message).replace('10','1 0').replace('01','0 1').split()))))


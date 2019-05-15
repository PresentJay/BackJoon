line = int(input())
for i in range(1,line+1,1):
    for j in range(line-i): print(" ",end='')
    for j in range(2*i-1): print("*",end='')
    print('')
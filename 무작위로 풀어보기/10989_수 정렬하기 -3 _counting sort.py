import sys
x=[0]*10001
for i in range(int(sys.stdin.readline())):
    x[int(sys.stdin.readline())]+=1
for i in range(10001):
    if x[i]>0:
        for j in range(x[i]): print(i)
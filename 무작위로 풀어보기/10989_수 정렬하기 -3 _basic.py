import sys
x=[]
for i in range(int(sys.stdin.readline())): x.append(int(sys.stdin.readline()))
for i in range(len(x)):
    for j in range(i+1, len(x), 1):
        if x[i]>x[j]:
            x[i], x[j] = x[j], x[i]
            continue
for i in x: print(i)
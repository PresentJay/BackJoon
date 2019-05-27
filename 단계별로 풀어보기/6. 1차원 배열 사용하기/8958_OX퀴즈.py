n=int(input())
a=[]
for i in range(n): a.append(input())
for i in a:
    c=0
    for j in i.split('X'):
        if j!='': c+=int((1+len(j))*(len(j)/2))
    print(int(c))
a=1
for i in range(3): a*=int(input())
for i in range(10):
    c=0
    for j in str(a):
        if int(j)==i: c+=1
    print(c)

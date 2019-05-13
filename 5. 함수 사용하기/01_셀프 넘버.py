def d(n):
    Ans=int(n)
    for i in range(len(n)):
        Ans+=int(n[i])
    return Ans
Ans=[]
for i in range(1,10000,1):
    if d(str(i))<10000: Ans.append(d(str(i)))
else:
    for i in range(1,10000,1):
        if i not in Ans:
            print(i)
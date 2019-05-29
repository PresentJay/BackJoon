l={}
m=[0]
for i in input().upper():
    if l.get(i,-1)==-1: l[i]=1
    else: l[i]+=1
for i in l:
    if l[i]>m[0]: m=[l[i],i]
    elif l[i]==m[0]: m[1]='?'
print(m[1])
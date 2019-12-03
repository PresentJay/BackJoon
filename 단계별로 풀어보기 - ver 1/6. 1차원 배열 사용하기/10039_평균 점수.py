s=[]
sum=0
for i in range(5): s.append(int(input()))
for i in s:
    if i>40: sum+=i
    else: sum+=40
print(int(sum/5))
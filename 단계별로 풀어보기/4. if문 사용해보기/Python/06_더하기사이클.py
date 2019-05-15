n= int(input())
count=1
tn = n%10*10 + (n//10 + n%10)%10
while tn!=n:
    tn = tn%10*10 + (tn//10 + tn%10)%10
    count+=1
print(count)
def d(n):
    if n<10: return n+n
    elif n<100: return n+(n//10)+(n%10)
    elif n<1000: return n+(n//100)+(n//10%10)+(n%10)
    else: return n+(n//1000)+(n//100%10)+(n//10%10)+(n%10)
Ans=[]
for i in range(1,10000,1):
    Ans.append(d(i))
    if i not in Ans: print(i)
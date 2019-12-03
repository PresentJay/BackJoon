A=int(input())
for i in range(A,2,-1):
    if i%5==0 or i<5:
        Ans=i//5
        if (A-Ans*5)%3==0:
                Ans+=(A-Ans*5)//3
                break
else:
    Ans=-1
print(Ans)
def d(n):
    if n<100: return 1
    else:
        if (n%10-n//10%10) == (n//10%10-n//100): return 1
        else: return 0
cnt,n = 0, int(input())
for i in range(1,n+1,1): cnt+=d(i)
print(cnt)
a, b, c = map(int, input().split(" "))
A=max(a,b)
B=max(b,c)
if A>B: print(B)
elif A<B: print(A)
else:
    if a>c: print(a)
    elif c>=a: print(c)
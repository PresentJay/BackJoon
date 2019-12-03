def f(x, n):
    if x-1>0: f(x-1,n*x)
    else: print(n)
f(int(input()), 1)
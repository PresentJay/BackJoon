import sys
sys.setrecursionlimit(10000)
def level(d, s, c):
    sd, ss, sc = d[0], s[0], c[0]
    for adder in range(1,-2,-1):
        c[0]+=1
        s[0]+=adder
        d[0]-=s[0]
        if d[0]>0: c[0]=level(d,s,c)
        if d[0]==0 and s[0]==1: break
        d[0], s[0], c[0] = sd, ss, sc
    return c[0]
tc = int(input())
start, end = [0]*tc, [0]*tc
for i in range(tc): start[i], end[i] = map(int, input().split(" "))
for i in range(tc): print(level([end[i]-start[i]],[0],[0]))
def level(d, s, c):
    sd, ss, sc = d[0], s[0], c[0] #rollback을 위한 해당 레벨의 초기값 저장
    print(c,"level start : ",d,s,c)
    for adder in range(1,-2,-1):
        c[0]+=1
        s[0]+=adder
        d[0]-=s[0]
        print("\t",adder,"adder start; d will be",d,"; s will be", s)
        if d[0]>0:
            print("\tgo upper")
            c=level(d,s,c)
        print(d,s,c)
        if d[0]==0 and s[0]==1:
            print("complete in",c,"level :",d,s,c)
            break
        d[0], s[0], c[0] = sd, ss, sc
        print("\t",adder,"adder is discarded : ",d,s,c)
    else: print(c,"level is discarded : ",d,s,c)
    return c
tc = int(input())
start, end = [0]*tc, [0]*tc
for i in range(tc): start[i], end[i] = map(int, input().split(" "))
for i in range(tc): print(level([end[i]-start[i]],[0],[0]))
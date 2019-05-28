TCs=[]
for i in range(int(input())): TCs.append(input().split())
for i in TCs:
    for j in i[1]: print(j*int(i[0]),end="")
    print("")
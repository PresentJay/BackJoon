n = int(input())
scores = input().split(" ")
obj=0
for i in range(n):
    scores[i] = int(scores[i])
    obj+=scores[i]
print(format(obj/max(scores)*100/n,".2f"))
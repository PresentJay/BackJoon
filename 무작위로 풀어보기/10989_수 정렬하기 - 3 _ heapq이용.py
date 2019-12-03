import heapq
x=[]
for i in range(int(input())): heapq.heappush(x,int(input()))
while len(x)>0: print(heapq.heappop(x))
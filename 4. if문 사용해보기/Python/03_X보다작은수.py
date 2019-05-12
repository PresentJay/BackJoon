import sys
n, std = map(int, input().split(" "))
score = sys.stdin.readline().split(" ")
for i in range(n):
    if(int(score[i])<std): print(int(score[i]),end=" ")
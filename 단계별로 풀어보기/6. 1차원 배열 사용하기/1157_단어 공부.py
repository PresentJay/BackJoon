import sys
max=[0,' ']
A=sys.stdin.readline().upper()
for a in range(ord('A'),ord('Z')+1,1):
    cnt=0
    for i in A:
        if i==chr(a): cnt+=1
    if max[0]<cnt:
        max[0]=cnt
        max[1]=chr(a)
    elif max[0]==cnt: max[1]='?'
print(max[1])
n = int(input())
for i in range(n):
    scores = input().split(" ")
    s, count= 0, 0
    for j in range(1,int(scores[0])+1,1):
        s+=int(scores[j])
    for j in range(1,int(scores[0])+1,1):
        if int(scores[j])>(s/int(scores[0])):
            count+=1
    print(format(count/int(scores[0])*100,".3f")+'%')
m,d = map(int,input().split(" "))
std = 0
DAY = ['MON','TUE','WED','THU','FRI','SAT','SUN']
for i in range(1,m+1,1):
    if i!=m:
        if i==3 or i==5 or i==7 or i==8 or i==10:
            std+=31
        elif i==2:
            std+=28
        elif i==1:
            std+=30
        else:
            std+=30
    else:
        if i==1: std+=d-1
        else: std+=d
print(DAY[std%7])
flag = 3
printer = ['ascending','descending','mixed']
n= input().split()
for i in range(len(n)-1):
    if int(n[i])>int(n[i+1]):
        if flag==3: flag=1
        elif flag!=1:
            flag=2
            break
    elif int(n[i])<int(n[i+1]):
        if flag==3: flag=0
        elif flag!=0:
            flag=2
            break
print(printer[flag])
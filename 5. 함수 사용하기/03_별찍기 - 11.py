func_print = [lambda n:print(n*5, end=' '), lambda n:print('  '+n+'  ', end=' '), lambda n:print(' '+n+' '+n+' ', end=' ')]
line = int(input())
for i in range(1,line+1,1):
    for j in range(((line//3-1)-(i-1)//3)*3): print(' ', end='')
    if ((i-1)//3+1)%4==3 and (i-1)//3>=1:
        func_print[i%3]('*')
        for k in range((((i-1)//3+1)//4+1)*2-1):
            func_print[i%3](' ')
            func_print[i%3]('*')
    elif (((i-1)//3+1)%4==2 and ((i-1)//3)>2):
        func_print[i%3]('*')
        func_print[i%3]('*')
        for k in range(((i-1)//3-2)//4+1):
            func_print[i%3](' ')
            func_print[i%3](' ')
            func_print[i%3]('*')
            func_print[i%3]('*')
    elif (((i-1)//3+1)%4==1 and (i-1)//3>2):
        func_print[i%3]('*')
        for k in range(((i-1)//3-1)//4+1):
            func_print[i%3](' ')
            func_print[i%3](' ')
            func_print[i%3](' ')
            func_print[i%3]('*')
    else:
        for k in range((i-1)//3+1): func_print[i%3]('*')
    if i!=line: print("")
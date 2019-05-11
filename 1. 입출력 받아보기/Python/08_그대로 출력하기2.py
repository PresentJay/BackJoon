lines=''
for i in range(100):
    try:
        if lines=='': lines+=input()
        else: lines+='\n'+input()
    except EOFError:break
print(lines)
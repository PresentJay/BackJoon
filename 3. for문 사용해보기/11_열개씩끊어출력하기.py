word=input()
for i in range(len(word)):
    print(word[i], end="")
    if (i+1)%10==0:
        print()
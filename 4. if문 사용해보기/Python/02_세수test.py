for i in range(1,101,1):
    for j in range(1,101,1):
        for k in range(1,101,1):
            if i>=j and j>=k: mid = j
            elif j>=k and k>=i: mid = k
            elif k>=i and i>=j: mid = i
            A=max(i,j)
            B=max(j,k)
            if A>B: mid2=B
            elif A<B: mid2=A
            else:
                if i>k: mid2=i
                elif k>=i: mid2=k
            if mid!=mid2:
                print(i,j,k," => ",mid,",",mid2)
print("end")
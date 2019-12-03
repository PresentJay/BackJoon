a, b, c = map(int, input().split(" "))
mid = 0
if (a>=b and b>=c) or (c>=b and b>=a): mid = b
elif (b>=c and c>=a) or (a>=c and c>=b): mid = c
elif (c>=a and a>=b) or (b>=a and a>=c): mid = a
print(mid)
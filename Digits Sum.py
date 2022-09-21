import math
T=int(input())
for i in range(T):
    n=int(input())
    if n==1:
        print("0")
    elif n<8:
        print("0")
    elif n==9:
        print("1")
    else:
        print(math.floor(n/10))
    
##incomplete

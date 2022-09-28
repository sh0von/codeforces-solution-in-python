import math
t = int(input())
for i in range(t):
    x, y = map(int, input().split())
    ans = math.sqrt(pow(0 - x, 2) + pow(0 - y, 2))
    if x == 0 and y == 0:
        print(0)
    elif ans == int(ans):
        print(1)
    else:
        print(2)

 

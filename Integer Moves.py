import math
# taking input
t = int(input())
# looping
for i in range(t):
    # taking input
    x, y = map(int, input().split())
    # finding distance
    ans = math.sqrt(pow(0 - x, 2) + pow(0 - y, 2))
    # checking if distance is integer or not
    if x == 0 and y == 0:
        # printing 0
        print(0)
    elif ans == int(ans):
        # printing 1
        print(1)
    else:
        # printing 2
        print(2)
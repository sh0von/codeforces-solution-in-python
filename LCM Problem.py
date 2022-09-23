import sys
input = sys.stdin.readline
     
t = int(input())
for i in range(t):
    l, r = map(int,input().split())
    if r >= l*2:
        print(l, l*2)
    else:
        print(-1, -1)
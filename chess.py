t = int(input())
for i in range(t):
    n,m = map(int,input().split())
    if n==3 and m==3:
        print("2 2")
    else:
        print(n//2+1,m//2+1)

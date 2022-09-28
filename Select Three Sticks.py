def solve():
    n = int(input())
    a = [int(x) for x in input().split()]
    a.sort()
    ans = 2e9
    for i in range(2,n):
        ans = min(ans,a[i]-a[i-2])
    print(ans)
t = int(input())
for i in range(t):
    solve()

 

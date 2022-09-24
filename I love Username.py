n = int(input())
a = list(map(int, input().split()))
cnt = 0
permmax = a[0]
permmin = a[0]
for j in range(n):
    for i in range(j):
        if a[j] > permmax:
            permmax = a[j]
            cnt += 1
        if a[j] < permmin:
            permmin = a[j]
            cnt += 1
print(cnt)

 

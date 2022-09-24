T = int(input())
for _ in range(T):
    n = int(input())
    res = 0
    for i in range(1, 10):
        cur = i
        while cur <= n:
            res += 1
            cur = cur * 10 + i # 11 -> 111, 2222 -> 22222
    print(res)



 

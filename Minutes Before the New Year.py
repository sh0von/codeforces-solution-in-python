T=int(input())
for i in range(T):
    h,m=map(int, input().split()) 
    print((23-h)*60+(60-m))
T=int(input())
for i in range(T):
    n=int(input())
    arr=list(map(int, input().strip().split()))[:n]   
    if sum(arr)>n:
        print(sum(arr)-n)
    elif sum(arr)/n==1:
        print("0")
    else:
        print("1")
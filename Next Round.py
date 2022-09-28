from itertools import count


a,b=map(int, input().split())
arr=list(map(int, input().strip().split()))[:a]
c=arr[b-1]
j2 = [i for i in arr if i >= c]
if arr.count(0)==len(arr):
    print("0")
elif c==0:
    print(len(j2)-arr.count(0))
else:
    print(len(j2))
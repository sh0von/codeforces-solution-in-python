from itertools import count #importing count function from itertools module


a,b=map(int, input().split()) #taking input of a and b
arr=list(map(int, input().strip().split()))[:a] #taking input of array
c=arr[b-1] #assigning c to the value of (b-1)th element of array
j2 = [i for i in arr if i >= c] #creating a new array with elements greater than or equal to c
if arr.count(0)==len(arr): #if all elements are 0
    print("0")
elif c==0: #if c is 0
    print(len(j2)-arr.count(0)) #printing the length of j2 array after removing the number of 0s
else: #if c is not 0
    print(len(j2)) #printing the length of j2 array

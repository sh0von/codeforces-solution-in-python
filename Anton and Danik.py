n=int(input())
w=input()
x=w.count("A")
if x>(n-x):
    print("Anton")
elif x<(n-x):
    print("Danik")
else:
    print("Friendship")
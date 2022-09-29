# It takes the number of test cases as input. 
# Then it takes the two numbers as input and stores them in x and y respectively. 
# Then it checks if x is divisible by y or not. If yes, then it prints "YES" else it prints "NO". 

n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    if x % y == 0:
        print("YES")
    else:
        print("NO")

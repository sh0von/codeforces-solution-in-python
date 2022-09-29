def div(n): #function to check if the number is divisible by 2
    while n % 2 == 0: #while loop to check if the number is divisible by 2
        n = n / 2 #divide the number by 2
    return n == 1 #return true if the number is 1

def main(): #main function
    for _ in range(int(input())): #for loop to take input
        n = int(input()) #take input
        print("NO" if div(n) else "YES") #print the result

if __name__ == '__main__': #call the main function
    main()

def div(n):
    while n % 2 == 0:
        n = n / 2
    return n == 1

def main():
    for _ in range(int(input())):
        n = int(input())
        print("NO" if div(n) else "YES")

if __name__ == '__main__':
    main()
def main():
    tc = int(input())
    for _ in range(tc):
        n = int(input())
        candies = [int(a) for a in input().split()]
        mini = min(candies)
        val = n * mini
        print(sum(candies) - val)

if __name__ == "__main__":
    main()
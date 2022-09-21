def solve(k, r):

    possible_remainders = {0, r}
    i = 1

    while True:

        mod = (i*k) % 10
        if mod in possible_remainders:
            return i
        else:
            i += 1


if __name__ == "__main__":

    k, r = map(int, input().split(" "))
    print (solve(k, r))
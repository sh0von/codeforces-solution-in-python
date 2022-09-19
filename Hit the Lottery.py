t = int(input())

arr = [1, 5, 10, 20, 100]




def trav(n, count, t):
    if t == 0:
        return count

    if t <0:
        return 100000000000000

    if n<0:
        return 100000000000000

    h = min(trav(n - 1, count + t//(arr[n]), t%(arr[n])) , trav(n - 2, count + t//(arr[n]), t%(arr[n])))
    return h

print(trav(len(arr) -1, 0, t))
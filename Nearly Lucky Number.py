n = int(input())
def countLuckyDigits(num):
    s = str(num)
    count = 0

    for i in range(len(s)):
        if s[i] == '4' or s[i] == '7':
            count += 1

    return count

def isLuckyNumber(num):
    s = str(num)
    ok = True

    for i in range(len(s)):
        if s[i] != '4' and s[i] != '7':
            ok = False
            break

    return ok

if isLuckyNumber(countLuckyDigits(n)):
    print("YES")
else:
    print("NO")
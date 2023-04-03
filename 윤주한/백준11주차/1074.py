n, r, c = map(int, input().split())

ans = 0
while (2 ** n) != 1:
    if r < (2 ** n) // 2:
        if c >= (2 ** n) // 2:
            ans += ((2 ** n) // 2) ** 2
            c -= (2 ** n) // 2
    else:
        if c < (2 ** n) // 2:
            ans += 2 * (((2 ** n) // 2) ** 2)
        else:
            ans += 3 * (((2 ** n) // 2) ** 2)
            c -= (2 ** n) // 2
        r -= (2 ** n) // 2
    n -= 1
print(ans)
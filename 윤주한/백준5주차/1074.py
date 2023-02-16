import sys
input = sys.stdin.readline
n, r, c = map(int, input().split())

cnt = 0
while n != 0:
    if (2 ** n) // 2 <= r:
        # 4사분면
        if (2 ** n) // 2 <= c:
            cnt += ((2 ** (n-1)) ** 2) * 3
            r -= 2 ** (n-1)
            c -= 2 ** (n-1)
        # 3사분면
        else:
            cnt += ((2 ** (n-1)) ** 2) * 2
            r -= 2 ** (n-1)
    else:
        # 2사분면
        if (2 ** n) // 2 <= c:
            cnt += ((2 ** (n-1)) ** 2) * 1
            c -= 2 ** (n-1)
    n -= 1
print(cnt)
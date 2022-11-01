N, M, K = map(int, input().split())
ls = list(map(int, input().split()))

ls.sort(reverse=True)
first = ls[0]
second = ls[1]

cnt = (M // (K+1)) * K
cnt += M % (K+1)

ans = cnt * first
ans += (M - cnt) * second

print(ans)
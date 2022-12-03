n, m = map(int, input().split())
ls = list(map(int, input().split()))

start = 0
end = max(ls)

def howlong(s):
    w = 0
    for i in ls:
        if i > s:
            w += (i - s)
    return w

while start <= end:
    mid = (start + end) // 2
    result = howlong(mid)
    
    if result < m:
        end = mid - 1
    else:
        start = mid + 1
        ans = mid

print(ans)
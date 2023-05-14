from collections import deque

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    q = deque()
    ls = list(map(int, input().split()))
    for i in range(n):
        q.append((ls[i], i))

    cnt = 1
    
    while q:
        v, idx = q.popleft()
        if len(q) != 0 and v < max(q, key=lambda x: x[0])[0]:
            q.append((v, idx))
        else:
            if idx == m:
                print(cnt)
            cnt += 1

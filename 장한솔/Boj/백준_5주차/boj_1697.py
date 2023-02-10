import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
visited = [0] * 100001

def bfs() :
    dq = deque()
    dq.append(N)
    while dq : # deque가 비어있지 않은 경우
        i = dq.popleft()
        if i == K :
            print(visited[i])
            break
        for j in (i-1, i+1, i*2) :
            if 0 <= j <= 100000 and not visited[j] : # visited[j]가 0인경우,,,,,,
                visited[j] = visited[i] + 1
                dq.append(j)

bfs()
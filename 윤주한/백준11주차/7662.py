import heapq, sys
input = sys.stdin.readline
t = int(input())

for _ in range(t):
    k = int(input())

    q_max = []
    q_min = []
    visited = [False] * k
    for j in range(k):
        order, num = input().split()
        num = int(num)
        if order == 'I':
            heapq.heappush(q_max, (-num, j))
            heapq.heappush(q_min, (num, j))
            visited[j] = True
        else:
            if num == 1:
                while q_max and not visited[q_max[0][1]]:
                    heapq.heappop(q_max)
                if q_max:
                    visited[q_max[0][1]] = False
                    heapq.heappop(q_max)
            else:
                while q_min and not visited[q_min[0][1]]:
                    heapq.heappop(q_min)
                if q_min:
                    visited[q_min[0][1]] = False
                    heapq.heappop(q_min)
    while q_max and not visited[q_max[0][1]]:
        heapq.heappop(q_max)       
    while q_min and not visited[q_min[0][1]]:
        heapq.heappop(q_min)
    
    if q_min and q_max:
        print(-q_max[0][0], q_min[0][0])
    else:
        print('EMPTY')
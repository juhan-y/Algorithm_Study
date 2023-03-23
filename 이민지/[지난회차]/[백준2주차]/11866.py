from collections import deque

n, k = map(int, input().split())
graph = list(range(1,n+1))
queue = deque(graph)
answer = []

while queue:
    for _ in range(k-1):
        a = queue.popleft()
        queue.append(a)
    b = queue.popleft()
    answer.append(b)

print('<' + str(answer[0]), end='')
for i in answer[1:]:
    print(', ' + str(i), end='')
print('>')

N, M = map(int, input().split())

answer = []

for i in range(N):
    li = list(map(int, input().split()))
    answer.append(min(li))
    
print(max(answer))
    

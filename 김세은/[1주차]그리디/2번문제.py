N, M, K = map(int, input().split())
li = list(map(int, input().split()))

li.sort()
answer = 0
count = 0

while True:
    for i in range(K):
        if count==M:
            break
        answer += li[-1]
        count += 1
        
    if count==M:
        break
    
    answer+=li[-2]
    count += 1

print(answer)

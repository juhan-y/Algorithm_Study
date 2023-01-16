# 1978 소수 찾기
N = int(input())

li = list(map(int, input().split()))

ans = []
    
for i in li:
    result = True
    for j in range(2, int(i**0.5)+1):
        if i%j == 0:
            result = False
            break
    if result:
        if i==1:
            continue
        ans.append(i)

print(len(ans))

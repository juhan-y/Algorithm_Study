n = int(input())

def find(num, target):
    pred = num
    while num > 0:
        pred += num % 10
        num //= 10
    
    if pred == target:
        return True
    else:
        return False

ans = []
for i in range(1, n+1):
    if find(i, n):
        ans.append(i)

if ans:
    print(min(ans))
else:
    print(0)
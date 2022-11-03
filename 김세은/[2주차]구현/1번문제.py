# 예제 4-1
N = int(input())
a = input().split()
x, y = 1,1

for i in a:
    if i=='L':
        if y > 1:
            y -= 1
    elif i=='R':
        if y < N:
            y += 1
    elif i=='U':
        if x > 1:
            x -= 1
    elif i=='D':
        if x < N:
            x += 1
print(x, y)

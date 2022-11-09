n = int(input())
plans = input().split()
x, y = 1, 1

for p in plans:
    if p == 'L':
        if y > 1:
            y -= 1
    elif p == 'R':
        if y < n:
            y += 1
    elif p == 'U':
        if x > 1:
            x -= 1
    elif p == 'D':
        if x < n:
            x += 1
            
print(x, y)
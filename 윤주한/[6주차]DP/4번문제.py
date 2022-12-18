d = [0] * 101

for i in range(1, 101):
    if i == 1 or i == 2:
        d[i] = 1
    else:
        d[i] = d[i-1] + d[i-2]

print(d[99], d[100])
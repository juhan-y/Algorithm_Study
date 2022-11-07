n = int(input())
pre_count = 10 * 6 * 10 + 5 * 6 * 10 + 5 * 9 * 10 + 5 * 9 * 5

cnt = 0
for i in range(n+1):
    if i == 3 or i == 13 or i == 23:
       cnt += 60 * 60
    else:
        cnt += pre_count

print(cnt)
#11번문제
n = int(input())
li = []

for i in range(n):
    a = input().split()
    li.append((a[0], int(a[1])))

li.sort(key=lambda i:i[1])
# li = sorted(li, key=lambda i:i[1])

for i in li:
    print(i[0], end=' ')

n = int(input())
ls = []
for _ in range(n):
    a, b = input().split()
    ls.append((a,int(b)))

ls.sort(key=lambda x: x[1])
for i in ls:
    print(i[0], end=' ')
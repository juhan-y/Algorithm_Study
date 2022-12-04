n = int(input())
ls = []

for _ in range(n):
    ls.append(int(input()))
    
ls.sort(reverse=True)

for i in ls:
    print(i, end=' ')
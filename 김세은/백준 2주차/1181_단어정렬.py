# 1181 단어 정렬
N = int(input())

li = []
for i in range(N):
    a = input()
    li.append(a)

li = list(set(li))
li.sort()
li.sort(key=lambda x: len(x))

for i in li:
    print(i)

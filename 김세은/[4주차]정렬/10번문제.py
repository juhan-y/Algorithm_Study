#10번문제
n = int(input())
li=[]

for i in range(n):
    a = int(input())
    li.append(a)
li.sort(reverse=True)

for i in li:
    print(i, end=' ')

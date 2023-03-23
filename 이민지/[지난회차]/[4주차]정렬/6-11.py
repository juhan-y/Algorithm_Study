n = int(input())
ls = []
for i in range(n):
    a, b = input().split() 
    ls.append([b,a]) # [성적, 이름]으로 추가
ls.sort()
for i,j in ls:
    print(j, end=' ')
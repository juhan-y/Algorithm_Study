t = int(input())
for _ in range(t):
    h, w, n = map(int, input().split())
    if n%h == 0:
        num = h*100+(n//h)
    else:
        num = (n%h)*100+(n//h)+1 # n%h는 층수, (n//h)+1은 번호
    print(num)
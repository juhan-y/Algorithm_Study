def cnt(x, y ,n):
    global white
    global blue
    color = arr[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != arr[i][j]:
                n = int(n/2)
                cnt(x, y, n)
                cnt(x, y+n, n)
                cnt(x+n, y, n)
                cnt(x+n, y+n, n)
                return 
    if color == str(0):
        white += 1
    if color == str(1):
        blue += 1

n = int(input())
arr = []
white = 0
blue = 0
for _ in range(n):
    arr.append(input().split())
cnt(0,0,n)
print(white)
print(blue)

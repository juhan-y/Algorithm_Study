# 예제 3-1 거스름돈
N = 1260
li = [500, 100, 50, 10]

count = 0

for i in li:
    count += N // i
    N = N % i

print(count)


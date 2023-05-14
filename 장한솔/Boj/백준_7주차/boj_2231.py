import sys

N = int(sys.stdin.readline())

answer = 0

for i in range(1, N+1) :
    answer = i + sum(map(int, str(i))) # 생성자
    if answer == N :
        print(i)
        break
    elif i == N : # 생성자 없는 경우
        print(0)
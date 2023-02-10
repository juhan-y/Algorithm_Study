import sys

N = int(sys.stdin.readline())
time = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

time.sort(key = lambda x : (x[1], x[0]))

cnt = 0
etime = 0 # 현재 시간 저장
for i, j in time : 
    if etime <= i : # 만약 현재 시간이 회의 시작시간보다 작거나 같으면
        etime = j # 이제 시작할 회의 종료시간을 현재시간에 저장
        cnt += 1 # 회의 수 카운트

print(cnt)
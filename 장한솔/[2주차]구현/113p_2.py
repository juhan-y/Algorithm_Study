import sys

N = int(sys.stdin.readline())

t = 45*15 + 15*60 
# 분 기준 3이 들어가는 개수 15개 -> 60초 할당 --> 15*60
# 분 기준 3이 들어가지 않는 개수 45개 -> 초에 3이 들어가는 횟수 15번 --> 45*15

result = 0
for i in range(N+1) :
    if (i == 3) or (i == 13) or (i == 23) :
        result += (60 * 60)
    else :
        result += t
        
print(result)
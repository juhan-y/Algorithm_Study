import sys

N = int(sys.stdin.readline())

score = [list(map(str, sys.stdin.readline().split())) for i in range(N)]

for i in range(N) :
    score[i][1] = int(score[i][1])
    
score.sort(key=lambda x : x[1])

for i in range(N) :
    print(score[i][0], end = ' ')
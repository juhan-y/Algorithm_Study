import sys

N, M = map(int, sys.stdin.readline().split())

che = [list(map(str, sys.stdin.readline().strip())) for _ in range(N)]
cnt = []

for a in range(N-7) : # 8*8로 자르기 위함
    for b in range(M-7) :
        white = 0 # 좌상단이 white로 시작한 경우 개수 세기
        black = 0 # 좌상단이 black으로 시작한 경우 개수 세기

        for i in range(a, a+8) :
            for j in range(b, b+8) :
                if (i+j) % 2 == 0 : # 인덱스의 합이 짝수이면 좌상단과 색이 같음
                    if che[i][j] != "W" :
                        white += 1
                    elif che[i][j] != "B" :
                        black += 1
                else : # 인덱스의 합이 홀수이면 좌상단과 색이 다름
                    if che[i][j] != "B" :
                        white += 1
                    elif che[i][j] != "W" :
                        black += 1

        cnt.append(white)
        cnt.append(black)

print(min(cnt))
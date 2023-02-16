import sys

N, M = map(int, sys.stdin.readline().split())

hear = [sys.stdin.readline() for _ in range(N)]
see = [sys.stdin.readline() for _ in range(M)]

hear = set(hear)
see = set(see)

answer = sorted(list(hear & see)) # 교집합 기호 : &

print(len(answer))
for i in answer :
    print(i, end = "")
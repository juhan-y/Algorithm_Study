import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
q = deque()
answer = []

# 1번부터 N번까지 deque에 저장
for i in range(1, N+1) :
    q.append(i)

# deque가 비어있지 않으면 while 반복
while q :
    # 0, ... , K-2번째까지
    # ex) K = 3일 경우 1,2 번째를 제거 -> 인덱스로 따지면 0, 1(K-2)
    for i in range(K-1) :
        q.append(q.popleft()) # 뺀것을 다시 deque의 뒤에 저장
    # 현시점 제일 앞에 있는 숫자(K번째 수) 제거
    answer.append(q.popleft())

print("<", end = "")
print(*answer, sep = ", ", end = "")
print(">")
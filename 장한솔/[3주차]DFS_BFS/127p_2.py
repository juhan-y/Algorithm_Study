from collections import deque

queue = deque()

queue.append(5) # 5삽입 5
queue.append(2) # 2삽입 5 2
queue.append(3) # 3삽입 5 2 3
queue.append(7) # 7삽입 5 2 3 7
queue.popleft() # 제일 왼쪽값(제일 먼저 들어온 값 제거) 2 3 7
queue.append(1) # 1삽입 2 3 7 1
queue.append(4) # 4삽입 2 3 7 1 4
queue.popleft() # 제일 왼쪽값(제일 먼저 들어온 값 제거) 3 7 1 4

print(queue) # 3 7 1 4 출력 (출력은 deque 객체)
queue.reverse() # queue 순서 역순으로
print(queue) # 4 1 7 3 출력 (deque 객체)

queue.reverse()
print(list(queue)) # deque 객체를 list 자료형으로 바꿔서 출력
queue.reverse()
print(list(queue))
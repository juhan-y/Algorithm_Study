# 큐
# First in First Out

# 삽입 5,2,3,7 -> 삭제 -> 삽입 1, 4 -> 삭제

import sys
from collections import deque

q = deque()

q.append(5)
q.append(2)
q.append(3)
q.append(7)
# deque는 popleft, pop 둘다 가능
q.popleft()
q.append(1)
q.append(4)
q.popleft()

print(q)
q.reverse()
print(q)
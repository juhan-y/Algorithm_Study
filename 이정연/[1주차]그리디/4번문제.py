#!/usr/bin/env python
# coding: utf-8

# In[21]:


# 내 풀이
n, k = map(int, input().split())
result = 0

while True:
    while n % k != 0:
        if n == 1:
            break
        n -= 1
        result += 1
        
    if n == 1:
        break
        
    n = n // k
    result += 1
    
print(result)


# In[22]:


# 정석
n, k = map(int, input().split())
result = 0

while n >= k:
    # N이 K로 나누어 떨어지지 않는다면 N에서 1씩 빼기
    while n % k != 0:
        n -= 1
        result += 1
    
    # k로 나누기
    n //= k
    result += 1
    
# 마지막으로 1씩 빼기
while n > 1:
    n -= 1
    result += 1
    
print(result)


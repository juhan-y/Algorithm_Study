#!/usr/bin/env python
# coding: utf-8

# In[9]:


n, m, k = map(int, input().split())
array = list(map(int, input().split()))

array.sort()
first = array[-1]
second = array[-2]

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1
    
print(result)


# In[ ]:





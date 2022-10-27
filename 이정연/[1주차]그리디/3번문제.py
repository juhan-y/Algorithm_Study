#!/usr/bin/env python
# coding: utf-8

# In[3]:


n, m = map(int, input().split())
result = 0

for i in range(n):
    array = list(map(int, input().split()))
    tmp = min(array)
    result = max(result, tmp)
    
print(result)


# In[ ]:





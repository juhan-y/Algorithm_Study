# 2108_통계학
import sys
from collections import Counter

N = int(sys.stdin.readline())
li = []
for i in range(N):
    x = int(sys.stdin.readline())
    li.append(x)

li.sort()

avg = round(sum(li)/N

if (len(li))%2==0:
    med = (li[((len(li))//2)-1] + li[((len(li)//2)+1)-1]) / 2
else:
    med = li[len(li)//2]

num = Counter(li).most_common()
if len(li) > 1:
    if num[0][1] == num[1][1]:
        mo = num[1][0]
    else:
        mo = num[0][0]

length = max(li)-min(li)

print(avg)
print(med)
print(mo)
print(length)

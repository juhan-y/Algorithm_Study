import sys
input = sys.stdin.readline
n = int(input())
l = []
d = {}
most = []
for _ in range(n):
    i = int(input())
    l.append(i)
    if not d.get(i):
        d[i] = 1
    else:
        d[i] += 1
for key, value in d.items():
    if value == max(d.values()):
        most.append(key)

l.sort()
most.sort()

print(round(sum(l)/n))
print(l[n//2])
if len(most) <2:
    print(most[0])
else:
    print(most[1])
print(l[-1]-l[0])
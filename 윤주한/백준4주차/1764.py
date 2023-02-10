n, m = map(int, input().split())
d = set()
b = set()
for _ in range(n):
    d.add(input())
for _ in range(m):
    b.add(input())

new_set = b & d
print(len(new_set))
new_set = list(new_set)
new_set.sort()
for i in new_set:
    print(i)
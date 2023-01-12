import math

n = int(input())
for _ in range(n):
  a, b, c = map(int, input().split())
  cnt = math.ceil(c / a)
  floor = c % a
  if floor == 0:
    floor = a
  w = str(floor*100 + cnt)
  print(w)
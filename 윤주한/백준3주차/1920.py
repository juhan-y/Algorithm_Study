n = int(input())
ls = list(map(int, input().split()))
m = int(input())
chk = list(map(int, input().split()))

ls.sort()
for i in chk:
  left = 0
  right = len(ls) - 1
  check = False
  while left <= right:
    mid = (left + right) // 2
    if ls[mid] == i:
      check = True
      break
    elif ls[mid] < i:
      left = mid + 1
    elif ls[mid] > i:
      right = mid -1

  if check:
    print(1)
  else:
    print(0)
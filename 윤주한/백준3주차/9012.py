n = int(input())

def is_vps(s):
  ls = []
  for i in s:
    if i == '(':
      ls.append(1)
    else:
      ls.append(-1)

  if sum(ls) != 0:
    return 'NO'
  else:
    stack = []
    for i in ls:
      if i == 1:
        stack.append(i)
      else:
        if stack:
          stack.pop()
        else:
          return 'NO'

    if len(stack) == 0:
      return 'YES'
    else:
      return 'NO'

for _ in range(n):
  s = input()
  print(is_vps(s))
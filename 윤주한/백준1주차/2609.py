n, m = map(int, input().split())

def gcd(a, b):
  while b > 0:
    a, b = b, a % b
  return a

print(gcd(n, m))
print(int(n * m / gcd(n, m)))
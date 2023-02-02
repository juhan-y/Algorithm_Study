d0 = [0] * 41
d1 = [0] * 41
t = int(input())
## N은 40보다 작거나 같은 자연수 또는 0이다.
## 40으로 하면 안됨 indexerror -> 오류인듯
d0[0] = 1
d1[1] = 1

for i in range(2, 41):
    d0[i] = d0[i-1] + d0[i-2]
    d1[i] = d1[i-1] + d1[i-2]

for _ in range(t):
    n = int(input())
    print(d0[n], d1[n])
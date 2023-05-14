t = int(input())
jobs = []

for _ in range(t):
    jobs.append(list(map(int, input().split())))

d = [0] * t

for i in range(t-1, -1, -1):
    day, v = jobs[i]
    if i + day < t:
        d[i] = d[i+day] + v

        
print(d)

print(max(d))
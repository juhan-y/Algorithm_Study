n = int(input())
user = []
for _ in range(n):
    age, name = input().split()
    age = int(age)
    user.append([age, name])
user.sort(key = lambda x:x[0])
for i in user:
    print(i[0], i[1])
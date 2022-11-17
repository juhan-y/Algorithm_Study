n = int(input())
student = []

for _ in range(n):
    data = input().split()
    student.append([data[0], data[1]])

student.sort(key=lambda x: int(x[1]))

for i in student:
    print(i[0], end=' ')
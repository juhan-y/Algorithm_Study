import sys
input = sys.stdin.readline
n = int(input())
l = [0] * 10001
for _ in range(n):
    l[int(input())] += 1
for i in range(10001):
    if l[i] != 0:
        for _ in range(l[i]):
            print(i)



# for문 속에서 append를 사용하게 되면 메모리 재할당이 이루어져서 메모리를 효율적으로 사용못한다.
# import sys
# input = sys.stdin.readline
# n = int(input())
# l = []
# for _ in range(n):
#     l.append(int(input()))
# l.sort()
# for i in l:
#     print(i)
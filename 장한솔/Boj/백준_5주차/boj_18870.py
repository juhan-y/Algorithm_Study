import sys

N = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
num_set = sorted(list(set(num)))

num_dic = {num_set[i] : i for i in range(len(num_set))}

for j in num :
    print(num_dic[j], end = " ")

"""
list.index(i)의 시간복잡도 : O(n)
dictionary의 시간복잡도 : O(1)
"""
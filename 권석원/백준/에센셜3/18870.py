import sys
import bisect

N = int(sys.stdin.readline())
x_list = list(map(int,sys.stdin.readline().split()))

x_set = sorted(list(set((x_list))))

for x in x_list:
    print(bisect.bisect_left(x_set,x),end=' ')



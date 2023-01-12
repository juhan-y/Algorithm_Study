import sys

N = int(sys.stdin.readline())

m_list = []


for i in range(N):
    name, score = map(str,sys.stdin.readline().rstrip().split())
    m_list.append([name, score])

m_list.sort(key= lambda x : x[1])

for m in m_list:
    print(m[0] , end=' ')

import sys
import heapq

# 입력된 수가 몇번째에 들어왔는지 체크
# 팝 됐으면 체크
# 위에 체크된 사항들로 최소힙 최대힙 동기화

T = int(sys.stdin.readline())

for _ in range(T):

    N = int(sys.stdin.readline())

    heap_min = []
    heap_max = []
    check = [False] * N
    pos = 0

    for _ in range(N):
        cmd = sys.stdin.readline().split()

        if cmd[0] == 'D':
            num = int(cmd[1])

            if num < 0: #최소
                
                while heap_min and check[heap_min[0][1]] == False:
                        heapq.heappop(heap_min)

                if heap_min:
                    _, tmp = heapq.heappop(heap_min)
                    check[tmp] = False

            else: # 최대

                while heap_max and check[heap_max[0][1]]  == False:
                        heapq.heappop(heap_max)

                if heap_max:
                    _, tmp = heapq.heappop(heap_max)
                    check[tmp] = False

        elif cmd[0] == 'I':
            num = int(cmd[1])
            heapq.heappush(heap_min,(num,pos))
            heapq.heappush(heap_max,(-num,pos))
            check[pos] = True
            pos += 1

    while heap_min and check[heap_min[0][1]] == False:
            heapq.heappop(heap_min)
    
    while heap_max and check[heap_max[0][1]]  == False:
            heapq.heappop(heap_max)


    if heap_min and heap_max:
        print(-heap_max[0][0],end=' ')
        print(heap_min[0][0],end=' ')
    else:
        print('EMPTY')
    

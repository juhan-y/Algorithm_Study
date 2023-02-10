import sys
import heapq

T = int(sys.stdin.readline())

for _ in range(T) :
    k = int(sys.stdin.readline())
    max_heap = []
    min_heap = []
    ex = [0 for _ in range(k)] # 현재 힙에 있는 숫자인지 아닌지 체크 위함 -> 입력 순서로 기억

    for i in range(k) :
        ope, num = map(str, sys.stdin.readline().split())

        if ope == "I" :
            heapq.heappush(min_heap, (int(num), i))
            heapq.heappush(max_heap, (-int(num), i))
            ex[i] = 1

        elif ope == "D" :
            if num == "-1" : # 최소값 삭제
                # 이미 최대값으로 빠진 값 다 삭제처리
                while min_heap and not ex[min_heap[0][1]] :
                    heapq.heappop(min_heap)
                if min_heap :
                    ex[min_heap[0][1]] = 0 # 힙에서 뺐다고 알려주기
                    heapq.heappop(min_heap)
            elif num == "1" :
                # 이미 최솟값으로 빠진 값 다 삭제처리
                while max_heap and not ex[max_heap[0][1]] :
                    heapq.heappop(max_heap)
                if max_heap :
                    ex[max_heap[0][1]] = 0 # 힙에서 뺐다고 알려주기
                    heapq.heappop(max_heap)

    # 찐 최최최종 최소힙/최대힙 동기화
    while min_heap and not ex[min_heap[0][1]]:
        heapq.heappop(min_heap)
    while max_heap and not ex[max_heap[0][1]]:
        heapq.heappop(max_heap)

    if min_heap and max_heap :
        print(-max_heap[0][0], min_heap[0][0])
    else :
        print("EMPTY")
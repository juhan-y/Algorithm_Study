import heapq, sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    k = int(input())
    q = []
    origin_q = []
    flip_q = []
    for _ in range(k):
        order, num = input().split()
        if order == 'I':
            heapq.heappush(q, int(num))
            heapq.heappush(origin_q, int(num))
            heapq.heappush(flip_q, (-int(num), int(num)))
        else:
            if q:
                # 최소 제거
                if num == '-1':
                    heapq.heappop(origin_q)
                # 최대 제거
                else:
                    heapq.heappop(flip_q)
                heapq.heappop(q)
    if not q:
        print('EMPTY')
    else:
        print(heapq.heappop(flip_q)[1], heapq.heappop(origin_q))


# t 1
# origin   16,     
# flip     (5643, -5643), (-123, 123)

# t 2
# origin -45,         653,         45,        97,  333
# flip   (45, -45),        (642, -642), (-45, 45), (-333, 333)


# 반례
# 1

# 9

# I 36

# I 37

# I 38

# D 1

# D 1

# I 39

# I 40

# D -1

# D -1
# origin 38, 39, 40
# flip (-36, 36) , (-39, 39), (-40, 40)
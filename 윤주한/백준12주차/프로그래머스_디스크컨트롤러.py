import heapq


def solution(jobs):
    q = []
    for i in range(len(jobs)):
        heapq.heappush(q, (jobs[i][0], jobs[i][1]))

    sec = 0
    now = False
    ans = 0
    q_in = []
    while q_in or q:
        if now:
            while q and q[0][0] <= sec:
                time, length = heapq.heappop(q)
                heapq.heappush(q_in, (length, time))

            if q_in:
                length, time = heapq.heappop(q_in)
                sec += length
                ans += (sec - time)
            else:
                if q:
                  now = False

        else:
            time, length = heapq.heappop(q)
            now = True
            sec = time
            sec += length
            ans += (sec - time)

    return ans // len(jobs)

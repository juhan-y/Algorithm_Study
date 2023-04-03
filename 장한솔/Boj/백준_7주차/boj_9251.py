import sys

S1 = sys.stdin.readline().strip()
S2 = sys.stdin.readline().strip()
answer = [0] * len(S2)

for i in range(len(S1)) :
    cnt = 0
    for j in range(len(S2)) :
        if answer[j] > cnt : # 순서를 지켜야하는 계산, max값으로 받으면 안됨.
            cnt = answer[j]
        elif S1[i] == S2[j] :
            answer[j] = cnt + 1
        # print(answer, cnt)
    # print("-" * 50)

print(max(answer))
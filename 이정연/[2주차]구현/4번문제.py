#!/usr/bin/env python
# coding: utf-8

# - N * M 크기의 직사각형, 각각의 칸은 육지 또는 바다
# - 캐릭터는 동서남북 중 한 곳을 바라봄
# 
# - 각 칸은 (A, B)로 나타냄
#     - A는 북쪽으로부터 떨어진 칸의 개수
#     - B는 서쪽으로부터 떨어진 칸의 개수
#     
# - 캐릭터는 상하좌우로 움직임. 바다는 갈 수 없음

# 1. 현재 위치에서 현재 방향을 기준으로 왼쪽 방향부터 차례대로 갈 곳을 정한다
# 2. 
# - 왼쪽 방향에 아직 가보지 않은 칸이 존재한다면, 왼쪽 방향으로 회전한 다음 왼쪽으로 한 칸을 전진.
# - 왼쪽 방향에 가보지 않은 칸이 없다면, 왼쪽 방향으로 회전만 수행한 뒤 1단계로.
#     
# 3. 네 방향 모두 가본 칸 or 바다로 되어 있는 칸이면,
# - 바라보는 방향을 유지한 채로 한 칸 뒤로 가고 1단계로.
# - 단, 뒤쪽이 바다인 경우 움직임을 멈춘다.

# - 캐릭터가 방문한 칸의 수를 출력

# ### 지금까지 시도

# In[76]:


# N * M 크기의 직사각형
N, M = map(int, input().split())

# 칸의 좌표 (A, B) 와 바라보는 방향 d (북동남서 : 0123)
A, B, direction = map(int, input().split())

# 맵 (0은 육지, 1은 바다)
graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))

# 현재 1, 1에서 북쪽 방향을 바라보고 있음
# 북동남서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

count = 1

# 현재 좌표를 1로 처리
graph[A][B] = 1


# In[ ]:


# 왼쪽으로 회전하는 함수
def turn_left(d):
    d -= 1
    if d == -1:
        d = 3
        
    return(d)


# In[66]:


# turn left를 4번 실행
while True:
    direction = turn_left(direction)
    tmp_x = dx[direction]
    tmp_y = dy[direction]
    
    #print(direction, tmp_x, tmp_y)
    
    # 바라보는 방향에 0이 있으면 이동
    if graph[A+tmp_x][B+tmp_y] == 0:
        print(A+tmp_x, B+tmp_y)
        graph[A+tmp_x][B+tmp_y] = 1
        count += 1
        A, B = A+tmp_x, B+tmp_y
        turn_time = 0
        continue

    # 네 방향 모두 가본 칸 or 바다로 가본 칸이면
    else:
        # 검증해보자
        tmp_x = A-dx[direction]
        tmp_y = B-dy[direction]
        # 바라보는 방향을 유지한 채로 한칸 뒤로
        if : # 몰?루 ㅠㅠ
            A = tmp_x
            B = tmp_y
        # 뒤쪽이 바다라면,
        else:
            break
            
print(count)


# ### 정답

# In[74]:


# N * M 크기의 직사각형
n, m = map(int, input().split())

# 방문한 위치를 저장하기 위한 맵
d = [[0] * m for _ in range(n)]

# 칸의 좌표 (A, B) 와 바라보는 방향 d (북동남서 : 0123)
x, y, direction = map(int, input().split())

# 현재 좌표를 1로 처리
d[x][y] = 1

# 맵 (0은 육지, 1은 바다)
array = []
for i in range(N):
    array.append(list(map(int, input().split())))

# 현재 1, 1에서 북쪽 방향을 바라보고 있음
# 북동남서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


# In[75]:


# 왼쪽으로 회전하는 함수
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3
        
# 시뮬레이션 시작
count = 1
turn_time = 0
while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    
    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
        
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1
        
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = A - dx[direction]
        ny = B - dy[direction]
        
        # 뒤로 갈 수 있다면 이동
        if array[nx][ny] == 0:
            x = nx
            y = ny
        
        # 뒤가 바다인 경우
        else:
            break
        turn_time = 0
        
print(count)


# In[ ]:





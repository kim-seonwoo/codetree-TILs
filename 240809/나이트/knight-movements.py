import sys
from collections import deque

# 변수 선언 및 입력
n = int(input())

ans = 0

r1, c1, r2, c2 = tuple(map(int, input().split()))

# bfs에 필요한 변수들 입니다.
q = deque()
visited = [
    [False for _ in range(n)]
    for _ in range(n)
]
# step[i][j] : 시작점으로부터 (i, j) 지점에 도달하기 위한 
# 최단거리를 기록합니다.
step = [
    [0 for _ in range(n)]
    for _ in range(n)
]


def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n


# 격자를 벗어나지 않으면서, 뱀도 없고, 아직 방문한 적이 없는 곳이라면
# 지금 이동하는 것이 최단거리임을 보장할 수 있으므로 가야만 합니다. 
def can_go(x, y):
    return in_range(x, y) and not visited[x][y]


# queue에 새로운 위치를 추가하고
# 방문 여부를 표시해줍니다.
# 시작점으로 부터의 최단거리 값도 갱신해줍니다.
def push(new_x, new_y, new_step):
    q.append((new_x, new_y))
    visited[new_x][new_y] = True
    step[new_x][new_y] = new_step
    
    
# bfs를 통해 최소 이동 횟수를 구합니다.
def find_min():
    global ans
    
    dxs = [-2, -1, 1, 2, 2, 1, -1, -2]
    dys = [1, 2, 2, 1, -1, -2, -2, -1]

    
    # queue에 남은 것이 없을때까지 반복합니다.
    while q:
        # queue에서 가장 먼저 들어온 원소를 뺍니다.
        x, y = q.popleft()    
    
        # queue에서 뺀 원소의 위치를 기준으로 4방향을 확인해봅니다.
        for dx, dy in zip(dxs, dys):
            new_x, new_y = x + dx, y + dy
        
            # 아직 방문한 적이 없으면서 갈 수 있는 곳이라면
            # 새로 queue에 넣어줍니다.
            if can_go(new_x, new_y):
                # 최단 거리는 이전 최단거리에 1이 증가하게 됩니다.
                push(new_x, new_y, step[x][y] + 1)

            if new_x == r2 and new_y == c2:
                ans = step[x][y]

# bfs를 이용해 최소 이동 횟수를 구합니다.
# 시작점을 queue에 넣고 시작합니다.
push(r1, c1, 0)
find_min()

# 불가능한 경우라면 -1을 답으로 넣어줍니다.
if ans == 0:
    ans = -1
    
print(ans - 1)
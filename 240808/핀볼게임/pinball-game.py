def pinball_max_time(n, grid):
    # 방향: 위, 아래, 왼쪽, 오른쪽
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def next_direction(current_dir, cell_value):
        if cell_value == 1:
            if current_dir == (-1, 0): return (0, -1)  # 위 -> 왼쪽
            if current_dir == (1, 0): return (0, 1)   # 아래 -> 오른쪽
            if current_dir == (0, -1): return (-1, 0) # 왼쪽 -> 위
            if current_dir == (0, 1): return (1, 0)   # 오른쪽 -> 아래
        elif cell_value == 2:
            if current_dir == (-1, 0): return (0, 1)  # 위 -> 오른쪽
            if current_dir == (1, 0): return (0, -1)  # 아래 -> 왼쪽
            if current_dir == (0, -1): return (1, 0)  # 왼쪽 -> 아래
            if current_dir == (0, 1): return (-1, 0)  # 오른쪽 -> 위
        return current_dir

    def simulate(x, y, direction):
        time = 0
        while 0 <= x < n and 0 <= y < n:
            time += 1
            if grid[x][y] in (1, 2):
                direction = next_direction(direction, grid[x][y])
            x += direction[0]
            y += direction[1]
        return time + 1  # 격자 밖으로 나가는 시간 포함

    max_time = 0

    # 격자 가장자리 4 * n 개의 시작 지점과 방향 설정
    for i in range(n):
        for direction in directions:
            # 상단
            max_time = max(max_time, simulate(0, i, (1, 0)))  # 아래로 진행
            # 하단
            max_time = max(max_time, simulate(n - 1, i, (-1, 0)))  # 위로 진행
            # 좌측
            max_time = max(max_time, simulate(i, 0, (0, 1)))  # 오른쪽으로 진행
            # 우측
            max_time = max(max_time, simulate(i, n - 1, (0, -1)))  # 왼쪽으로 진행

    return max_time

# 예제 입력
n1 = 5
grid1 = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [1, 0, 1, 0, 2],
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 2]
]

n2 = 5
grid2 = [
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1]
]

print(pinball_max_time(n1, grid1))  # 출력: 10
print(pinball_max_time(n2, grid2))  # 출력: 10
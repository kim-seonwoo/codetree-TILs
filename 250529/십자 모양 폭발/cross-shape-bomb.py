n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())  # r: 행, c: 열

dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def bomb(x, y):
    power = grid[x][y]
    grid[x][y] = 0  

    for dx, dy in zip(dxs, dys):
        for dist in range(1, power):
            nx = x + dx * dist
            ny = y + dy * dist
            if in_range(nx, ny):
                grid[nx][ny] = 0

def move():
    for col in range(n):
        temp = []
        for row in range(n - 1, -1, -1):  # 아래 → 위
            if grid[row][col] != 0:
                temp.append(grid[row][col])
        # 채워넣기
        for row in range(n - 1, -1, -1):
            if temp:
                grid[row][col] = temp.pop(0)
            else:
                grid[row][col] = 0

bomb(r - 1, c - 1)
move()

for row in grid:
    print(*row)

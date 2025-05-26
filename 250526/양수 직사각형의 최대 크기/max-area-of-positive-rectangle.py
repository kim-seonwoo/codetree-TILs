n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

max_area = 0

def is_valid(x1, y1, x2, y2):
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            if grid[i][j] < 0:
                return False
    return True

for i in range(n):
    for j in range(m):
        for ni in range(i, n):
            for nj in range(j, m):
                if is_valid(i, j, ni, nj):  # 여기서만 넓이 계산
                    area = (ni - i + 1) * (nj - j + 1)
                    max_area = max(max_area, area)

print(max_area if max_area > 0 else -1)

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
        for end_i in range(i, n):
            for end_j in range(j, m):
                if is_valid(i, j, end_i, end_j):
                    area = (end_i - i + 1) * (end_j - j + 1)
                    max_area = max(max_area, area)

print(max_area if max_area > 0 else -1)

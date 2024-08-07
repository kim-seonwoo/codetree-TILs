# 변수 선언 및 입력:
import copy

n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

def in_bomb_range(x, y, center_x, center_y, bomb_range):
    return (x == center_x or y == center_y) and \
           abs(x - center_x) + abs(y - center_y) < bomb_range

def bomb_and_apply_gravity(center_x, center_y):
    bomb_range = grid[center_x][center_y]
    next_grid = [
        [0 for _ in range(n)]
        for _ in range(n)
    ]

    # Step1. 폭탄이 터질 위치는 0으로 채워줍니다.
    for i in range(n):
        for j in range(n):
            if in_bomb_range(i, j, center_x, center_y, bomb_range):
                grid[i][j] = 0

    # Step2. 폭탄이 터진 이후의 결과를 next_grid에 저장합니다.
    for j in range(n):
        next_row = n - 1
        for i in range(n - 1, -1, -1):
            if grid[i][j] != 0:
                next_grid[next_row][j] = grid[i][j]
                next_row -= 1
                
    # Step3. 원래의 grid 복원
    for i in range(n):
        for j in range(n):
            grid[i][j] = next_grid[i][j]

    return next_grid

def count_pairs(grid):
    pairs = 0
    for i in range(n):
        for j in range(n):
            if i < n - 1 and grid[i][j] == grid[i + 1][j] and grid[i][j] != 0:
                pairs += 1
            if j < n - 1 and grid[i][j] == grid[i][j + 1] and grid[i][j] != 0:
                pairs += 1
    return pairs

max_pairs = 0

for r in range(n):
    for c in range(n):
        original_grid = copy.deepcopy(grid)
        next_grid = bomb_and_apply_gravity(r, c)
        pairs = count_pairs(next_grid)
        max_pairs = max(max_pairs, pairs)
        grid = original_grid  # 원래의 grid로 되돌려줌

print(max_pairs)
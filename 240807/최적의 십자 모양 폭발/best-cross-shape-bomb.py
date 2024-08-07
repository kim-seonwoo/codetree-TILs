def in_bomb_range(x, y, center_x, center_y, bomb_range):
    return (x == center_x or y == center_y) and \
           abs(x - center_x) + abs(y - center_y) < bomb_range

def bomb_and_apply_gravity(grid, center_x, center_y):
    n = len(grid)
    bomb_range = grid[center_x][center_y]
    
    # 폭탄 효과 적용
    for i in range(n):
        for j in range(n):
            if in_bomb_range(i, j, center_x, center_y, bomb_range):
                grid[i][j] = 0

    # 중력 효과 적용
    for j in range(n):
        stack = []
        for i in range(n-1, -1, -1):
            if grid[i][j]:
                stack.append(grid[i][j])
        
        for i in range(n-1, -1, -1):
            if stack:
                grid[i][j] = stack.pop(0)
            else:
                grid[i][j] = 0

def count_pairs(grid):
    n = len(grid)
    pair_count = 0
    for i in range(n):
        for j in range(n):
            if i > 0 and grid[i][j] == grid[i-1][j]:
                pair_count += 1
            if j > 0 and grid[i][j] == grid[i][j-1]:
                pair_count += 1
    return pair_count

# 입력 받기
n = int(input())
original_grid = [list(map(int, input().split())) for _ in range(n)]

max_pairs = 0

for i in range(n):
    for j in range(n):
        # 원본 그리드를 복사하여 폭탄 터뜨리기 및 중력 적용
        grid = [row[:] for row in original_grid]
        bomb_and_apply_gravity(grid, i, j)
        # 터뜨린 후 쌍의 개수 세기
        pairs = count_pairs(grid)
        if pairs > max_pairs:
            max_pairs = pairs

print(max_pairs)
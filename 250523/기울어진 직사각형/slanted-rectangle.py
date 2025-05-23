n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

# for (i, j로 시작점을 잡는다)
# 함수에 각각 위치를 넣음
# 순회하면서 진행 방향을 select
# for 이중문을 수행하면서 가로 길이와 세로 길이를 고른다.

max_range = n - 1
result = 0

def in_range(x, y):
    if x <= n - 1 and y <= n - 1:
        return True
    return False

def cal_count(range_x, range_y, dx, dy):
    count = 0
    save_x = dx
    save_y = dy
    if not in_range(save_x + range_x, save_y + range_y):
        return 0

    if not in_range(save_x - range_x, save_y + range_y):
        return 0

    if not in_range(save_x + range_x, save_y - range_y):
        return 0

    if not in_range(save_x - range_x, save_y - range_y):
        return 0

    for i in range(range_x):
        dxs = save_x + i
        dys = save_y + i
        if not in_range(dxs, dys):
            return 0
        count += grid[dxs][dys]
        save_x = dxs
        save_y = dys

    for i in range(range_y):
        dxs = save_x - i
        dys = save_y + i
        if not in_range(dxs, dys):
            return 0
        count += grid[dxs][dys]
        save_x = dxs
        save_y = dys

    for i in range(range_x):
        dxs = save_x - i
        dys = save_y - i
        if not in_range(dxs, dys):
            return 0

        count += grid[dxs][dys]
        save_x = dxs
        save_y = dys

    for i in range(range_y):
        dxs = save_x + i
        dys = save_y - i
        if not in_range(dxs, dys):
            return 0
        count += grid[dxs][dys]
        save_x = dxs
        save_y = dys

    return count


def square(x, y):
    max_count = 0
    for i in range(max_range):
        for j in range(max_range):
            max_count = max(max_count, cal_count(i, j, x, y))

    return max_count

for i in range(n):
    for j in range(n):
        answer = square(i, j)
        result = max(result, answer)


print(result)
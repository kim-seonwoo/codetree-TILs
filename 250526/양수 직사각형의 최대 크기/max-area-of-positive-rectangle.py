n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

max_num = -1

def cal(x, y, plus_i, plus_j):
    result = 0
    for i in range(x, plus_i + 1):
        for j in range(y, plus_j + 1):
            if grid[i][j] <= 0:
                return -1
            else:
                result += 1

    return (plus_i + 1 - x) * (plus_j + 1 - y)


for i in range(n):
    for j in range(m):
        for num_i in range(i, n):
            for num_j in range(j, m):
                max_num = max(max_num, cal(i, j, num_i, num_j))


if max_num == -1:
    print(-1)
else:
    print(max_num)
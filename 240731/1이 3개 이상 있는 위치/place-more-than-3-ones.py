total_num = int(input())
array = []
cnt = 0
dxs, dxy = [0, 1, 0, -1], [1, 0, -1, 0]

def in_range(x, y):
    return 0 <= x < total_num and 0 <= y < total_num

def calNum(x, y):
    global cnt
    small_cnt = 0
    for dx, dy in zip(dxs, dxy):
        nx, ny = x + dx, y + dy

        if in_range(nx, ny) and array[nx][ny] == "1":
            small_cnt += 1

    if small_cnt >= 3:
        cnt += 1

for i in range(total_num):
    new_arr = input().split()
    array.append(new_arr)

for x in range(total_num):
    for y in range(total_num):
        calNum(x, y)

print(cnt)
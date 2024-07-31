c_dir = input()
dir_num = 3
x, y = 0, 0

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

for dist in c_dir:
    if dist == "L":
        dir_num = (dir_num + 3) % 4
    elif dist == "R":
        dir_num = (dir_num + 1) % 4
    else:
        x, y = x + dx[dir_num], y + dy[dir_num]

print(x, y)
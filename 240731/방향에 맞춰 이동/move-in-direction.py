def calDir(direction, amount, x, y):
    amount = int(amount)
    if direction == 'E':
        dir_num = 0
    elif direction == 'S':
        dir_num = 1
    elif direction == 'W':
        dir_num = 2
    elif direction == 'N':
        dir_num = 3
    
    calDx, calDy = [1, 0, -1, 0], [0, -1, 0, 1]
    nx, ny = x + calDx[dir_num] * amount, y + calDy[dir_num] * amount

    return nx, ny

total_num = int(input())
x, y = 0, 0

for i in range(total_num):
    direction, amount = input().split()
    x, y = calDir(direction, amount, x, y)

print(x, y)
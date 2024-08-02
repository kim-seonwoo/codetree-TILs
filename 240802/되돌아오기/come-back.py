# 입력 처리
n = int(input())
commands = []
for _ in range(n):
    direction, amount = input().split()
    commands.append((direction, int(amount)))

# 방향 설정 (북, 동, 남, 서)
direction_map = {
    'N': (-1, 0),
    'E': (0, 1),
    'S': (1, 0),
    'W': (0, -1)
}

# 초기 위치
x, y = 0, 0
time = 0

# 이동 처리
for direction, amount in commands:
    dx, dy = direction_map[direction]
    for _ in range(amount):
        x += dx
        y += dy
        time += 1
        if x == 0 and y == 0:
            print(time)
            exit()

# 시작점으로 돌아오지 못한 경우
print(-1)
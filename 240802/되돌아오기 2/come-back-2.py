def find_return_time(commands):
    # 방향 설정 (북, 동, 남, 서)
    directions = ['N', 'E', 'S', 'W']
    direction_vectors = {
        'N': (-1, 0),
        'E': (0, 1),
        'S': (1, 0),
        'W': (0, -1)
    }
    
    # 초기 상태
    x, y = 0, 0
    direction_index = 0  # 처음에는 북쪽을 향함
    time = 0
    
    # 명령어 처리
    for command in commands:
        if command == 'L':
            direction_index = (direction_index - 1) % 4  # 왼쪽으로 90도 회전
            time += 1
        elif command == 'R':
            direction_index = (direction_index + 1) % 4  # 오른쪽으로 90도 회전
            time += 1
        elif command == 'F':
            dx, dy = direction_vectors[directions[direction_index]]
            x += dx
            y += dy
            time += 1
        
        # 시작점으로 돌아온 경우
        if x == 0 and y == 0:
            return time
    
    # 모든 명령어 처리 후에도 돌아오지 못한 경우
    return -1

# 입력
commands = input().strip()

# 결과 계산
result = find_return_time(commands)

# 출력
print(result)
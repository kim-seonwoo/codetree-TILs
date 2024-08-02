def final_position(n, t, r, c, d):
    # 방향을 숫자로 매핑
    directions = {
        'U': 0,
        'D': 1,
        'R': 2,
        'L': 3
    }
    
    # 방향 벡터 설정 (상, 하, 우, 좌)
    dxs = [-1, 1, 0, 0]
    dys = [0, 0, 1, -1]
    
    # 초기 위치 및 방향 설정
    x, y = r - 1, c - 1  # 1-indexed to 0-indexed
    dir_num = directions[d]
    
    # n번 반복
    for _ in range(t):
        # 다음 위치 계산
        nx, ny = x + dxs[dir_num], y + dys[dir_num]
        
        # 벽에 부딪힌 경우
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            # 방향 반대로 전환
            if dir_num == 0: dir_num = 1  # U -> D
            elif dir_num == 1: dir_num = 0  # D -> U
            elif dir_num == 2: dir_num = 3  # R -> L
            elif dir_num == 3: dir_num = 2  # L -> R
            # 다시 이동 계산
            nx, ny = x + dxs[dir_num], y + dys[dir_num]
        
        # 위치 업데이트
        x, y = nx, ny
    
    # 0-indexed to 1-indexed
    return x + 1, y + 1

# 입력
n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r), int(c)

# 결과 계산
result = final_position(n, t, r, c, d)

# 출력
print(result[0], result[1])
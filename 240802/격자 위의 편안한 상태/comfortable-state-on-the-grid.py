def is_comfortable(x, y, grid, N):
    # 인접한 칸의 좌표 (상, 하, 좌, 우)
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
    
    count = 0
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N and grid[nx][ny] == 1:
            count += 1
    
    return count == 3

def main():
    # 입력 처리
    N, M = map(int, input().split())
    commands = [tuple(map(int, input().split())) for _ in range(M)]
    
    # 격자 초기화
    grid = [[0] * N for _ in range(N)]
    
    # 결과 저장
    results = []
    
    for r, c in commands:
        # 1-indexed to 0-indexed
        x, y = r - 1, c - 1
        
        # 칠하기
        grid[x][y] = 1
        
        # 편안한 상태인지 체크
        if is_comfortable(x, y, grid, N):
            results.append(1)
        else:
            results.append(0)
    
    # 결과 출력
    for result in results:
        print(result)

# 실행
main()
n, m = map(int, input().split())
grid = []
for i in range(n):
    row = list(map(int, input().split()))
    grid.append(row)

# Initialize dp array
dp = [[0] * m for _ in range(n)]

# Initialize first row and first column
for c in range(m):
    dp[0][c] = grid[0][c]
for r in range(n):
    dp[r][0] = grid[r][0]

# Fill dp table
max_size = 0
for r in range(1, n):
    for c in range(1, m):
        if grid[r][c] > 0:
            dp[r][c] = min(dp[r-1][c], dp[r][c-1], dp[r-1][c-1]) + 1
            max_size = max(max_size, dp[r][c])

# Check if there's any positive rectangle
if max_size == 0:
    print(-1)
else:
    print(max_size * max_size)
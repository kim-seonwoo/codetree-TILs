def count_happy_sequences(n, m, grid):
    happy_count = 0

    # Count happy sequences in rows
    for row in range(n):
        consecutive_count = 1
        for col in range(1, n):
            if grid[row][col] == grid[row][col - 1]:
                consecutive_count += 1
            else:
                if consecutive_count >= m:
                    happy_count += 1
                consecutive_count = 1
        # Check the last segment in the row
        if consecutive_count >= m:
            happy_count += 1

    # Count happy sequences in columns
    for col in range(n):
        consecutive_count = 1
        for row in range(1, n):
            if grid[row][col] == grid[row - 1][col]:
                consecutive_count += 1
            else:
                if consecutive_count >= m:
                    happy_count += 1
                consecutive_count = 1
        # Check the last segment in the column
        if consecutive_count >= m:
            happy_count += 1

    return happy_count

# Main program
import sys
input = sys.stdin.read
data = input().splitlines()

first_line = data[0].split()
n = int(first_line[0])
m = int(first_line[1])

grid = []
for i in range(1, n + 1):
    row = list(map(int, data[i].split()))
    grid.append(row)

result = count_happy_sequences(n, m, grid)
print(result)
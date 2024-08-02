def main():
    # Read input
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    T = int(data[1])
    commands = data[2]
    
    # Reading the grid
    grid = []
    index = 3
    for i in range(N):
        row = list(map(int, data[index:index + N]))
        grid.append(row)
        index += N
    
    # Initial position (center of the grid)
    x, y = N // 2, N // 2
    
    # Direction vectors for North, East, South, West (NESW)
    dxs = [-1, 0, 1, 0]
    dys = [0, 1, 0, -1]
    
    # Initial direction is North (index 0)
    direction = 0
    
    # Initialize the sum with the starting position
    total_sum = grid[x][y]
    
    for command in commands:
        if command == 'L':
            # Turn left (counter-clockwise)
            direction = (direction + 3) % 4
        elif command == 'R':
            # Turn right (clockwise)
            direction = (direction + 1) % 4
        elif command == 'F':
            # Move forward in the current direction
            nx, ny = x + dxs[direction], y + dys[direction]
            
            # Check if the new position is within bounds
            if 0 <= nx < N and 0 <= ny < N:
                x, y = nx, ny
                total_sum += grid[x][y]
    
    # Output the result
    print(total_sum)

# Call the main function
main()
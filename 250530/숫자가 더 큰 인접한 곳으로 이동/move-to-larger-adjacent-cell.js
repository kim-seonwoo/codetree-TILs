const fs = require("fs");
const input = fs.readFileSync(0).toString().trim().split('\n');

let [n, currX, currY] = input[0].split(' ').map(Number);
let grid = input.slice(1, n + 1).map(line => line.split(' ').map(Number));

// Please Write your code here.

const dx = [-1, 1, 0, 0]
const dy = [0, 0, -1, 1]
let result = []

function in_range(x, y) {
    if (0 <= x && x < n && 0 <= y && y < n) {
        return true;
    } else {
        return false;
    }
}

function simulate(x, y) {

    const curr = grid[x][y]
    result.push(curr)
    let is_end = false
    for(i = 0; i < 4; i++) {
        new_x = x + dx[i]
        new_y = y + dy[i]

        if(in_range(new_x, new_y)) {
            if(grid[new_x][new_y] > curr) {
                simulate(new_x, new_y)
                is_end = true
            }
        } else {
            continue
        }
    }

    if(is_end === false) {
        console.log(result.join(' '))
    }
}

simulate(currX - 1, currY - 1)
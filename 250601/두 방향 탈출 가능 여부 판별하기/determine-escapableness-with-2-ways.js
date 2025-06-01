const fs = require("fs");
const input = fs.readFileSync(0).toString().trim().split('\n');

const [n, m] = input[0].split(' ').map(Number);
const grid = input.slice(1, n + 1).map(row => row.split(' ').map(Number));

// Please Write your code here.

let visited = Array.from({ length: n }, () => Array(m).fill(false));

const dx = [0 , 1]
const dy = [1, 0]

let result = 0

function canGo(new_x, new_y) {
    if (0 <= new_x && new_x < n && 0 <= new_y && new_y < m) {
    
    } else {
    return false
    }

    if ( visited[new_x][new_y] ) {
        return false
    }

    if (!grid[new_x][new_y]) {
        return false
    }

    return true
}

function dfs(x, y) {
    visited[x][y] = true
    if (x === n - 1 && y === m - 1) {
        // 종료 조건
        result = 1
    }

    for (let i = 0; i < 2; i++) {
        let new_x = x + dx[i];
        let new_y = y + dy[i];


        if ( canGo(new_x, new_y)) {
            dfs(new_x, new_y)
        }
    }
}

dfs(0, 0)

console.log(result)
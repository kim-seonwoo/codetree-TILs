const fs = require("fs");
const input = fs.readFileSync(0).toString().trim().split('\n');

const [n, m] = input[0].split(' ').map(Number);

// Please Write your code here.

result = []

function check() {
    for (let i = 0; i < result.length - 1; i++) {

        if (result[i] >= result[i + 1]) {
            return false
        }
    }


    return true
}

function print_answer() {
    console.log(result.join(' '))
}

function simulation(depth, num) {
    if (result.length === m) {

        if (check()) {
            print_answer()
        }

        return
    }

    for (let i = num; i < n + 1; i++) {
        result.push(i)
        simulation(depth + 1, i)
        result.pop()
    }
}

simulation(0, 1)
const fs = require("fs");
const input = fs.readFileSync(0).toString().trim().split('\n');

const [k, n] = input[0].split(' ').map(Number);

// Please Write your code here.

result = []

function print_answer() {
    console.log(result.join(' '))
}

function check() {
    let count = 0
    for(let i = 0; i < result.length - 1; i++) {
        if (result[i] === result[i + 1]) {
            count += 1
            if (count === 2) {
                return false
            }
         } else {
            count = 0
        }
    }

    return true
}

function simulation(depth) {
    //  종료 조건 return n과 같으면 종료
    if (depth === n) {
        if (check()) {
            print_answer()
        }
        return
    }

    for(let i = 1; i < k + 1; i++) {
        result.push(i)
        simulation(depth + 1)
        result.pop()
    }
}

simulation(0)
const fs = require('fs');
const input = require('fs').readFileSync('/dev/stdin').toString().split('\n');
// const input = fs.readFileSync('./예제.txt').toString().split('\n');
let n = Number(input.shift())
let arr = input.map(v=>v.split(' ').map(Number))
const dp = Array(n).fill(0)

for(let i = 0 ; i < n ; i++){
    const [day, pay] = arr[i]

    if(i + day > n){
        continue
    }

    dp[i] += pay

    for(let j = i + day ; j < n; j++){
        dp[j] = Math.max(dp[j], dp[i])
    }
}

console.log(Math.max(...dp))
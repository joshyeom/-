const fs = require("fs");
const input = require("fs").readFileSync("/dev/stdin").toString().split("\n");
// const input = fs.readFileSync("./예제.txt").toString().split("\n");
let [N, K] = input[0].split(" ").map(Number);

const coins = [];
let count = 0;

for (let i = 1; i < N + 1; i++) {
  coins.push(parseInt(input[i]));
}

while (coins.length > 0) {
  const coin = coins.pop();

  if (K < coin) continue;

  count += Math.floor(K / coin);
  K %= coin;
}

console.log(count);

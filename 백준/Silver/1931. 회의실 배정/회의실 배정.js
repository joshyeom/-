const fs = require("fs");
const file = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = fs.readFileSync(file).toString().trim().split("\n");
const [n, ...arr] = input;

const times = arr
  .map((num) => num.split(" ").map((num) => +num))
  .sort((a, b) => {
    if (a[1] === b[1]) {
      return a[0] - b[0];
    } else {
      return a[1] - b[1];
    }
  });

let count = 0;
let end = 0;

for (let i = 0; i < times.length; i++) {
  if (times[i][0] >= end) {
    count += 1;
    end = times[i][1];
  }
}

console.log(count);

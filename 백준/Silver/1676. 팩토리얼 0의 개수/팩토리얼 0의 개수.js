let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split(" ");

function Factorial(input) {
  let answer = 0;
  if (input === 0) return answer;
  for (let i = 5; i <= input; i += 5) {
    if (i % 5 === 0) answer++;
    if (i % 25 === 0) answer++;
    if (i % 125 === 0) answer++;
  }
  return answer;
}

console.log(Factorial(input));

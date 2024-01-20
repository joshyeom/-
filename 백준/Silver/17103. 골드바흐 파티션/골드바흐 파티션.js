const fs = require("fs");
// TODO: 제출 시 경로 변환 필수 ("/dev/stdin")
const input = fs
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .replaceAll("\r", "")
  .split("\n");

// 풀이
function solution(sum) {
  let count = sum.shift();
  let max = Math.max(...sum.map(Number));
  let primeNumber = new Array(max).fill(true);
  let result = "";
  primeNumber[0] = false;
  primeNumber[1] = false;
  for (let i = 2; i < max / 2; i++) {
    if (primeNumber[i]) {
      for (let j = 2; j <= max / i; j++) {
        primeNumber[i * j] = false;
      }
    }
  }
  sum.forEach((val) => {
    let cnt = 0;
    // 순서만 다른 경우 제외하기 위해 나누기 2
    for (let i = 2; i <= val / 2; i += 1) {
      if (primeNumber[i] && primeNumber[val - i]) {
        cnt++;
      }
    }
    result += `${cnt}\n`;
  });
  return result;
}
console.log(solution(input));

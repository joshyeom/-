const fs = require("fs");
// TODO: 제출 시 경로 변환 필수 ("/dev/stdin")
const input = fs
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .replaceAll("\r", "")
  .split("\n");

// 풀이
function solution(s) {
  const step = Number(s[0]);
  const arr = Array.from(new Array(step + 1), () => new Array(10));
  const MOD = 1000000000;
  arr[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1];
  arr[2] = [1, 1, 2, 2, 2, 2, 2, 2, 2, 1];
  for (let i = 3; i <= step; i++) {
    for (let j = 0; j <= 9; j++) {
      if (j === 0) {
        arr[i][j] = arr[i - 1][j + 1] % MOD;
      } else if (j === 9) {
        arr[i][j] = arr[i - 1][j - 1] % MOD;
      } else {
        arr[i][j] = (arr[i - 1][j - 1] + arr[i - 1][j + 1]) % MOD;
      }
    }
  }
  return arr[step].reduce((a, c) => a + c, 0) % MOD;
}

console.log(solution(input));

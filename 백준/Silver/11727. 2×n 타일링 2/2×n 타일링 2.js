const fs = require("fs");
// TODO: 제출 시 경로 변환 필수 ("/dev/stdin")
const input = Number(
  fs
    .readFileSync("/dev/stdin")
    .toString()
    .trim()
    .replaceAll("\r", "")
    .split("\n")[0]
);

// 풀이
function solution(s) {
  let DP = new Array(s).fill(0);
  DP[1] = 1;
  DP[2] = 3;
  DP[3] = 5;
  for (let i = 4; i <= s; i++) {
    DP[i] = (DP[i - 1] + 2 * DP[i - 2]) % 10007;
  }
  return DP[s];
}

console.log(solution(input));

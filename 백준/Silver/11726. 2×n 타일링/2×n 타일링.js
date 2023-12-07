const fs = require("fs");
// TODO: 제출 시 경로 변환 필수 ("/dev/stdin")
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

// 풀이
function solution(s) {
  s = Number(s);
  const DP = new Array(s + 1).fill(0);
  DP[1] = 1;
  DP[2] = 2;
  for (let i = 3; i <= s; i++) {
    DP[i] = (DP[i - 1] + DP[i - 2]) % 10007;
  }
  return DP[s];
}

console.log(solution(input));

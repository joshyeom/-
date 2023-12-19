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
  const cards = Number(s[0]);
  const DP = new Array(cards + 1).fill(0);
  const price = s[1].split(" ").map(Number);
  for (let i = 1; i <= cards; i++) {
    DP[i] = price[i - 1];
    for (let j = 1; j < i; j++) {
      DP[i] = Math.min(DP[i], DP[i - j] + price[j - 1]);
    }
  }
  return DP[cards];
}

console.log(solution(input));

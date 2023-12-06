const fs = require("fs");
// TODO: 제출 시 경로 변환 필수 ("/dev/stdin")
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

// 풀이
function solution(s) {
  s = s
    .join("")
    .split(" ")
    .map((v) => parseInt(v));
  let [max, min] = [Math.max(...s), Math.min(...s)];
  while (max % min !== 0) {
    [max, min] = [min, max % min];
  }
  return [min, (s[0] * s[1]) / min].join("\n");
}

console.log(solution(input));

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
  const arr = new Array(274).fill(0);
  arr[0] = 0;
  arr[1] = 1;
  arr[2] = 2;
  arr[3] = 4;
  const answer = [];
  for (let i = 4; i <= 10; i++) {
    arr[i] = arr[i - 1] + arr[i - 2] + arr[i - 3];
  }
  for (let i = 1; i <= s[0]; i++) {
    answer.push(arr[s[i]]);
  }
  return answer.join("\n");
}

console.log(solution(input));

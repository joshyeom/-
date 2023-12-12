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
  let stack = [];
  let count = 0;
  for (let i = 0; i < s[0].length; i++) {
    if (s[0][i] === "(") {
      stack.push("(");
    } else {
      if (s[0][i - 1] === "(") {
        stack.pop();
        count += stack.length;
      } else {
        stack.pop();
        count++;
      }
    }
  }
  return count;
}

console.log(solution(input));

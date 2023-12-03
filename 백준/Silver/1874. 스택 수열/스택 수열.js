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
  const arr = new Array(Number(s[0]) + 1)
    .fill(0)
    .map((_, i) => i)
    .slice(1);
  const stack = [];
  const answer = [];
  for (let i = 1; i < s.length + 1; i++) {
    for (let j = Number(s[i]); j >= 0; j--) {
      if (stack[stack.length - 1] === Number(s[i])) {
        answer.push("-");
        stack.pop();
        break;
      }
      stack.push(arr.shift());
      answer.push("+");
    }
    if (stack.includes(undefined)) {
      return "NO";
    }
  }
  return answer.join("\n");
}

console.log(solution(input));

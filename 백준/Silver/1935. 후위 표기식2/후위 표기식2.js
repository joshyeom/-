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
  const stack = [];
  let first = 0;
  let second = 0;
  for (let i = 0; i < s[1].length; i++) {
    switch (s[1][i]) {
      case "+":
        first = stack.pop();
        second = stack.pop();
        stack.push(second + first);
        break;
      case "-":
        first = stack.pop();
        second = stack.pop();
        stack.push(second - first);
        break;
      case "*":
        first = stack.pop();
        second = stack.pop();
        stack.push(second * first);
        break;
      case "/":
        first = stack.pop();
        second = stack.pop();
        stack.push(second / first);
        break;
      default:
        stack.push(Number(s[s[1].charCodeAt(i) - 63]));
    }
  }
  return stack[0].toFixed(2);
}

console.log(solution(input));

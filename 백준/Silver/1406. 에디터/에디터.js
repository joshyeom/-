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
  const leftStack = s[0].split("");
  const rightStack = [];

  for (let i = 2; i < s.length; i++) {
    const [command, value] = s[i].split(" ");

    switch (command) {
      case "L":
        if (leftStack.length != 0) {
          rightStack.push(leftStack.pop());
        }
        break;

      case "D":
        if (rightStack.length != 0) {
          leftStack.push(rightStack.pop());
        }
        break;

      case "B":
        if (leftStack.length != 0) {
          leftStack.pop();
        }
        break;

      case "P":
        leftStack.push(value);
        break;
    }
  }
  return leftStack.concat(rightStack.reverse()).join("");
}

console.log(solution(input));

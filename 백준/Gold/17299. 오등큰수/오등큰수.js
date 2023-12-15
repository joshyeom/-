const fs = require("fs");
// TODO: 제출 시 경로 변환 필수 ("/dev/stdin")
const input = fs
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .replaceAll("\r", "")
  .split("\n")[1];

// 풀이
function solution(s) {
  const arr = s.split(" ").map(Number);
  let answer = new Array(arr.length).fill(-1);
  const count = {};
  const stack = [];
  for (let i of arr) {
    count[i] = (count[i] || 0) + 1;
  }
  for (let i = 0; i < arr.length; i++) {
    while (
      stack.length > 0 &&
      count[arr[stack[stack.length - 1]]] < count[arr[i]]
    ) {
      answer[stack.pop()] = arr[i];
    }
    stack.push(i);
  }
  return answer.join(" ");
}

console.log(solution(input));

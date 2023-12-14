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
  const res = Array(arr.length).fill(-1);
  const stack = [];

  for (let i = 0; i < arr.length; i++) {
    while (stack.length > 0 && stack[stack.length - 1][0] < arr[i]) {
      const [_, idx] = stack.pop();
      res[idx] = arr[i];
    }
    stack.push([arr[i], i]);
  }
  return res.join(" ");
}

console.log(solution(input));

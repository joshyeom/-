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
  const arr = [];
  const answer = [];
  for (let i = 1; i < s.length; i++) {
    const order = s[i].split(" ");
    switch (order[0]) {
      case "push":
        arr.push(Number(order[1]));
        break;
      case "pop":
        arr.length === 0 ? answer.push(-1) : answer.push(arr.shift());
        break;
      case "size":
        answer.push(arr.length);
        break;
      case "empty":
        arr.length === 0 ? answer.push(1) : answer.push(0);
        break;
      case "front":
        arr.length === 0 ? answer.push(-1) : answer.push(Number(arr[0]));
        break;
      case "back":
        arr.length === 0
          ? answer.push(-1)
          : answer.push(Number(arr[arr.length - 1]));
        break;
    }
  }
  return answer.join("\n");
}

console.log(solution(input));

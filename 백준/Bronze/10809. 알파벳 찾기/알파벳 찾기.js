const fs = require("fs");
// TODO: 제출 시 경로 변환 필수 ("/dev/stdin")
const input = fs
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .replaceAll("\r", "")
  .split("\n")[0];

// 풀이
function solution(s) {
  const answer = new Array(26).fill(-1);
  for (let i = 0; i < s.length; i++) {
    if (answer[s.charCodeAt(i) - 97] === -1) {
      answer[s.charCodeAt(i) - 97] = i;
    }
  }
  return answer.join(" ");
}

console.log(solution(input));

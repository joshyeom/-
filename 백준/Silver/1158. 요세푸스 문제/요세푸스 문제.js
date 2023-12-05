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
  const [N, K] = s[0].split(" ");
  const arr = new Array(Number(N)).fill(0).map((_, i) => i + 1);
  const answer = [];
  let count = 0;
  while (arr.length !== 0) {
    count++;
    if (count % Number(K) === 0) {
      answer.push(arr.shift());
    } else {
      arr.push(arr.shift());
    }
  }
  return `<${answer.join(", ")}>`;
}

console.log(solution(input));

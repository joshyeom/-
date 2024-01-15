const fs = require("fs");
// TODO: 제출 시 경로 변환 필수 ("/dev/stdin")
const input = fs
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .replaceAll("\r", "")
  .split("\n")[0];

function solution(sum) {
  let answer = [];

  if (sum.length === 1 && sum[0] === "0") {
    return "0";
  }

  for (let i = 0; i < sum.length; i++) {
    const binaryDigit = parseInt(sum[i], 8).toString(2).padStart(3, "0");
    answer.push(...binaryDigit);
  }

  while (answer[0] === "0") {
    answer.shift();
  }

  return answer.join("");
}

console.log(solution(input));

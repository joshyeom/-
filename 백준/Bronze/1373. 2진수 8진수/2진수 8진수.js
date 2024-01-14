const fs = require("fs");
// TODO: 제출 시 경로 변환 필수 ("/dev/stdin")
const input = fs
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .replaceAll("\r", "")
  .split("\n")[0];

function solution(sum) {
  let binary2 = sum;
  let binary8 = "";
  while (binary2.length >= 3) {
    binary8 =
      parseInt(binary2.slice(binary2.length - 3), 2).toString(8) + binary8;
    binary2 = binary2.slice(0, binary2.length - 3);
  }
  return (binary2 ? parseInt(binary2, 2).toString(8) : "") + binary8;
}

console.log(solution(input));

const fs = require("fs");
// TODO: 제출 시 경로 변환 필수 ("/dev/stdin")
const input = fs
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .replaceAll("\r", "")
  .split("\n");

const getGCD = (a, b) => {
  let r;
  while (b) {
    r = a % b;
    a = b;
    b = r;
  }
  return a;
};

function solution(sum) {
  const subin = +sum[0].split(" ")[1];
  const sisters = sum[1].split(" ").map(Number);
  const distance = sisters.map((v) => Math.abs(v - subin));
  let tmp;
  for (let i = 0; i < distance.length; i++) {
    tmp = getGCD(tmp, distance[i]);
  }
  return tmp;
}

console.log(solution(input));

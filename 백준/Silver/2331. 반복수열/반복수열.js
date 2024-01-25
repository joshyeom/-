const fs = require("fs");
const file = process.platform === "linux" ? "/dev/stdin" : "./test.txt";
const input = fs
  .readFileSync(file)
  .toString()
  .trim()
  .replaceAll("\r", "")
  .split("\n");

function solution(sum) {
  const [A, P] = sum[0].split(" ");
  let D = [];
  D.push(A);
  while (true) {
    const now = D[D.length - 1].split("");
    let total = 0;
    for (let i = 0; i < now.length; i++) {
      const num = Number(now[i]) ** P;
      total += num;
    }
    let str = String(total);
    if (D.includes(str)) {
      return D.slice(0, D.indexOf(str)).length;
    }
    D.push(str);
  }
}
console.log(solution(input));

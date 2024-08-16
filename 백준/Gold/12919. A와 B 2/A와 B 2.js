const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = require("fs")
  .readFileSync(filePath)
  .toString()
  .trim()
  .split("\n");
const S = input[0].trim();
const T = input[1].trim();

let answer = 0;

const dfs = (t) => {
  if (S === t) {
    answer = 1;
    return;
  }
  if (t.length === 0) return;

  if (t[t.length - 1] === "A") {
    const newT = t.slice(0, t.length - 1); // 마지막 'A' 제거
    dfs(newT); // 재귀 호출 및 결과 저장
  }

  if (t[0] === "B") {
    const newT = [...t.slice(1)].reverse().join(""); // 첫 번째 'B' 제거하고 뒤집기
    dfs(newT); // 재귀 호출 및 결과 저장
  }
};

dfs(T);

console.log(answer);

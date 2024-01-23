const fs = require("fs");
// TODO: 제출 시 경로 변환 필수 ("/dev/stdin")
const input = fs
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .replaceAll("\r", "")
  .split("\n");

// 풀이

function solution(sum) {
  const testCase = sum.shift();
  let answer = [];
  for (let i = 0; i < testCase; i++) {
    const visited = {};
    let count = 0;
    const size = sum.shift();
    const node = sum.shift().split(" ");
    const dfs = (from, to) => {
      if (visited[from]) {
        count++;
        return;
      }
      visited[from] = to;
      dfs(to, node[to - 1]);
    };
    for (let j = 0; j < node.length; j++) {
      const from = j + 1;
      const to = node[j];
      if (!visited[from]) {
        dfs(from, to);
      } else if (from === to) {
        visited[from] = to;
        count++;
      }
    }
    answer.push(count);
  }
  return answer.join("\n");
}
console.log(solution(input));

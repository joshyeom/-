const fs = require("fs");
const file = process.platform === "linux" ? "/dev/stdin" : "./test.txt";
const input = fs
  .readFileSync(file)
  .toString()
  .trim()
  .replaceAll("\r", "")
  .split("\n");

function solution(sum) {
  const [N, K] = sum[0].split(" ").map(Number);
  const visited = Array(100001).fill(false);
  const queue = [[N, 0]];

  while (queue.length) {
    const [cur, depth] = queue.shift();
    if (visited[cur]) {
      continue;
    }

    visited[cur] = true;

    if (cur === K) {
      return depth;
    }

    for (let next of [cur + 1, cur - 1, cur * 2]) {
      if (!visited[next] && next >= 0 && next <= 100000) {
        queue.push([next, depth + 1]);
      }
    }
  }
}
console.log(solution(input));

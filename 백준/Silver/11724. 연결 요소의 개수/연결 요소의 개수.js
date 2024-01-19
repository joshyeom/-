const fs = require("fs");
// TODO: 제출 시 경로 변환 필수 ("/dev/stdin")
const input = fs
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .replaceAll("\r", "")
  .split("\n");

// 풀이
function dfs(start) {
  visited[start];
}

function solution(sum) {
  let [node, edge] = sum.shift().split(" ").map(Number);
  let graph = [];
  let answer = 0;
  for (let i = 1; i <= node; i++) {
    graph[i] = [];
  }
  let visited = new Array(node + 1).fill(false);
  for (let i = 0; i < edge; i++) {
    let [from, to] = sum[i].split(" ").map(Number);
    graph[from].push(to);
    graph[to].push(from);
  }

  function dfs(start) {
    visited[start] = true;
    for (let i = 0; i < graph[start].length; i++) {
      let next = graph[start][i];
      if (!visited[next]) {
        dfs(next);
      }
    }
  }

  for (let i = 1; i <= node; i++) {
    if (!visited[i]) {
      dfs(i);
      answer++;
    }
  }

  return answer;
}

console.log(solution(input));

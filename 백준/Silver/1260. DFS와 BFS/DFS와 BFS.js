const fs = require("fs");
// TODO: 제출 시 경로 변환 필수 ("/dev/stdin")
const input = fs
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .replaceAll("\r", "")
  .split("\n");

// 풀이

const DFS = (graph, startNode) => {
  const visited = []; // 탐색을 마친 노드들
  let needVisit = []; // 탐색해야할 노드들

  needVisit.push(startNode); // 노드 탐색 시작

  while (needVisit.length !== 0) {
    // 탐색해야할 노드가 남아있다면
    const node = needVisit.shift(); // queue이기 때문에 선입선출, shift()를 사용한다.
    if (!visited.includes(node)) {
      // 해당 노드가 탐색된 적 없다면
      visited.push(node);
      needVisit = [...graph[node], ...needVisit];
    }
  }
  return visited;
};

const BFS = (graph, startNode) => {
  let visited = []; // 탐색을 마친 노드들
  let needVisit = []; // 탐색해야할 노드들
  needVisit.push(startNode); // 노드 탐색 시작

  while (needVisit.length !== 0) {
    // 탐색해야할 노드가 남아있다면
    const node = needVisit.shift(); // 가장 오래 남아있던 정점을 뽑아냄.
    if (!visited.includes(node)) {
      // 해당 노드 방문이 처음이라면,
      visited.push(node);
      needVisit = [...needVisit, ...graph[node]];
    }
  }
  return visited;
};

function solution(sum) {
  const [node, edge, startNode] = sum[0].split(" ").map(Number);
  let graph = {};
  for (let i = 1; i <= node; i++) {
    graph[i] = [];
  }
  for (let i = 1; i < sum.length; i++) {
    let [from, to] = sum[i].split(" ").map(Number);
    graph[from].push(to);
    graph[to].push(from);
    graph[from] = graph[from].sort((a, b) => a - b);
    graph[to] = graph[to].sort((a, b) => a - b);
  }
  console.log(...DFS(graph, startNode));
  console.log(...BFS(graph, startNode));
}

solution(input);

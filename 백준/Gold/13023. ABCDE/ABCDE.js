const fs = require("fs");
const input = fs
  .readFileSync("dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map((v) => v.split(" ").map(Number));
const [N, M] = input.shift();
let answer = 0;
const friends = Array.from(Array(N), () => []);

input.forEach((v) => {
  const [x, y] = v;
  friends[x].push(y);
  friends[y].push(x);
});

function dfs(value, cnt) {
  visited[value] = true;
  if (answer == 1) return;
  if (cnt == 5) {
    answer = 1;
    return;
  }
  friends[value].forEach((v) => {
    if (!visited[v]) {
      dfs(v, cnt + 1);
    }
  });
  visited[value] = false;
}

let visited = new Array(N).fill(false);
for (let i = 0; i < N; i++) {
  if (answer != 0) break;
  dfs(i, 1);
}

console.log(answer);

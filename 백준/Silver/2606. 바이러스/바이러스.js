const fs = require("fs");
const file = process.platform === "linux" ? "/dev/stdin" : "./test.txt";
const input = fs
  .readFileSync(file)
  .toString()
  .trim()
  .replaceAll("\r", "")
  .split("\n");

function solution(sum) {
  const computer = +sum.shift();
  const edge = sum.shift();
  const map = new Array(computer + 1).fill(null).map(() => []);
  const visited = [];
  let infected = new Set();
  infected.add(1);
  for (let i = 0; i < edge; i++) {
    const [from, to] = sum[i].split(" ").map(Number);
    map[from].push(to);
    map[to].push(from);
  }
  const dfs = (i) => {
    map[i].map((v) => {
      if (visited.includes(v)) {
        return;
      }
      if (Array.from(infected).includes(i)) {
        map[i].map((v) => infected.add(v));
      }
      visited.push(v);
      dfs(v);
    });
  };
  for (let i = 1; i < map.length; i++) {
    dfs(i);
  }
  return Array.from(infected).length - 1;
}
console.log(solution(input));

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
  const line = +sum.shift();
  const map = sum.map((row) => row.split("").map(Number));
  const visited = Array.from(Array(line), () => Array(line).fill(false));
  const dx = [0, 0, -1, 1];
  const dy = [-1, 1, 0, 0];

  let home = 0;
  let complex = 0;
  const answer = [];

  const dfs = (x, y) => {
    if (map[y][x] === 1 && visited[y][x] === false) {
      visited[y][x] = true;
      home += 1;

      for (let i = 0; i < 4; i++) {
        const [newY, newX] = [y + dy[i], x + dx[i]];
        if (newX >= 0 && newX < line && newY >= 0 && newY < line) {
          dfs(newX, newY);
        }
      }
    }
  };
  for (let i = 0; i < line; i++) {
    for (let j = 0; j < line; j++) {
      if (map[j][i] === 1 && visited[j][i] === false) {
        dfs(i, j);
        complex += 1;
        answer.push(home);
        home = 0;
      }
    }
  }
  console.log(complex + "\n" + `${answer.sort((a, b) => a - b).join("\n")}`);
}
solution(input);

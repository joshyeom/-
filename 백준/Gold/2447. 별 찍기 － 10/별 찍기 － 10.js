const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = require("fs")
  .readFileSync(filePath)
  .toString()
  .trim()
  .split("\n");
const N = input[0].trim();

const dfs = (n) => {
  if (n === 1) {
    return ["*"];
  }

  const Stars = dfs(n / 3);
  const L = [];

  for (let i = 0; i < Stars.length; i++) {
    L.push(Stars[i].repeat(3));
  }
  for (let i = 0; i < Stars.length; i++) {
    L.push(Stars[i] + " ".repeat(n / 3) + Stars[i]);
  }
  for (let i = 0; i < Stars.length; i++) {
    L.push(Stars[i].repeat(3));
  }

  return L;
};

console.log(dfs(N).join("\n"));

const fs = require("fs");
// TODO: 제출 시 경로 변환 필수 ("/dev/stdin")
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

// 풀이
function solution(s) {
  let text = s[0];
  let stack = [];
  let isBracket = false;
  let answer = [];
  for (let i = 0; i < text.length; i++) {
    if (text[i] === "<") {
      isBracket = true;
      stack = stack
        .join("")
        .split(" ")
        .map((v) => v.split("").reverse().join(""));
      answer.push(...stack.join(" "));
      stack = [];
    }
    if (text[i] === ">") {
      isBracket = false;
      answer.push(">");
    }
    if (isBracket) {
      answer.push(text[i]);
    } else if (text[i] === ">") {
      continue;
    } else {
      stack.push(text[i]);
    }
  }
  answer.push(
    stack
      .join("")
      .split(" ")
      .map((v) => v.split("").reverse().join(""))
      .join(" ")
  );
  return answer.join("");
}

console.log(solution(input));

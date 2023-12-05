const fs = require("fs");
// TODO: 제출 시 경로 변환 필수 ("/dev/stdin")
const input = fs
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .replaceAll("\r", "")
  .split("\n");

// 풀이
function solution(s) {
  const deck = [];
  const answer = [];
  for (let i = 1; i < s.length; i++) {
    const order = s[i].split(" ");
    switch (order[0]) {
      case "push_front":
        deck.unshift(Number(order[1]));
        break;
      case "push_back":
        deck.push(Number(order[1]));
        break;
      case "pop_front":
        deck.length !== 0 ? answer.push(deck.shift()) : answer.push(-1);
        break;
      case "pop_back":
        deck.length !== 0 ? answer.push(deck.pop()) : answer.push(-1);
        break;
      case "size":
        answer.push(deck.length);
        break;
      case "empty":
        deck.length === 0 ? answer.push(1) : answer.push(0);
        break;
      case "front":
        deck.length === 0 ? answer.push(-1) : answer.push(deck[0]);
        break;
      case "back":
        deck.length === 0
          ? answer.push(-1)
          : answer.push(deck[deck.length - 1]);
        break;
    }
  }
  return answer.join("\n");
}

console.log(solution(input));

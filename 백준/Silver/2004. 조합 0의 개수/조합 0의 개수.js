var fs = require("fs");
var inputs = fs
  .readFileSync("/dev/stdin")
  .toString()
  .split(" ")
  .map((x) => Number(x));
inputs.push(inputs[0] - inputs[1]);
var answer2 = [];
var answer5 = [];
for (var i = 0; i < inputs.length; i++) {
  var n5 = inputs[i];
  var n2 = inputs[i];
  var answer5N = 0;
  var answer2N = 0;
  while (n5 >= 5) {
    answer5N += parseInt(n5 / 5);
    n5 /= 5;
  }
  answer5.push(answer5N);
  while (n2 >= 2) {
    answer2N += parseInt(n2 / 2);
    n2 /= 2;
  }
  answer2.push(answer2N);
}
var result2 = answer5[0] - (answer5[1] + answer5[2]);
var result5 = answer2[0] - (answer2[1] + answer2[2]);
console.log(Math.min(result2, result5));

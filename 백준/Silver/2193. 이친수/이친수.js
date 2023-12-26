const fs = require('fs');
const N = parseInt(fs.readFileSync('/dev/stdin').toString().trimRight());

const d = new Array(N+1).fill(BigInt(0));
d[1] = BigInt(1);
for (let i = 2; i <= N; i++) d[i] = d[i-1] + d[i-2];
console.log(d[N].toString());
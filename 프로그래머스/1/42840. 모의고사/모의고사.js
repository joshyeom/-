function solution(answers) {
    const num1 = [1,2,3,4,5]
    const num2 = [2,1,2,3,2,4,2,5]
    const num3 = [3,3,1,1,2,2,4,4,5,5]
    
    let count1 = 0
    let count2 = 0
    let count3 = 0
    
    answers.forEach((v, i) => {
        if(num1[i % num1.length] === v) count1++
        if(num2[i % num2.length] === v) count2++
        if(num3[i % num3.length] === v) count3++
    })
    
    const maxNum = Math.max(count1, count2, count3)
    
    const answer = []
    
    if (count1 === maxNum) answer.push(1);
    if (count2 === maxNum) answer.push(2);
    if (count3 === maxNum) answer.push(3);
    
    return answer.sort((a, b) => a - b)
}
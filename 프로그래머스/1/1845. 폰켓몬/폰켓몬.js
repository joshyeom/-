function solution(nums) {
    const mySet = new Set(nums)
    const maxNum = nums.length / 2
    return maxNum > mySet.size ? mySet.size : maxNum
}
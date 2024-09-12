def solution(nums):
    my_set = set()
    for num in nums:
        my_set.add(num)
    arr = list(my_set)
    
    max = len(nums) / 2
    if max < len(arr):
        return max
    else:
        return len(arr)
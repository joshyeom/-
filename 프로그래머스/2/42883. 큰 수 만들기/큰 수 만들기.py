def solution(num, k):
    stack = []
    for digit in num:
        while stack and k > 0 and stack[-1] < digit:
            stack.pop()
            k -= 1
        stack.append(digit)
    
    return ''.join(stack[:len(num)-k])
def is_prime(num):
    if num <= 1:
        return False
    if num == 2 or num == 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def binary(n, k):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, k)
        rev_base += str(mod)

    return rev_base[::-1] 



def solution(n, k):
    answer = 0
    current_number = ''
    k_base_number = binary(n, k)
    
    for char in k_base_number:
        if char != '0':
            current_number += char
            
        else:
            if current_number:
                num = int(current_number)
                if is_prime(num):
                    answer += 1
                    current_number = ''
                else:
                    current_number = ''
                    
    if current_number:
        num = int(current_number)
        if is_prime(num):
            answer += 1
            
    return answer
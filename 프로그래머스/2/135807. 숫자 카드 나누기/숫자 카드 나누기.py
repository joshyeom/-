import math

def get_result_gcd(array):
  gcd = 0
  i = 0

  while i < len(array):
    if gcd == 0:
      gcd = array[i]
    else:
      gcd = math.gcd(gcd, array[i])
    i += 1
  

  return gcd


def solution(arrayA, arrayB):
    result_a = get_result_gcd(arrayA)
    result_b = get_result_gcd(arrayB)



    max_num = 0

    if result_a > result_b:
      max_num = [result_a, 'a']
    else:
      max_num = [result_b, 'b']
    


    if max_num[1] == 'b':
      for i in arrayA:
        if i % max_num[0] == 0:
          return 0

    else:
      for i in arrayB:
        if i % max_num[0] == 0:
          return 0


    
    
    return max_num[0]
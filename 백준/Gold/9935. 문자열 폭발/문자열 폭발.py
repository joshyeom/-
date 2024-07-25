import sys
input = sys.stdin.readline

str_string = input().strip()  # 원본 문자열
bomb_string = input().strip()  # 제거할 부분 문자열

stack = []

# 스택을 사용하여 문자열 처리
for char in str_string:
    stack.append(char)
    
    # 스택의 끝부분이 bomb 문자열과 일치하는지 확인
    if "".join(stack[-len(bomb_string):]) == bomb_string:
        # 부분 문자열이 일치하면 제거
        del stack[-len(bomb_string):]

# 결과 문자열 생성
result = "".join(stack)

# 결과 출력
if result:
    print(result)
else:
    print("FRULA")
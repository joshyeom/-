a, b = map(int, input().split())
answer = ""

if(a > b):
  answer = ">"
elif(a < b):
  answer = "<"
else:
  answer = "=="

print(answer)